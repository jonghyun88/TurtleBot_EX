#! /usr/bin/env python 
# This line will ensure the interpreter used is the first one on your environment's $PATH. Every Python file needs
# to start with this line at the top.

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import atexit


def callback(msg):
    
    # print(msg.ranges)
    move = Twist()
    # print(len(msg.ranges))
    # print(msg.ranges)

    if (msg.ranges[90] < 0.3 or msg.ranges[120] < 0.3 or msg.ranges[60] < 0.3): # if robot place obstacle distance under 1m, turn right or turn left 
        print("turn")
        
        if (msg.ranges[135] <= 0.5 and msg.ranges[45] <= msg.ranges[135] ):
            print("right")
            move.linear.x = 0
            move.angular.z = -0.2 #Move the with an angular velocity in the z axis
            pub.publish(move)
            rate.sleep()

        elif (msg.ranges[45] <= 0.5 and msg.ranges[135] <= msg.ranges[45] ):
            print("left")
            move.linear.x = 0
            move.angular.z = 0.2 #Move the with an angular velocity in the z axis
            pub.publish(move)
            rate.sleep()

        else:
            print("--")
            move.linear.x = 0
            move.angular.z = 0.2 #Move the with an angular velocity in the z axis
            pub.publish(move)
            rate.sleep()
    else:
        move.linear.x = 0.1
        print("go")
        pub.publish(move)
    


rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rate = rospy.Rate(8)
rospy.spin()
