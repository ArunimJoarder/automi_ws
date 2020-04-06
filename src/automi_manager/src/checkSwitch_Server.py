#!/usr/bin/env python

import rospy

from automi_manager.srv import switchTrigger

def checkGuards(req):
    resp = {'mode': rospy.get_param("/switches/behave_mode"),
            'mode_index': rospy.get_param("/switches/switch_index")}

    if req.check == True:
        # check individual guard conditions
        # combine CV and sensor data to decide what to do - walk, turn, stand, rise
        
        resp = {'mode': 'walk',
                'mode_index': 1}
        pass
    # print(resp)
    return resp

def checkSwitch_server():
    rospy.init_node('checkSwitch_server')
    s = rospy.Service('checkSwitch', switchTrigger, checkGuards)
    rospy.spin()

if __name__ == "__main__":
    checkSwitch_server()
