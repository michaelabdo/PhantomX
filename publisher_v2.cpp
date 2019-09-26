#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>

void initialState();
void platform(int plat);


int main(int argc, char **argv)
{
	ofstream myfile;
	myfile.open ("initial_config.txt");
	initialState();

	while (!myfile.eof())
	{

	}
	//level 1


	platform(4 //platform int from positions);
	level(6 //level int from positions)




}

void initialState()
{
	system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /gripper_joint/command std_msgs/Float64 -- 0.0");
}

void platform(int plat)
{
	initialState();
	if (plat == 1)
		//system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.0");
	if (plat == 2)
		//system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.0");
	if (plat == 3)
		system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.27");
	if (plat == 4)
		system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.68");
}

void level (int lev)
{
	if (lev == 1)
	{
		/*
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.83");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.3");
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.2");
		*/
	}
	if (lev == 2)
	{
		/*
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.83");
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.53");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
		*/
	}
	if (lev == 3)
	{
		/*
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.83");
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.53");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
		*/
	}
	if (lev == 4)
	{
		/*
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.83");
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.53");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
		*/
	}
	if (lev == 5)
	{
		/*system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.83");
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.53");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
		*/
	}
	if (lev == 6)
	{
		/*
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.83");
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.53");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
		*/
	}

}
