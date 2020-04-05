import rospy
from comm_setup import *
from dynamixel_sdk import *                    # Uses Dynamixel SDK library

open_ports()
set_baudrates()

packetHandler = [PacketHandler(2.0), PacketHandler(1.0)]

# Biped setup parameters
biped_dxls = rospy.get_param("/general/biped_dxls")
