#! /usr/bin/python

#import for ros
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import cv2

camera_number = 0
cap = cv2.VideoCapture(camera_number) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

#instantiate bridge
bridge = CvBridge()

# Publisher Information
image_publisher = rospy.Publisher('image_raw', Image, queue_size=10)
rospy.init_node('camera_node', anonymous=True)
rate = rospy.Rate(1000) 

counter = 0
def camera_input(cap):
    # take first frame of the video
    ret,frame = cap.read()
    return ret, frame

while(camera_input(cap)[0] and not rospy.is_shutdown()):
        current_frame = camera_input(cap)[1]
        image_publisher.publish(bridge.cv2_to_imgmsg(current_frame, "bgr8"))
        counter += 1
        rospy.loginfo(counter)
 