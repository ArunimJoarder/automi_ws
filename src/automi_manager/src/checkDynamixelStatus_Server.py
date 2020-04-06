#!/usr/bin/env python

import rospy
from dynamixel_sdk import *                    # Uses Dynamixel SDK library

from comm_setup import *

from std_srvs.srv import Trigger


packetHandler = [PacketHandler(2.0), PacketHandler(1.0)]

# Get Dynamixels ID & Protocols
biped_dxls = rospy.get_param("/general/biped_dxls")

# Get Address and Length of Hardware Error in MX(2.0)
hardware_error = rospy.get_param("/dynamixel_config/MX_2/hardware_error")

def checkStatus(req):
    resp = {'success': True, 'message': 'No Error'}
    # for i in range(len(biped_dxls)):
    #     if biped_dxls[1][1] == 2:
    #         value, dxl_comm_result, dxl_error = packetHandler[0].read1ByteTxRx(biped_portHandler, biped_dxls[i]['id'], hardware_error['addr'])
    #         if value == 0:
    #             resp['success'] = False
    #             resp['message'] = str(packetHandler[0].getRxPacketError(value))
    #             rospy.set_param("status/failed", True)
    #             break
    
    return resp

def checkStatus_server():
    rospy.init_node('checkDynamixelStatus_server')
    s = rospy.Service('checkDynamixelStatus', Trigger, checkStatus)
    rospy.spin()

if __name__ == "__main__":
    checkStatus_server()