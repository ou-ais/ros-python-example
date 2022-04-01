import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats # float32[] data
import numpy

def talker():
    pub = rospy.Publisher('floats', numpy_msg(Floats),queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        Array = numpy.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=numpy.float32)
        pub.publish(Array)
        r.sleep()

if __name__ == '__main__':
    talker()