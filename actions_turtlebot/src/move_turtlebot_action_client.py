#! /usr/bin/env python
import rospy
import time
import actionlib
from actions_turtlebot.msg import ActionMsgAction, ActionMsgGoal, ActionMsgResult, ActionMsgFeedback

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
def feedback_callback(feedback):
    print(feedback) # from server
    print("feedback: Running ...client") #from clinet feedback run
    # print(feedback.feedback)

# initializes the action client node
rospy.init_node('move_turtlebot_action_client')

# create the connection to the action server
client = actionlib.SimpleActionClient('/move_turtlebot_as', ActionMsgAction)
# waits until the action server is up and running
client.wait_for_server()

# creates a goal to send to the action server
goal = ActionMsgGoal()
goal.goal = 2

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)
rate = rospy.Rate(1)
rospy.loginfo("Action /move_turtlebot_action_client Run")

client.wait_for_result()
print('[Result] State: %d'%(client.get_state()))

