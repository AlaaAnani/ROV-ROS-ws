#include <ros/ros.h>
#include "motion_map/motors.h"
#include <sensor_msgs/Joy.h> 
#include <std_msgs/String.h>
 #include <stdio.h>
 #include <string.h> 
#include <cstring> 
 #include <sstream>
#include <stdlib.h>  
#include <string>


std_msgs::String msg;


class TeleopROV
{
public:
  TeleopROV();

private:
  void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);

  ros::NodeHandle nh_;
  ros::Publisher rov_pub_;
  ros::Subscriber joy_sub_;
};



TeleopROV::TeleopROV()
{
  /*nh_.param("axis_linear", linear_, linear_);
  nh_.param("axis_angular", angular_, angular_);
  nh_.param("scale_angular", a_scale_, a_scale_);
  nh_.param("scale_linear", l_scale_, l_scale_);*/


  rov_pub_ = nh_.advertise<std_msgs::String>("motor_values", 1000);
  joy_sub_ = nh_.subscribe<sensor_msgs::Joy>("joy", 1000, &TeleopROV::joyCallback, this);
}

char* intToStr(int value)
{
   int divisor = 1;
   int bufferLength = 1;
   int isNegative = 0;
   int bufferIndex = 0;

   // Handle the negative value case by remebering that the number is negative
   // and then setting it positive
   if(value < 0)
   {
       isNegative = 1;
       value *= -1;
       bufferIndex++; // move 1 place in the buffer so we don't overwrite the '-'
   }

   // Determine the length of the integer so we can allocate a string buffer
   while(value / divisor >= 10)
   {
       divisor *= 10;
       bufferLength++;
   }

   // Create the resulting char buffer that we'll return.
   // bufferLength + 1 because we need a terminating NULL character.
   // + isNegative because we need space for the negative sign, if necessary.
   char *result = new char[bufferLength + 1 + isNegative];

   // Set the first character to NULL or a negative sign
   result[0] = isNegative == false ? 0 : '-';

   while(bufferLength > 0)
   {
       // ASCII table has the number characters in sequence from 0-9 so use the
       // ASCII value of '0' as the base
       result[bufferIndex] = '0' + value / divisor;

       // This removes the most significant digit converting 1337 to 337 because
       // 1337 % 1000 = 337
       value = value % divisor;

       // Adjust the divisor to next lowest position
       divisor = divisor / 10;

       bufferIndex++;
       bufferLength--;
   }

   // NULL terminate the string
   result[bufferIndex] = 0;

   return result;
}


void TeleopROV::joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
  	motion_map::motors motor_values;
	/*
	Tilting? axes[5]
	Up? buttons[4]
	Down? buttons[2]
	Foward and backward? axes[1]
	Right and left? axes[0]
	Z-rotation? axes[2]
	*/
int motorA, motorB, motorC, motorD, motorE, motorF;
bool PH_button = false, TEMP_button = false, MAG_button = false, WATER_button = false;


	if (joy -> buttons[8])
	PH_button = 1;

	if (joy -> buttons[9])
	TEMP_button = 1;

	if (joy -> buttons[10])
	MAG_button = 1;

	if (joy -> buttons[11])
	WATER_button = 1;

  	if(joy->axes[5] != 0) 	//Tilting
  	{
	  motorA = 1500 + (300*joy -> axes[5]);
  	motorB = 1500 - 0.5*(300*joy -> axes[5]);
  	motorC = 1500 - 0.5*(300*joy -> axes[5]);
	}
 	else if(joy->buttons[4]) //Z-Axis UP
	{
	motor_values.motorA = 1500 + (300*joy -> buttons[4]);
  	motorB = 1500 + (300*joy -> buttons[4]);
  	motorC = 1500 + (300*joy -> buttons[4]);
	}
	else if(joy->buttons[2]) //Z-axis DOWN
	{
	motorA = 1500 - (300*joy -> buttons[2]);
  	motorB = 1500 - (300*joy -> buttons[2]);
  	motorC = 1500 - (300*joy -> buttons[2]);
	}
	else
	{
	  motorA = 1500;
  	motorB = 1500;
  	motorC = 1500;
	}


	if(joy->axes [2] != 0) 	//Z-Axis Rotation is required in joystick, give motors D and E reverse values
	{
	motorD = 1500 + (300*joy -> axes[2]);
  	motorE = 1500 - (300*joy -> axes[2]);
	}
	else 			//Move forward/backward
	{
		motorD = 1500 + (300*joy -> axes[1]);
	  	motorE = 1500 + (300*joy -> axes[1]);
	}
	
	//Right/Left
	  motorF = 1500 + (300*joy -> axes[0]);


/*itoa(motor_values.motorA, mA, 10);
itoa(motor_values.motorB, mB, 10);
itoa(motor_values.motorC, mC, 10);
itoa(motor_values.motorD, mD, 10);
itoa(motor_values.motorE, mE, 10);
itoa(motor_values.motorF, mF, 10);
itoa(motor_values.motorA, ph_str, 10);
itoa(motor_values.motorA, temp_str, 10);
itoa(motor_values.motorA, water_str, 10);
itoa(motor_values.motorA, mag_str, 10);
std::string to_publish = 'A' + mA + 'B';*/


std::stringstream ss;
std::stringstream ss2;

// ss << motor_values.motorA << motor_values.motorB << motor_values.motorC << motor_values.motorD << motor_values.motorE << motor_values.motorF << motor_values.PH_button << motor_values.TEMP_button << motor_values.WATER_button << motor_values.MAG_button<<"K";
 //ss << "ssssssssssssssssssssssssssssssssssssssssssssssssMK";
// msg.data = ss.str();
  char buffer[4] = "";
  sprintf(buffer, "%d", motorF);


  ss << "A" << motorA << "B" <<  motorB << "C" <<  motorC << "D" <<  motorD << "E" <<  motorE << "F" <<  buffer << "G" << PH_button << TEMP_button <<  MAG_button  <<  WATER_button << "K";
  msg.data = ss.str();
  rov_pub_.publish(msg);
  // ros::Duration(0.01).sleep();

}


int main(int argc, char** argv)
{
  ros::init(argc, argv, "teleop_ROV");
  TeleopROV teleop_ROV;
  ros::spin();
}
