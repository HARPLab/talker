cmake_minimum_required(VERSION 2.8.3)
project(talker)

find_package(catkin REQUIRED
    genmsg
    actionlib_msgs
    actionlib)

catkin_python_setup()

add_action_files(DIRECTORY action)

generate_messages(DEPENDENCIES actionlib_msgs)

catkin_package()

install(PROGRAMS scripts/say.py
    DESTINATION "${CATKIN_PACKAGE_BIN_DESTINATION}")

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)
