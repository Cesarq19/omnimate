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

<div align="center">

  # Simulation packages ROS1

</div>

## :books: Package Summary

- :ledger: [`yahboom_new_description`](./yahboom_new_description): Contains the URDF description of the robot.
- :compass: [`yahboom_nav`](./yahboom_nav/): Navigation stack based on `nav_core`.
- :world_map: [`yahboom_slam`](./yahboom_slam/): Provides support for SLAM with your `yahboom` robot.
- :video_game: [`yahboom_ctrl`](./yahboomcar_ctrl/): Allows the robot to be moved using keyboard commands and wireless control.

## :wrench: Description of the robot
El diseño del robot sufrio cambios a medida de que se fue haciendo sus implementaciones, al principio se uso como referencia el modelo CAD del Yahboom ROSMASTER X3, sin embargo se realizo un cambio radical en base a los nuevos cambios de hardware, resultando:

<p align="center">
  <img src="/docs/robot.png" width=300 />
</p>


#### Workspace

Packages here provided are catkin packages. As such a catkin workspace is expected:

1. Create catkin workspace

```
mkdir -p ~/ws/src
```

2. Clone this repository in the `src` folder

```
cd ~/ws/src
```

```
git clone https://github.com/RAMEL-ESPOL/Omnimate.git
```

3. Install dependencies via `rosdep`

```
cd ~/ws
```

```
rosdep install --from-paths src --ignore-src -i -y
```

4. Build the packages

```
catkin_make
```

5. Finally, source the built packages
   If using `bash`:

```
source devel/setup.bash
```

`Note`: Whether your are installing the packages in your dev machine or in your robot the procedure is the same.

## :rocket: Usage

### Teleoperation

Launch files for using the keyboard or a joystick for teleoperating the robot are provided.

[`twist_mux`](http://wiki.ros.org/twist_mux) is used to at the same time accept command velocities from different topics using certain priority for each one of them (See [twist_mux config](https://github.com/ros-teleop/twist_mux/blob/melodic-devel/config/joystick.yaml)). Available topics are (ordering by priority):

- cmd_vel
- cmd_vel_keyboard
- cmd_vel_joy

### RViz

Use:

```
roslaunch yahboom_new_description display.launch
```

For starting `rviz` visualization with a provided configuration.

<img src="/docs/rviz_robot.png" width=400/>

## :computer: Simulation

The [`yahboom_gz`](./yahboom_new_description/launch/gazebo.launch) package provides a Gazebo simulation for the Yahboom robot.

<img src="/docs/gazebo_robot.png" width=400/>

## Slam

Using the robot for mapping.

<img src="/docs/slam_robot.png" width=400/>

See [`yahboom_slam`](./yahboom_slam/) for more information.

## :compass: Navigation

The [`yahboom_nav`](./yahboom_nav/launch/navigation.launch) package provides a navigation stack based on the great AMCL package.



https://github.com/RAMEL-ESPOL/Omnimate/assets/90804290/0648415d-6822-4050-bd19-e20bbc07cd83


