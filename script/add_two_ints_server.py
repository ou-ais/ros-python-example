#!/usr/bin/env python

from ros_python_examples.srv import AddTwoInts, AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
    print('Returning [%s + %s = %s]' % (req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')  # Init one ros node
    rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    # Define a service: (service_name, service_type, callback)
    print('Ready to add two ints.')
    rospy.spin()

if __name__ == '__main__':
    add_two_ints_server()