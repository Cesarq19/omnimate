<div align="center">

  # Yahboom ROSMASTER X3 PLus

</div>

<p align="center">
  <img src="docs/robot.png" width=300 />
</p>

ROSMASTER X3 PLUS is an omnidirectional motion robot developed based on the ROS robot operating system.
Supports four controllers: Jetson NANO 4GB/Xavier NX/TX2 NX and Raspberry Pi 4B.
It is equipped with high-performance hardware configurations such as lidar, depth camera, high-power 520 motor, interactive voice recognition module and 7-inch HD screen.
It can realize applications such as mapping and application navigation, automatic driving, human feature recognition.
Support remote control of mobile phones, handles, computer keyboards.

## :wrench: Setting up

To start, you will need to connect via SSH to the jetson nano, using your credentials:

`user`: jetson
`password`: yahboom

And taking into account that the external machine (PC) is connected to the `RAMEL_5G` network


```
ssh jetson@192.168.31.109
```

Once started, the commands can be executed to put the robot into operation, using:

```
roslaunch yahboomcar_bringup bringup.launch
```

In this case, the package corresponding to teleoperation with the remote control will not have to be started externally, since it is called automatically, you only have to verify that the control is linked to the robot, which is the case when the light indicator stays on constantly.

