#! /usr/bin/env python

import rospy
import actionlib
import ros_python_examples.msg

class FibonacciAction(object):
    # create messages that are used to publish feedback/result
    _feedback = ros_python_examples.msg.FibonacciFeedback()  # protected variable
    _result = ros_python_examples.msg.FibonacciResult()

    def __init__(self, name):
        self._action_name = name
        self._action_server = actionlib.SimpleActionServer(self._action_name, ros_python_examples.msg.FibonacciAction, execute_cb=self.execute_callback, auto_start = False)
        # SimpleActionServer(action_name, action_type, execute_callback, auto_start),
        # Mote you should always set auto_start to False explicitly, unless you know what you're doing.
        self._action_server.start()
      
    def execute_callback(self, goal):
        # helper variables
        r = rospy.Rate(1) # 1hz
        success = True
        
        # set feedback to a list and append the seeds for the fibonacci sequence
        self._feedback.sequence = []
        self._feedback.sequence.append(0)
        self._feedback.sequence.append(1)
        
        # publish info to the console for the user
        rospy.loginfo('%s: Executing, creating fibonacci sequence of order %i with seeds %i, %i' 
                       % (self._action_name, goal.order, self._feedback.sequence[0], self._feedback.sequence[1]))
        
        # start executing the action
        for i in range(1, goal.order):
            # check that preempt has not been requested by the client
            if self._action_server.is_preempt_requested():
                rospy.loginfo('%s: Preempted' % self._action_name)
                self._action_server.set_preempted()
                success = False
                break
            self._feedback.sequence.append(self._feedback.sequence[i] + self._feedback.sequence[i-1])
            # publish the feedback
            self._action_server.publish_feedback(self._feedback)
            # this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes
            r.sleep()
          
        if success:
            self._result.sequence = self._feedback.sequence
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._action_server.set_succeeded(self._result)
        
if __name__ == '__main__':
    rospy.init_node('fibonacci')
    server = FibonacciAction(rospy.get_name())
    rospy.spin()