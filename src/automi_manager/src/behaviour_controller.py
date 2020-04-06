#!/usr/bin/env python3

# Import libraries
import rospy
import atexit
from dynamixel_sdk import *                    # Uses Dynamixel SDK library

# Import utility files
from comm_setup import *
import startup

# Import all behaviours
import walk
import turn
import stand
import rise
import initialise

# Import Messages and Services
from automi_manager.srv import switchTrigger
from std_srvs.srv import Trigger

def on_shutdown():
    # close_ports()
    print('closing Dynamixel ports')

def trySwitch():
    rospy.wait_for_service('checkSwitch')
    try:
        checkSwitch = rospy.ServiceProxy("checkSwitch", switchTrigger)
        response = checkSwitch(rospy.get_param("/switches/check"))

        rospy.set_param("/switches/behave_mode", response.mode)
        rospy.set_param("/switches/switch_index", response.mode_index)
        print(response.mode, response.mode_index)
    except rospy.ServiceException:
        print("Service call for \'checkSwitch\' failed")

def findStatus():
    rospy.wait_for_service("checkDynamixelStatus")
    try:
        checkStatus = rospy.ServiceProxy("checkDynamixelStatus", Trigger)
        response = checkStatus()
        
        if not response.success:            # If there is Hardware Error in Dynamixels
            rospy.set_param("/switches/behave_mode", 'stand')
            rospy.set_param("/switches/switch_index", 0)
        
        else:
            pass

    except rospy.ServiceException:
        print("Service call for \'checkDynamixelStatus\' failed")

def behaviourControl():
    # open_ports()
    # set_baudrates()

    rospy.init_node('behaviourControl', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    
    if rospy.get_param("/switches/startup"):
        # startup.setup(biped_portHandler, torso_portHandler)
        rospy.set_param("/switches/startup", False)
        print('\'/switches/startup\' = ', rospy.get_param("/switches/startup"))
    
    if not rospy.get_param("/switches/initialised"):
        # initialise.init(biped_portHandler, torso_portHandler)
        rospy.set_param("/switches/initialised", True)
        print('\'/switches/initialised\' = ', rospy.get_param("/switches/initialised"))
    
    while not rospy.get_param("/switches/autonomous"):
        r = input('Press ENTER to continue')
        # print('passed input line')
        rospy.set_param("/switches/autonomous", True)
        print('\'/switches/autonomous\' = ', rospy.get_param("/switches/autonomous"))

    print('check')
    while not rospy.is_shutdown():

        trySwitch()                 # checks conditions to switch to particular behaviour

        findStatus()                # checks whether any Dynamixel has had Hardware Error

        switch = rospy.get_param("/switches/switch_index")
        
        if switch == 0:
            # stand.stand(biped_portHandler, torso_portHandler)
            pass
        elif switch == 1:
            # walk.walk(biped_portHandler, torso_portHandler)
            pass
        elif switch == 2:
            # turn.turn(biped_portHandler, torso_portHandler)
            pass
        elif switch == 4:
            # rise.rise(biped_portHandler, torso_portHandler)
            pass
        print('2')
        pass
        

if __name__ == '__main__':
    try:
        behaviourControl()
        atexit.register(on_shutdown)
    except rospy.ROSInterruptException:
        pass