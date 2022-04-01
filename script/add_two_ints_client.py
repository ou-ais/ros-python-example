#!/usr/bin/env python

import sys
import rospy
from ros_python_examples.srv import AddTwoInts

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    # block until the service named 'add_two_ints' is available.
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        # Declare service: ('service_name', service_type)
        response = add_two_ints(x, y)  # call the service
        return response.sum
    except rospy.ServiceException as e:
        print('Service call failed: %s' % e)

def usage():
    return '%s [x y]' % sys.argv[0]

if __name__ == '__main__':
    # No need to call 'init_node' in a client.
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print('Requesting %s + %s' % (x, y))
    print('%s + %s = %s' % (x, y, add_two_ints_client(x, y)))