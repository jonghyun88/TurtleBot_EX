#! /usr/bin/env python

import rospy
from services_turtlebot.srv import turtlebotCustomServiceMessage, turtlebotCustomServiceMessageResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo("The Service move_turtlebot_in_square_custom has been called")
    k = 0

    move_square.linear.x = 0.5
    my_pub.publish(move_square)
    rate.sleep()

    while k <= request.repetitions:
        # print(k)
        i = 0
        j = 0
    
        while i <= request.side: 
            move_square.linear.x = 0.2
            move_square.angular.z = 0
            my_pub.publish(move_square)
            rate.sleep()
            # print(i)
            i += 1
        
        while j <= 7:
            move_square.linear.x = 0
            move_square.angular.z = 0.2
            my_pub.publish(move_square)
            rate.sleep()
            # print(j)
            j += 1

        # print(k)
        k += 1
    
    rospy.loginfo("Finished service move_turtlebot_in_square_custom")

    move_square.angular.z = 0
    my_pub.publish(move_square)

    response = turtlebotCustomServiceMessageResponse()
    response.success = True
    
    return response # the service Response class, in this case EmptyResponse



rospy.init_node('service_move_turtlebot_in_square_custom_server') 
my_service = rospy.Service('/move_turtlebot_in_square_custom', turtlebotCustomServiceMessage, my_callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_square = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_turtlebot_in_square_custom Ready")

rospy.spin() # mantain the service open.