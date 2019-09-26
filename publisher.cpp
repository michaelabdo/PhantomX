//#include <ros/ros.h>
//#include <geometry_msgs/Twist.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void initialState();
void platform(int plat);
void level(int lev);
void vectorFill(vector<int> &vect);

int main(int argc, char **argv)
{
	vector<int> vect;
	vectorFill(vect);


	//platform(4); //platform int from positions);
	//level(3); //level int from positions)

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
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- -0.72");
	else if (plat == 2)
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- -0.28");
	else if (plat == 3)
		system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.3");
	else if (plat == 4)
		system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.72");
}

void level (int lev)
{
	if (lev == 1)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.30");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.85");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.10");
	}
	if (lev == 2)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.22");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.60");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.64");
	}
	else if (lev == 3)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.00");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.60");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
	}
	else if (lev == 4)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.90");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.60");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
	}
	else if (lev == 5)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.76");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.60");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
	}
	else if (lev == 6)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.64");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.60");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.79");
	}
}

void vectorFill(std::vector<int> &vect)
{
	ifstream file("final_sol.txt");
	int size = 574 - 72;                      //Ending point minus the starting point

	string fileCon;                           //String for file content

	if(file.is_open())                        //Store specific sections of file in fileCon
	{
			file.seekg(80);
			fileCon.resize(size);
			file.read(&fileCon[0], size);
	}

	for (std::string::size_type i = 0; i < fileCon.size(); i++)
		if (isdigit(fileCon[i]))
			 vect.push_back(fileCon[i] - '0');       //Convert char to int

	for (std::vector<int>::iterator it = vect.begin(); it != vect.end(); ++it)
		 std::cout << *it << std::endl;
}
