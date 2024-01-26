cmake_minimum_required(VERSION 2.8.3)
project(yahboom_new_description)

find_package(catkin REQUIRED COMPONENTS
  urdf
  xacro
  roscpp
  std_msgs
  geometry_msgs
  nav_msgs
  tf
  gazebo_ros
)

find_package(gazebo REQUIRED)

catkin_package(
  CATKIN_DEPENDS urdf xacro
)

link_directories(${GAZEBO_LIBRARY_DIRS})

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
)

install(DIRECTORY meshes rviz urdf launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)