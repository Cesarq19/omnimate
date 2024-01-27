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

## :books: Package Summary

- :ledger: [`yahboom_new_description`](./Omnimate_ros1/yahboom_new_description): Contains the URDF description of the robot.
- :compass: [`yahboom_nav`](./Omnimate_ros1/yahboom_nav/): Navigation stack based on `nav_core`.
- :world_map: [`yahboom_slam`](./Omnimate_ros1/yahboom_slam/): Provides support for SLAM with your `yahboom` robot.
- :video_game: [`yahboom_ctrl`](./Omnimate_ros1/yahboomcar_ctrl/): Allows the robot to be moved using keyboard commands and wireless control.

