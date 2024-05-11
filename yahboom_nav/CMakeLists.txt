cmake_minimum_required(VERSION 2.8.3)
project(yahboom_nav)

find_package(catkin REQUIRED COMPONENTS 
    rospy)

catkin_package()

install(DIRECTORY launch maps param rviz
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

include_directories(
    ${catkin_INCLUDE_DIRS}
)