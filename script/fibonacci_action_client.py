#! /usr/bin/env python

import rospy
import actionlib
import ros_python_examples.msg

# Called once when the goal completes
def done_callback(state, result):
    rospy.loginfo('Action server is done.\n State: [%s]\n Result, %s' 
               % (str(state), str(result)))

# Call once when the goal become active
def active_callback():
    rospy.loginfo('Action server is processing the goal.')

# Call every time feedback is received for the goal
def feedback_callback(feedback):
    length = len(feedback.sequence)
    rospy.loginfo('Got new feedback: %s' % str(feedback.sequence[-1]))
    if length == 10:
        print('Intermediate is finished.')
    # Do some feedback process
    # ...

def fibonacci_client():
    # Creates the SimpleActionClient, passing the type of the action (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('fibonacci', ros_python_examples.msg.FibonacciAction)

    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = ros_python_examples.msg.FibonacciGoal(order=20)

    # Sends the goal to the action server.
    client.send_goal(goal, done_cb=done_callback, active_cb=active_callback, feedback_cb=feedback_callback)
    
    # Waits for the server to finish performing the action.
    # client.wait_for_result()

    # Prints out the result of executing the action
    # return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
    try:
        rospy.init_node('fibonacci_client_py')
        # result = fibonacci_client()
        # print("Result:", ', '.join([str(n) for n in result.sequence]))
        fibonacci_client()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("program interrupted before completion")
