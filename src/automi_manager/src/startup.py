#!/usr/bin/env python3

import rospy
from dynamixel_sdk import *                    # Uses Dynamixel SDK library
from comm_setup import biped_portHandler, torso_portHandler

def setup():
    packetHandler = [PacketHandler(2.0), PacketHandler(1.0)]

    # Get setup parameters
    drive_mode  = rospy.get_param("/dynamixel_config/MX_2/drive_mode")
    prf_vel     = rospy.get_param("/dynamixel_config/MX_2/prf_vel")
    prf_acc     = rospy.get_param("/dynamixel_config/MX_2/prf_acc")
    max_vel     = rospy.get_param("/dynamixel_config/MX_2/max_vel")
    p_gain_pos  = rospy.get_param("/dynamixel_config/MX_2/p_gain_pos")
    i_gain_pos  = rospy.get_param("/dynamixel_config/MX_2/i_gain_pos")
    d_gain_pos  = rospy.get_param("/dynamixel_config/MX_2/d_gain_pos")

    moving_vel  = rospy.get_param("/dynamixel_config/AX_1/moving_vel")

    # Biped setup parameters
    biped_dxls  = rospy.get_param("/general/biped_dxls")

    for i in range(len(biped_dxls)):
        if (biped_dxls[i][1] == 2):
            dxl_comm_result, dxl_error = packetHandler[0].write2ByteTxRx(biped_portHandler, biped_dxls[i][0], drive_mode[0], 4)
            dxl_comm_result, dxl_error = packetHandler[0].write4ByteTxRx(biped_portHandler, biped_dxls[i][0], prf_vel[0], rospy.get_param("/general/prf_vel"))
            dxl_comm_result, dxl_error = packetHandler[0].write4ByteTxRx(biped_portHandler, biped_dxls[i][0], prf_acc[0], rospy.get_param("/general/prf_acc"))
            dxl_comm_result, dxl_error = packetHandler[0].write4ByteTxRx(biped_portHandler, biped_dxls[i][0], max_vel[0], rospy.get_param("/general/max_vel"))
            dxl_comm_result, dxl_error = packetHandler[0].write2ByteTxRx(biped_portHandler, biped_dxls[i][0], p_gain_pos[0], rospy.get_param("/general/p_gain_pos"))
            dxl_comm_result, dxl_error = packetHandler[0].write2ByteTxRx(biped_portHandler, biped_dxls[i][0], i_gain_pos[0], rospy.get_param("/general/i_gain_pos"))
            dxl_comm_result, dxl_error = packetHandler[0].write2ByteTxRx(biped_portHandler, biped_dxls[i][0], d_gain_pos[0], rospy.get_param("/general/d_gain_pos"))
        else:
            dxl_comm_result, dxl_error = packetHandler[1].write2ByteTxRx(biped_portHandler, biped_dxls[i][0], moving_vel[0], rospy.get_param("/general/moving_vel"))
        
        if dxl_comm_result != COMM_SUCCESS:
            print(packetHandler[0].getTxRxResult(dxl_comm_result), biped_dxls[i][0])
        elif dxl_error != 0:
            print(packetHandler[0].getRxPacketError(dxl_error), biped_dxls[i][0])

    # Torso setup parameters
    torso_dxls = rospy.get_param("/general/torso_dxls")

    for i in range(len(torso_dxls)):
        dxl_comm_result, dxl_error = packetHandler[1].write2ByteTxRx(torso_portHandler, torso_dxls[i][0], moving_vel[0], rospy.get_param("/general/moving_vel"))
        
        if dxl_comm_result != COMM_SUCCESS:
            print(packetHandler[1].getTxRxResult(dxl_comm_result), torso_dxls[i][0])
        elif dxl_error != 0:
            print(packetHandler[1].getRxPacketError(dxl_error), torso_dxls[i][0])

