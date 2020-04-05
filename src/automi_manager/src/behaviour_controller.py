#!/usr/bin/env python3

import rospy
import atexit
from dynamixel_sdk import *                    # Uses Dynamixel SDK library
from comm_setup import *
import startup

# Import all behaviours
import walk
import turn
import stand
import rise
import initialise

def on_shutdown():
    # close_ports()
    print('\ngot into \'on_shutdown\'\n')

def behaviourControl():
    # open_ports()
    # set_baudrates()

    rospy.init_node('behaviourControl', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    
    if rospy.get_param("/switches/startup"):
        # startup.setup()
        rospy.set_param("/switches/startup", False)
        print('/switches/startup = ', rospy.get_param("/switches/startup"))
    
    if not rospy.get_param("/switches/initialised"):
        # initialise.init(biped_portHandler, torso_portHandler)
        rospy.set_param("/switches/initialised", True)
        print('/switches/initialised = ', rospy.get_param("/switches/initialised"))
    
    while not rospy.get_param("/switches/autonomous"):
        r = input('Press ENTER to continue')
        print('passed input line')
        rospy.set_param("/switches/autonomous", True)
        print('/switches/autonomous = ', rospy.get_param("/switches/autonomous"))


    while not rospy.is_shutdown():
        pass
        

if __name__ == '__main__':
    try:
        behaviourControl()
        atexit.register(on_shutdown)
    except rospy.ROSInterruptException:
        # print('got here')
        pass