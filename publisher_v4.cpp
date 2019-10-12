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
void platform(int plat, int level);
void level(int lev);
void vectorFill(vector<positions> &vect);
void gripper(bool);

int main(int argc, char **argv)
{
	vector<positions> vect;
	vectorFill(vect);


	gripper(true);
	platform(3, 1);
	level(1);
	gripper(false);
	platform(2, 3);
	level(3);
	gripper(true);
	initialState();


/*
	gripper(true);
	system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- -0.28");
	system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.64");
	system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.60");
	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.77");

	gripper(false);
	initialState();

  system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- -0.28");
	system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.64");
	system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.60");
	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.77");

	gripper(true);
	initialState();
	*/
	/*
	gripper(true);
	int temp = 5;
 	for (int i = 6; i > 0; i--)
 	{
		 platform(1, i);
		 level(i);
		 gripper(false);
		 platform(2, i);
		 level(6-temp);
		 temp--;
		 gripper(true);
	}
	*/

	/*
	for (std::vector<positions>::iterator it = vect.begin(); it != vect.end(); ++it)
	{																															//Prints out contents of the struct
		 platform((*it).origPlat);
		 level((*it).origLevel);
		 gripper(false);
		 platform((*it).newPlat);
		 level((*it).newLevel);
		 gripper(true);
	 }
	 */

	 //initialState();
}

void initialState()
{
	system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.0");
	system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- 0.0");
}

void platform(int plat, int level)
{
	initialState();

	if (plat == 1)
	{
		system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- -0.72");
		if (level < 4)
			system("rostopic pub -1 /arm_shoulder_pan_joint/command std_msgs/Float64 -- -0.73");
	}
		//0.73 for level 4 and 6
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
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.30");
 	 	system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.80");
 	 	system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.07");
	}
	else if (lev == 2)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.22");
    system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.58");
 	  system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.58");
	}
	else if (lev == 3)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 1.00");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.62");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.77");
	}
	else if (lev == 4)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.90");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.56");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.77");
	}
	else if (lev == 5)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.76");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.60");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.77");
	}
	else if (lev == 6)
	{
		system("rostopic pub -1 /arm_shoulder_lift_joint/command std_msgs/Float64 -- 0.64");
		system("rostopic pub -1 /arm_elbow_flex_joint/command std_msgs/Float64 -- 0.60");
		system("rostopic pub -1 /arm_wrist_flex_joint/command std_msgs/Float64 -- 0.77");
	}

}

void gripper(bool value)
{
	if (value)
		system("rostopic pub -1 /gripper_joint/command std_msgs/Float64 -- 0.0");		//open
	else
		system("rostopic pub -1 /gripper_joint/command std_msgs/Float64 -- 1.0");		//close
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
