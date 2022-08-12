#! /usr/bin/env python
# Import ROS.
import rospy
# Import the API.
from iq_gnc.py_gnc_functions import *
# To print colours (optional).
from iq_gnc.PrintColours import *
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

bridge = CvBridge()
x=0
sub = None

def image_callback(msg):
    print("Received an image!")
    try:
        # Convert ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        global sub
    except CvBridgeError as e:
        print(e)
    else:
        # Save OpenCV2 image as a jpeg
        global x 
        cv2.imwrite('camera_image'+str(x)+'.jpeg', cv2_img)
        sub.unregister()

    


def main():
    # Initializing ROS node.
    rospy.init_node("drone_controller", anonymous=True)
    # Create an object for the API.
    drone = gnc_api()
    # Wait for FCU connection.
    drone.wait4connect()
    # Wait for the mode to be switched.
    drone.wait4start()

    # Create local reference frame.
    drone.initialize_local_frame()
    # Request takeoff with an altitude of 50m.
    drone.takeoff(50)
    # Specify control loop rate.
    rate = rospy.Rate(3)

    # Waypoints
    goals = [[0, 0, 30, 0], [20, 0, 30, 0],[0,-40,30,0],[0,-40,30,30],[15,-40,30,120],[15,-50,30,-135],[-2,-50,30,-180],[-5,-40,30,-90],[0,0,30,0],[0,0,20,0],[0,0,10,0],[0,0,5,0],[0,0,2,0],[0,0,1,0],[0,0,0.5,0],[0,0,0,0],]
    i = 0

    while i < len(goals):
        drone.set_destination(
            x=goals[i][0], y=goals[i][1], z=goals[i][2], psi=goals[i][3])
        rate.sleep()
        if drone.check_waypoint_reached():
            i += 1
            global x
            x=x+1
            rospy.loginfo(CGREEN2 + "All waypoints reached landing now." + CEND)
            # Defining image topic
            image_topic = "/webcam/image_raw"
            # Set up your subscriber and define its callback
            global sub
            sub = rospy.Subscriber(image_topic, Image, image_callback)
            # Spin until ctrl + c
    rospy.spin()
    # Land after all waypoints is reached.
    drone.land()
    


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()