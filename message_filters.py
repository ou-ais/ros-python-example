import rospy
import message_filters
from sensor_msgs.msg import Image, CameraInfo

def callback(image, camera_info):
    rospy.loginfo('I heard image: % s \n, caminfo: %s \n', image, camera_info)
    # do some work ...

image_sub = message_filters.Subscriber('image', Image)
info_sub = message_filters.Subscriber('camera_info', CameraInfo)

ts = message_filters.TimeSynchronizer([image_sub, info_sub], queze_size=10)
'''
Alternatively, approximately synchronizes messages by their timestamps, you can use another function like this: 
ts = message_filters.ApproximateTimeSynchronizer([mode_sub, penalty_sub], queze_size=10, slop=0.1, allow_headerless=True)
where argument 'slop' defines the delay (in seconds) which message can be synchronized.
'''
ts.registerCallback(callback)
rospy.spin()