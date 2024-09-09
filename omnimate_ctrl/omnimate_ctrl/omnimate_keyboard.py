#!/usr/bin/env python
# encoding: utf-8
# import public lib
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# import ros lib
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

msg = """
Control Your SLAM-Bot!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
t/T : x and y speed switch
s/S : stop keyboard control
space key, k : force stop
anything else : stop smoothly

CTRL-C to quit
"""

moveBindings = {
    "i": (1, 0),
    "o": (1, -1),
    "j": (0, 1),
    "l": (0, -1),
    "u": (1, 1),
    ",": (-1, 0),
    ".": (-1, 1),
    "m": (-1, -1),
    "I": (1, 0),
    "O": (1, -1),
    "J": (0, 1),
    "L": (0, -1),
    "U": (1, 1),
    "M": (-1, -1),
}

speedBindings = {
    "Q": (1.1, 1.1),
    "Z": (0.9, 0.9),
    "W": (1.1, 1),
    "X": (0.9, 1),
    "E": (1, 1.1),
    "C": (1, 0.9),
    "q": (1.1, 1.1),
    "z": (0.9, 0.9),
    "w": (1.1, 1),
    "x": (0.9, 1),
    "e": (1, 1.1),
    "c": (1, 0.9),
}


class Omnimate_keyboard(Node):
    def __init__(self, name):
        super().__init__(name)
        self.pub = self.create_publisher(Twist, "cmd_vel", 1)
        self.declare_parameter("linear_speed_limit", 1.0)
        self.declare_parameter("angular_speed_limit", 5.0)
        self.linenar_speed_limit = (
            self.get_parameter("linear_speed_limit").get_parameter_value().double_value
        )
        self.angular_speed_limit = (
            self.get_parameter("angular_speed_limit").get_parameter_value().double_value
        )
        self.settings = termios.tcgetattr(sys.stdin)

    def getKey(self):
        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ""
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def vels(self, speed, turn):
        return "currently:\tspeed %s\tturn %s " % (speed, turn)


def main():
    rclpy.init()
    omnimate_keyboard = Omnimate_keyboard("omnimate_keyboard_ctrl")
    xspeed_switch = True
    (speed, turn) = (0.2, 1.0)
    (x, th) = (0, 0)
    status = 0
    stop = False
    count = 0
    twist = Twist()
    try:
        print(msg)
        print(omnimate_keyboard.vels(speed, turn))
        while 1:
            key = omnimate_keyboard.getKey()
            if key == "t" or key == "T":
                xspeed_switch = not xspeed_switch
            elif key == "s" or key == "S":
                print("stop keyboard control: {}".format(not stop))
                stop = not stop
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                th = moveBindings[key][1]
                count = 0
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]
                count = 0
                if speed > omnimate_keyboard.linenar_speed_limit:
                    speed = omnimate_keyboard.linenar_speed_limit
                    print("Linear speed limit reached!")
                if turn > omnimate_keyboard.angular_speed_limit:
                    turn = omnimate_keyboard.angular_speed_limit
                    print("Angular speed limit reached!")
                print(omnimate_keyboard.vels(speed, turn))
                if status == 14:
                    print(msg)
                status = (status + 1) % 15
            elif key == " ":
                (x, th) = (0, 0)
            else:
                count = count + 1
                if count > 4:
                    (x, th) = (0, 0)
                if key == "\x03":
                    break
            if xspeed_switch:
                twist.linear.x = speed * x
            else:
                twist.linear.y = speed * x
            twist.angular.z = turn * th
            if not stop:
                omnimate_keyboard.pub.publish(twist)
            if stop:
                omnimate_keyboard.pub.publish(Twist())
    except Exception as e:
        print(e)
    finally:
        omnimate_keyboard.pub.publish(Twist())
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, omnimate_keyboard.settings)
    omnimate_keyboard.destroy_node()
    rclpy.shutdown()