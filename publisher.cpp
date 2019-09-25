#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	
	system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.0");	
	system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.0");
	
	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.0");
	
	system("rostopic pub -1 /gripper_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.83");	
	system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.68");
	system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.53");
	
	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
	system("rostopic pub -1 /gripper_joint/command std_msgs/Float64 -- 0.9");






	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.3");
	system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.27");


	
	
	
	
	system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.2");
	system("rostopic pub -1 /gripper_joint/command std_msgs/Float64 -- 0.0");
	
	
}
