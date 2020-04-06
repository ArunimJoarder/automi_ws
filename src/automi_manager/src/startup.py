#!/usr/bin/env python3

import rospy
from dynamixel_sdk import *                    # Uses Dynamixel SDK library

def setup(biped_portHandler, torso_portHandler):
    packetHandler = [PacketHandler(2.0), PacketHandler(1.0)]

    # Get setup parameters
        # MX Parameters
    drive_mode  = rospy.get_param("/dynamixel_config/MX_2/drive_mode")
    prf_vel     = rospy.get_param("/dynamixel_config/MX_2/prf_vel")
    prf_acc     = rospy.get_param("/dynamixel_config/MX_2/prf_acc")
    max_vel     = rospy.get_param("/dynamixel_config/MX_2/max_vel")
    p_gain_pos  = rospy.get_param("/dynamixel_config/MX_2/p_gain_pos")
    i_gain_pos  = rospy.get_param("/dynamixel_config/MX_2/i_gain_pos")
    d_gain_pos  = rospy.get_param("/dynamixel_config/MX_2/d_gain_pos")
        # AX Parameters
    moving_vel  = rospy.get_param("/dynamixel_config/AX_1/moving_vel")

    # Get setup values
        # MX Values
    drive_mode_value  = 4
    prf_vel_value     = rospy.get_param("/general/prf_vel")
    prf_acc_value     = rospy.get_param("/general/prf_acc")
    max_vel_value     = rospy.get_param("/general/max_vel")
    p_gain_pos_value  = rospy.get_param("/general/p_gain_pos")
    i_gain_pos_value  = rospy.get_param("/general/i_gain_pos")
    d_gain_pos_value  = rospy.get_param("/general/d_gain_pos")
        # AX Values
    moving_vel_value  = rospy.get_param("/general/moving_vel")

    # Biped setup parameters
    biped_dxls  = rospy.get_param("/general/biped_dxls")

    for i in range(len(biped_dxls)):
        if (biped_dxls[i]['protocol'] == 2):
            dxl_comm_result, dxl_error = packetHandler[0].write2ByteTxRx(biped_portHandler, biped_dxls[i]['id'], drive_mode['addr'], drive_mode_value)
            dxl_comm_result, dxl_error = packetHandler[0].write4ByteTxRx(biped_portHandler, biped_dxls[i]['id'], prf_vel['addr'], prf_vel_value)
            dxl_comm_result, dxl_error = packetHandler[0].write4ByteTxRx(biped_portHandler, biped_dxls[i]['id'], prf_acc['addr'], prf_acc_value)
            dxl_comm_result, dxl_error = packetHandler[0].write4ByteTxRx(biped_portHandler, biped_dxls[i]['id'], max_vel['addr'], max_vel_value)
            dxl_comm_result, dxl_error = packetHandler[0].write2ByteTxRx(biped_portHandler, biped_dxls[i]['id'], p_gain_pos['addr'], p_gain_pos_value)
            dxl_comm_result, dxl_error = packetHandler[0].write2ByteTxRx(biped_portHandler, biped_dxls[i]['id'], i_gain_pos['addr'], i_gain_pos_value)
            dxl_comm_result, dxl_error = packetHandler[0].write2ByteTxRx(biped_portHandler, biped_dxls[i]['id'], d_gain_pos['addr'], d_gain_pos_value)
        else:
            dxl_comm_result, dxl_error = packetHandler[1].write2ByteTxRx(biped_portHandler, biped_dxls[i]['id'], moving_vel['addr'], moving_vel_value)
        
        if dxl_comm_result != COMM_SUCCESS:
            print(packetHandler[0].getTxRxResult(dxl_comm_result), biped_dxls[i]['id'])
        elif dxl_error != 0:
            print(packetHandler[0].getRxPacketError(dxl_error), biped_dxls[i]['id'])

    # Torso setup parameters
    torso_dxls = rospy.get_param("/general/torso_dxls")

    for i in range(len(torso_dxls)):
        dxl_comm_result, dxl_error = packetHandler[1].write2ByteTxRx(torso_portHandler, torso_dxls[i]['id'], moving_vel['addr'], moving_vel_value)
        
        if dxl_comm_result != COMM_SUCCESS:
            print(packetHandler[1].getTxRxResult(dxl_comm_result), torso_dxls[i]['id'])
        elif dxl_error != 0:
            print(packetHandler[1].getRxPacketError(dxl_error), torso_dxls[i]['id'])

