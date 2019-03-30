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

    float z_axis_analog = (joy->axes[3] + 1)/2.0;
    int diagonal_mag = sqrt(pow(joy->axes[0], 2) + pow(joy->axes[1], 2));
    int diagonal_sign = ((joy->axes[1]<0)? -1:1);
/*
    if (joy -> buttons[8])
    PH_button = 1;

    if (joy -> buttons[9])
    TEMP_button = 1;

    if (joy -> buttons[10])
    MAG_button = 1;

    if (joy -> buttons[11])
    WATER_button = 1;*/

    if(joy->buttons[6] != 0)
	{
	motorA = 1600;
	}
	else
	motorA = 1500;
    
	if(joy->buttons[7] != 0)
	{
	motorB = 1600;
	}
	else
	motorB = 1500;
    
	if(joy->buttons[8] != 0)
	{
	motorC = 1600;
	}
	else
	motorC = 1500;

    if(joy->buttons[9] != 0)
	{
	motorD = 1600;
	}
	else
	motorD = 1500;

    if(joy->buttons[10] != 0)
	{
	motorE = 1600;
	}
	else
	motorE = 1500;
    
	if(joy->buttons[11] != 0)
	{
	motorF = 1600;
	}
	else
	motorF = 1500;


std::stringstream ss;



 char buffer[4] = "";
 sprintf(buffer, "%d", motorF);


 ss << "A" << motorA << "B" <<  motorB << "C" <<  motorC << "D" <<  motorD << "E" <<  motorE << "F" <<  buffer << "G" << PH_button << TEMP_button <<  MAG_button  <<  WATER_button << "K";
 msg.data = ss.str();
 rov_pub_.publish(msg);
 // ros::Duration(0.01).sleep();

}
int main(int argc, char** argv)
{
 ros::init(argc, argv, "map_motors_test");
 TeleopROV teleop_ROV;
 ros::spin();
}
