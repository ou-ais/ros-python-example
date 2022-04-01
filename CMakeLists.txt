cmake_minimum_required(VERSION 3.0.2)
project(ros_python_examples)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

# Generate messages in the 'msg' folder
add_message_files(
  FILES
  Num.msg
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  AddTwoInts.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
catkin_install_python(PROGRAMS
  script/ros_numpy_talker.py
  script/ros_numpy_listener.py
  script/add_two_ints_server.py
  script/add_two_ints_client.py 
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
