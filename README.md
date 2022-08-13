# Aerial Surveying in IIT Indore
Welcome to the drone simulation by IITI</br>
(Project made under IITI SoC 2022)</br>
## Contributors:</br>
Jha Rohan</br>
Abhishek Nair</br>
Ebrahim Rampurawala</br>
Niranjana Nair</br>
## Mentors:</br>
Bhavya Dalal</br>
Raghuvamsi Bokka</br>

The repository can be used for a complete drone simulation for aerial simulation. It contains the model of a drone with down facing camera in a gazebo world (a lake).</br>

To run this repositiory please clone the repository to your local machine:</br>
git clone https://github.com/rohanjha04/IITI_SoC_2022_AUTO_2_AerialSurveyingWithDrone</br>
Use git submodule --init --recursive in case of empty folders.</br>

### Dependencies:</br>
i. This is made for ROS Noetic and Ubuntu 20.04.</br>
ii. ArduCopter 4.0.4</br>
iii. MAVROS and MAVLink</br>
iv. Gazebo 11</br>
v. Python3</br>

To run the simulation please run the following commands in the terminal with all the dependencies satisfied:</br>
(Run these codes in your catkin workspace)</br>
i. catkin build</br>
ii. source devel/setup.bash</br>
iii. roslaunch iq_sim lake_travis.launch</br>
In new terminal</br>
iv. cd iq_sim/scripts/</br>
v. ./startsitl.sh</br>
In new terminal</br>
vi. source devel/setup.bash</br>
vii. roslaunch iq_sim apm.launch</br>
In new terminal</br>
viii. rosrun iq_gnc square.py</br>
In new terminal</br> 
ix. rqt_image_view</br>
Set mode GUIDED in the mavlink terminal to start the simulation</br>

To run the colab files, upload the pictures being send by the drone on google colab or use the loacl machines for image processing.</br>
Link to view a simulation: https://drive.google.com/drive/folders/1X5MsPP1fwMIs43cv_ZnfPmSOb4EU5XYY?usp=sharing
