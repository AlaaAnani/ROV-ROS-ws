#!/usr/bin/env python

import rospy
from GUI.msg import cannonNumbers
from std_msgs.msg import String
import numpy as np

canon_calc_pub = rospy.Publisher('calculated_cannon_numbers', cannonNumbers, queue_size=10)

cannon_numbers = cannonNumbers()
specific_gravity = 0.0

def calculate_cannon():
    global cannon_numbers
    global specific_gravity
    arg1 = ((1.0/3.0) * pow (cannon_numbers.r3 - cannon_numbers.r1,2))
    arg2 = (cannon_numbers.r1 * (cannon_numbers.r3 - cannon_numbers.r1))
    arg3 = pow(cannon_numbers.r1, 2)
    arg4 = pow(cannon_numbers.r2, 2)
    cannon_numbers.vol = np.pi * cannon_numbers.l * ((arg1 + arg2) + (arg3) - (arg4))
    Mass = (cannon_numbers.vol * 1e-6) * specific_gravity
    cannon_numbers.weight = 9.81 * Mass


def cannon_callback(msg):
    global cannon_numbers
    cannon_numbers = msg
    calculate_cannon()
    canon_calc_pub.publish(cannon_numbers)


def flag_callback(msg):
    global specific_gravity
    if(str(msg.data) == 'start_AF'):
        specific_gravity = 8030.0
    elif(str(msg.data) == 'start_else'):
        specific_gravity = 7870.0

def listener():
     rospy.init_node('calculations', anonymous=True)
     rospy.Subscriber('cannon_numbers', cannonNumbers, cannon_callback)
     rospy.Subscriber('cannon_flag', String, flag_callback)
     rospy.spin()
 

if __name__ == '__main__':
    listener()