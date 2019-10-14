//#include <ros/ros.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct positions
{
	int time;
	int origLevel;
	int origPlat;
	int newLevel;
	int newPlat;

	positions(int t = 0, int oL = 0, int oP = 0,
						int nL = 0 , int nP = 0) : time(t),
						origLevel(oL),origPlat(oP), newLevel(nL),
						newPlat(nP) {}
};

struct less_than_key
{
    inline bool operator() (const positions& struct1, const positions& struct2)
    {
        return (struct1.time < struct2.time);
    }
};

void initialState();
void platform(int plat);
void level(int lev);
void vectorFill(vector<positions> &vect);
void gripper(bool);

int main(int argc, char **argv)
{
	vector<positions> vect;
	vectorFill(vect);

	gripper(false);
	for (std::vector<positions>::iterator it = vect.begin(); it != vect.end(); ++it)
	{																															//Prints out contents of the struct
		 platform((*it).origPlat);
		 level((*it).origLevel);
		 gripper(true);
		 platform((*it).newPlat);
		 level((*it).newLevel);
		 gripper(false);
	 }

	 initialState();
}

void initialState()
{
	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- -1.2");
	system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.0");
}

void platform(int plat)
{
	initialState();

	if (plat == 1)
		system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- -0.72");
	else if (plat == 2)
		system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- -0.29");
	else if (plat == 3)
		system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.3");
	else if (plat == 4)
		system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.72");
}

void level (int lev)
{
	if (lev == 1)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.64");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- -1.05");
 	 	system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 1.03");
	}
	else if (lev == 2)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.29");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- -0.95");
    system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 1.31");
	}
	else if (lev == 3)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.02");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- -0.83");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 1.45");
	}
	else if (lev == 4)
	{

		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.80");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- -0.72");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 1.50");
	}
	else if (lev == 5)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.63");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- -0.70");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 1.55");
	}
	else if (lev == 6)
	{
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- -0.45");
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.50");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 1.40");
	}

}

void gripper(bool value)
{
	if (value)
		system("rostopic pub -1 /gripper_joint/command std_msgs/Float64 -- 1.0");		//close
	else
		system("rostopic pub -1 /gripper_joint/command std_msgs/Float64 -- 0.0");		//open
}

void vectorFill(std::vector<positions> &vect)
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

	int count = 0;
	positions pos;														//Struct object

	for (std::string::size_type i = 0; i < fileCon.size(); i++)
	{
		if (isdigit(fileCon[i]))
		{
			count++;
			if (count == 1)
			{
					pos.time = fileCon[i] - '0';  //Convert char to int
					i++;
					if (isdigit(fileCon[i]))
						pos.time = (pos.time*10) + fileCon[i] - '0';			//If there is a second
			}																												//digit, append it
			else if (count == 2)
				pos.origLevel = fileCon[i] - '0';
			else if (count == 3)
				pos.origPlat = fileCon[i] - '0';
			else if (count == 4)
				pos.newLevel = fileCon[i] - '0';
			else if (count == 5)
			{
				pos.newPlat = fileCon[i] - '0';
				vect.push_back(pos);																		//Push struct to vect
				count = 0;
			}
			else
			{
				std::cout << "ERROR - Count is not in range - line 153" << std::endl;
				exit(1);
			}
		}
	}

	std::sort(vect.begin(), vect.end(), less_than_key());				//Sorts the vector in
																															//regards to time movement
	for (std::vector<positions>::iterator it = vect.begin(); it != vect.end(); ++it)
	{																															//Prints out contents of the struct
		 std::cout << (*it).time << ", ";
		 std::cout << (*it).origLevel << ", ";
	 	 std::cout << (*it).origPlat << ", ";
		 std::cout << (*it).newLevel << ", ";
		 std::cout << (*it).newPlat << std::endl;
	 }

}
