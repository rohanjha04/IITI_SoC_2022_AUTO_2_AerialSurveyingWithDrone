# Aerial Surveying in IIT Indore
Welcome to the drone simulation by IITI
(Project made under IITI SoC 2022)
Contributors:
Jha Rohan
Abhishek Nair
Ebrahim Rampurawala
Niranjana Nair
Mentors:
Bhavya Dalal
Raghuvamsi Bokka

The repository can be used for a complete drone simulation for aerial simulation. It contains the model of a drone with down facing camera in a gazebo world (a lake).

To run this repositiory please clone the repository to your local machine:
LINK

Dependencies:
i. This is made for ROS Noetic and Ubuntu 20.04.
ii. ArduCopter 4.0.4
iii. MAVROS and MAVLink
iv. Gazebo 11
v. Python3

To run the simulation please run the following commands in the terminal with all the dependencies satisfied:
(Run these codes in your catkin workspace)
i. catkin build
ii. source devel/setup.bash
iii. roslaunch iq_sim lake_travis.launch
In new terminal
iv. cd iq_sim/scripts/
v. ./startsitl.sh
In new terminal
vi. source devel/setup.bash
vii. roslaunch iq_sim apm.launch
In new terminal
viii. rosrun iq_gnc square.py
In new terminal 
ix. rqt_image_view

To run the colab files, upload the pictures being send by the drone on google colab or use the loacl machines for image processing.
