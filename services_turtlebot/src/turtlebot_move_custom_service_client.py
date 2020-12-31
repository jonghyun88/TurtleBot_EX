#! /usr/bin/env python

import rospkg
import rospy
# from std_srvs.srv import Empty, EmptyRequest # you import the service message python classes generated from Empty.srv.
from services_turtlebot.srv import turtlebotCustomServiceMessage, turtlebotCustomServiceMessageRequest

rospy.init_node('service_move_turtlebot_in_square_custom_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/move_turtlebot_in_square_custom') # Wait for the service client /move_bb8_in_circle to be running
move_turtlebot_in_square_service_client = rospy.ServiceProxy('/move_turtlebot_in_square_custom', turtlebotCustomServiceMessage) # Create the connection to the service
move_turtlebot_in_square_request_object = turtlebotCustomServiceMessageRequest() # Create an object of type EmptyRequest

move_turtlebot_in_square_request_object.side = 2.0
move_turtlebot_in_square_request_object.repetitions = 3

rospy.loginfo("Doing Service Call...")

result = move_turtlebot_in_square_service_client(move_turtlebot_in_square_request_object) # Send through the connection the path to the trajectory file to be executed
rospy.loginfo(str(result)) # Print the result given by the service called

rospy.loginfo("END of Service call...")