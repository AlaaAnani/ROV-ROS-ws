#!/usr/bin/env python
## 1- Press 'a' to capture current frame from the video
## 2- Select with the mosue a rectangle which only contains the shapes (the smaller the rectangle the better)
## 3- Press 'a' to detect and count the shapes
## Done for now but may need calibration when we try it (easy)
#import imutils
import rospy
import math
import numpy as np
import cv2
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from GUI.msg import Num
#from beginner_tutorials.msg import Num
#from GUI.msg import Num

uvc_img = Image()
bridge = CvBridge()
pub = rospy.Publisher('species_No', Num, queue_size=10)

#variables
c,C,T,L,S,w,h=0,0,0,0,0,0,0

def talker():
    #rospy.init_node('shapes_no', anonymous=True)
    rate = rospy.Rate(10)
    msg = Num()
    msg.circlesNo = C
    msg.trianglesNo = T
    msg.linesNo = L
    msg.squaresNo = S
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

def color_seg(choice):
    if choice == 'black':
        lower_hue = np.array([0,0,0])
        upper_hue = np.array([1,255,255])
    return lower_hue, upper_hue

def detectShape(cnt):
    shape = 'unknown'
    peri = cv2.arcLength(c, True)
    vertices = cv2.approxPolyDP(c, 0.04 * peri, True)
    if len(vertices) == 2:
        shape = 'line'
    elif len(vertices) == 3:
        shape = 'triangle'
    elif len(vertices) == 4:
        if ((float(w)/h) > 0.9 and (float(w)/h) < 1.1):
            shape = "square"
        else:
            shape = "line"
    else:
        shape = "circle"
    return shape

def set_window():
    window = cv2.namedWindow("Image_processing", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image_processing", 1920,1080)
    cv2.moveWindow("Image_processing",100,100)

def main():
    global c, C, T, L, S, w, h 
    set_window()
    INITIATE_flag = 0
    flag = 1
    while(flag and not rospy.is_shutdown()):
        try:
            # Convert your ROS Image message to OpenCV2
            current_frame = bridge.imgmsg_to_cv2(uvc_img, "bgr8")
        except CvBridgeError, e:
            print(e)
        else:
            current_frame = cv2.flip(current_frame, 1)
            cv2.imshow('Image_processing',current_frame)
            k = cv2.waitKey(1) & 0xff
            if k == 27:
                flag = 0
                rospy.signal_shutdown('process done')
            chosen_color = 'black'
            hsv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
            lower_hue, upper_hue = color_seg(chosen_color)
            mask = cv2.inRange(hsv, lower_hue, upper_hue)                
            if cv2.waitKey(33) == ord('a'):
                cv2.imwrite("imageRetrieved.jpg", current_frame)
                im = cv2.imread("imageRetrieved.jpg")
                r = cv2.selectROI(im,False)
                imCrop = im[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
                cv2.imshow("IMAGE",imCrop)
                cv2.waitKey(0)

                gray = cv2.cvtColor(imCrop,cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(gray,50,150)
                _, contours, _ = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                L,T,S,C=0,0,0,0
                for c in contours:
                    M = cv2.moments(c)
                    if M['m00'] == 0:
                        shape = 'line'
                        cX, cY = 0, 0
                    else:
                        cX = int(M['m10'] / M['m00'])
                        cY = int(M['m01'] / M['m00'])
                    p = cv2.arcLength(c,True)
                    v = cv2.approxPolyDP(c,0.04*p,True)
                    (x,y),(w,h),theta = cv2.minAreaRect(v)
                    if w >= h:
                        if w > 20 and w < 150:
                            shape = detectShape(c)
                            if shape == 'line':
                                L += 1
                            elif shape == 'triangle':
                                T += 1
                            elif shape == 'square':
                                S += 1
                            elif shape == 'circle':
                                C += 1
                    else:
                        if h > 20 and h < 150:
                            shape = detectShape(c)
                            if shape == 'line':
                                L += 1
                            elif shape == 'triangle':
                                T += 1
                            elif shape == 'square':
                                S += 1
                            elif shape == 'circle':
                                C += 1
                    cv2.drawContours(imCrop,[c],-1,(0, 255, 0),2)
                    cv2.putText(imCrop, shape,(cX,cY),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255), 2)
                    cv2.imshow("Not final yet", imCrop)
                print('Number of lines is ', L)
                print('Number of triangles is ', T)
                print('Number of squares is ', S)
                print('Number of circles is ', C)
                try:
                    talker()
                except rospy.ROSInterruptException:
                    pass

    cv2.destroyAllWindows()



def image_callback(msg):
    global uvc_img
    uvc_img = msg
   
def gui_flag_callback(msg):
    if(str(msg.data) == 'start'):
       main()

def listener():
     rospy.init_node('shapes_detection', anonymous=True)
     rospy.Subscriber("species_flag", String, gui_flag_callback)
     rospy.Subscriber('camera/image_raw', Image, image_callback)
     rospy.spin()

listener()