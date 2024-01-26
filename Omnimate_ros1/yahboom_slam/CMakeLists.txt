find_package(catkin REQUIRED)
cmake_minimum_required(VERSION 3.0.2)
project(yahboom_slam)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  sensor_msgs
)
catkin_package(
        #  INCLUDE_DIRS include
        #  LIBRARIES yahboomcar_description
        #  CATKIN_DEPENDS roscpp rosmsg rospy
        #  DEPENDS system_lib
)

include_directories(
        # include
        ${catkin_INCLUDE_DIRS}
)

