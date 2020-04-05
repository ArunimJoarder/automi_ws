#!/usr/bin/env python3

import rospy
from dynamixel_sdk import *                    # Uses Dynamixel SDK library

BIPED_DEVICE = rospy.get_param("/comm_config/biped_port")
TORSO_DEVICE = rospy.get_param("/comm_config/torso_port")

BAUDRATE = rospy.get_param("/comm_config/baudrate")

biped_portHandler = PortHandler(BIPED_DEVICE)
torso_portHandler = PortHandler(TORSO_DEVICE)

# Open port
def open_ports():
    if biped_portHandler.openPort() and torso_portHandler.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        quit()


# Set port baudrate
def set_baudrates():
    if biped_portHandler.setBaudRate(BAUDRATE) and torso_portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        quit()


def close_ports():
    biped_portHandler.closePort()
    torso_portHandler.closePort()