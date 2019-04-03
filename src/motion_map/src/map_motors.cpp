#include <ros/ros.h>
#include <sensor_msgs/Joy.h>
#include <std_msgs/String.h>
#include "std_msgs/Float64.h"
#include <std_msgs/Bool.h>
#include <stdio.h>
#include <string.h>
#include <cstring>
#include <sstream>
#include <stdlib.h>
#include <string>
//Calibration part:
const int speed = 200;
const int A_sign = -1;
const int B_sign = 1;
const int C_sign = -1;
const int D_sign = -1;
const int E_sign = 1;
const int F_sign = -1;
int Reverse = 1;

/*
G-K
0-> DC1-R
1-> DC1-L
2-> arm
3-> LED
*/


std_msgs::String msg;
std::string dir_var;
std::string line_enable = "stop";

int motorA = 1500, motorB = 1500, motorC = 1500, motorD= 1500, motorE= 1500, motorF= 1500, motor_def_A, motor_def_B, motor_def_C, motor_def_D, motor_def_E, motor_def_F;
float yaw_control_effort, pitch_control_effort, depth_control_effort;
bool PH_button = false, TEMP_button = false, arm_button = false, t_shapes_button1 = false, t_shapes_button2 = false, micro_rov_key = false, led_button = false;


float   z_axis_analog;
int     diagonal_mag;
int     diagonal_sign;

#define motorA motor_def_D
#define motorB motor_def_A
#define motorC motor_def_E
#define motorD motor_def_B
#define motorE motor_def_C
#define motorF motor_def_F

class TeleopROV
{
public:
 TeleopROV();
 void publish();

private:
 void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);
 void yaw_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg);
 void pitch_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg);
 void depth_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg);
 void direction_Callback(const std_msgs::String::ConstPtr& dir);
 void LineFollowerEnable_Callback(const std_msgs::String::ConstPtr& msg);

 ros::NodeHandle nh_;
 ros::Publisher rov_pub_;
 ros::Subscriber joy_sub_;
 ros::Subscriber yaw_control_effort_sub;
 ros::Subscriber pitch_control_effort_sub;
 ros::Subscriber depth_control_effort_sub;
 ros::Subscriber LineFollwerEnable_sub;
 ros::Subscriber dir_sub;
};



TeleopROV::TeleopROV()
{
 /*nh_.param("axis_linear", linear_, linear_);
 nh_.param("axis_angular", angular_, angular_);
 nh_.param("scale_angular", a_scale_, a_scale_);  
 nh_.param("scale_linear", l_scale_, l_scale_);*/


 rov_pub_ = nh_.advertise<std_msgs::String>("motor_values", 1000);
 
 joy_sub_ = nh_.subscribe<sensor_msgs::Joy>("joy", 1000, &TeleopROV::joyCallback, this);
 yaw_control_effort_sub = nh_.subscribe<std_msgs::Float64>("yaw_control_effort", 1000, &TeleopROV::yaw_control_effort_Callback, this);
 pitch_control_effort_sub = nh_.subscribe<std_msgs::Float64>("pitch_control_effort", 1000, &TeleopROV::pitch_control_effort_Callback, this);
 depth_control_effort_sub = nh_.subscribe<std_msgs::Float64>("depth_control_effort", 1000, &TeleopROV::depth_control_effort_Callback, this);

 dir_sub = nh_.subscribe<std_msgs::String>("direction", 1000, &TeleopROV::direction_Callback, this);
 LineFollwerEnable_sub = nh_.subscribe<std_msgs::String>("line_follower_flag", 1000, &TeleopROV::LineFollowerEnable_Callback, this);

}

void Up(const sensor_msgs::Joy::ConstPtr& joy);
void Down(const sensor_msgs::Joy::ConstPtr& joy);
void YAxis(const sensor_msgs::Joy::ConstPtr& joy);
void Tilt(const sensor_msgs::Joy::ConstPtr& joy);
void Yaw(const sensor_msgs::Joy::ConstPtr& joy);
void DiagonalRight(const sensor_msgs::Joy::ConstPtr& joy);
void DiagonalLeft(const sensor_msgs::Joy::ConstPtr& joy);
void LeftOrRight(const sensor_msgs::Joy::ConstPtr& joy);
void Buttons(const sensor_msgs::Joy::ConstPtr& joy);

//Autonomous motion functions.
void Right();
void Left();
void Down_autonomous();
void Up_autonomous();

void TeleopROV::direction_Callback(const std_msgs::String::ConstPtr& dir)
{
    
    dir_var = dir->data;
    ROS_INFO_STREAM("Line follower direction callback \n");
    
            if (dir_var == "right")
            {
                ROS_INFO_STREAM("line_follower right");
                Right();
            }
            else if (dir_var == "left")
            {
                ROS_INFO_STREAM("line_follower left");
                Left();
            }
            else if (dir_var == "up")
            {
                ROS_INFO_STREAM("line_follower up");
                Up_autonomous();
            }
            else if (dir_var == "down")
            {
                ROS_INFO_STREAM("line_follower down");
                Down_autonomous();
            }
            else
            {
                motorA = 1500;
                motorB = 1500;
                motorC = 1500;
                motorD = 1500;
                motorE = 1500;
                motorF = 1500;
            }
            ROS_INFO_STREAM("Autonomous mode ON!!");
            
    
    std::stringstream ss;
    char buffer[4] = "";
    sprintf(buffer, "%d", motorF);

    ss << "A" << motor_def_A << "B" <<  motor_def_B << "C" <<  motor_def_C << "D" <<  motor_def_D << "E" <<  motor_def_E << "F" <<  buffer << "G" << PH_button << arm_button << t_shapes_button1<< t_shapes_button2<< "K";
    msg.data = ss.str();
    rov_pub_.publish(msg);
}

void TeleopROV::LineFollowerEnable_Callback(const std_msgs::String::ConstPtr& msg)
{
     line_enable = msg->data; 
}

void TeleopROV::publish()
{
    std::stringstream ss;
    char buffer[4] = "";
    sprintf(buffer, "%d", motorF);

    ss << "A" << motor_def_A << "B" <<  motor_def_B << "C" <<  motor_def_C << "D" <<  motor_def_D << "E" <<  motor_def_E << "F" <<  buffer << "G" << PH_button << arm_button << t_shapes_button1<< t_shapes_button2<< "K";
    msg.data = ss.str();
    rov_pub_.publish(msg);
 
}

void TeleopROV::yaw_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg)
{
  yaw_control_effort = msg->data;
}

void TeleopROV::pitch_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg)
{
  pitch_control_effort = msg->data;
}

void TeleopROV::depth_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg)
{
  depth_control_effort = msg->data;
}

void TeleopROV::joyCallback(const sensor_msgs::Joy::ConstPtr& joy)
{
    /*
    Tilting? axes[5]
    Up? buttons[4]
    Down? buttons[2]
    Foward and backward? axes[1]
    Right and left? axes[0]
    Z-rotation? axes[2]
    */
    z_axis_analog = (joy->axes[3] + 1)/2.0;
    diagonal_mag = sqrt(pow(joy->axes[0], 2) + pow(joy->axes[1], 2));
    diagonal_sign = ((joy->axes[1]<0)? -1:1);
    Buttons(joy);
if (line_enable == "stop") // if line follwer is not enabled
{
    if (joy -> buttons[5]) //reverse motion
        Reverse = -1;
    else
        Reverse = 1;

    //joy normal motion 
    if(joy->axes[5] != 0)     //Tilting
        Tilt(joy);  
    else if(joy->buttons[4]) //Z-Axis UP
        Up(joy); 
    else if(joy->buttons[2]) //Z-axis DOWN
        Down(joy);
    else
    {
        motorE = 1500;
        motorF = 1500;
    }
    if(joy->axes [2] != 0  && (joy->axes [2] > 0.2 || joy->axes [2] < -0.4))     //Z-Axis Rotation is required in joystick, give motors D and E reverse values
        Yaw(joy);
    else if(joy->axes[1] != 0 && joy->axes[0] != 0 ) //X and Y--> Diagonal
    {
        if((joy->axes[1] < 0 && joy->axes[0] < 0) && (joy->axes[1] > 0 && joy->axes[0] > 0))
            DiagonalRight(joy);
        else
            DiagonalLeft(joy);    
    }
    else if(joy->axes[1] != 0)        //Move forward/backward
        YAxis(joy);
    else if(joy->axes[0] != 0)         // Move left/right
        LeftOrRight(joy);
    else
    {
        motorA = 1500;
        motorB = 1500;
        motorC = 1500;
        motorD = 1500;
    }
    
}

    if (yaw_control_effort == 0 && pitch_control_effort == 0 && depth_control_effort == 0 && line_enable == "stop")
        {
            ROS_INFO_STREAM("Joy is changing.");
            std::stringstream ss;
            char buffer[4] = "";
            sprintf(buffer, "%d", motorF);

            ss << "A" << motor_def_A << "B" <<  motor_def_B << "C" <<  motor_def_C << "D" <<  motor_def_D << "E" <<  motor_def_E << "F" <<  buffer << "G" << PH_button << arm_button << t_shapes_button1<< t_shapes_button2<< "K";
            msg.data = ss.str();
            rov_pub_.publish(msg);   
        }


}



int main(int argc, char** argv)
{
    ros::init(argc, argv, "map_motors");    
    TeleopROV teleop_ROV;
    ros::Rate loop_rate(10);
    ROS_INFO_STREAM("Balease");
    while (ros::ok())
    {
        if (yaw_control_effort != 0 || pitch_control_effort != 0 || depth_control_effort != 0)
        {
        ROS_INFO_STREAM("PID while loop " << yaw_control_effort);
        motorA -= int (yaw_control_effort);
        motorB += int (yaw_control_effort);
        motorC -= int (yaw_control_effort);
        motorD -= int (yaw_control_effort);
        motorE = motorE + int (depth_control_effort) + int (pitch_control_effort);
        motorF = motorF + int (depth_control_effort) + int (pitch_control_effort);

        teleop_ROV.publish();
        
        motorA += int (yaw_control_effort);
        motorB -= int (yaw_control_effort);
        motorC += int (yaw_control_effort);
        motorD += int (yaw_control_effort);
        motorE = motorE - int (depth_control_effort) - int (pitch_control_effort);
        motorF = motorF - int (depth_control_effort) - int (pitch_control_effort);
        }
        

        yaw_control_effort = 0;
        pitch_control_effort = 0;
        depth_control_effort = 0;
        
        ros::spinOnce();
        loop_rate.sleep();
    } 


  return 0;
}

void Up(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorE = 1500 + Reverse*(E_sign)*(300 *z_axis_analog);
    motorF = 1500 + Reverse*(F_sign)*(300 *z_axis_analog);
}
void Up_autonomous()
{
    motorE = 1500 + speed;
    motorF = 1500 + speed;
}
void Down(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorE = 1500 - Reverse*(speed*z_axis_analog);
	motorF = 1500 - Reverse*(speed*z_axis_analog);
}
void Down_autonomous()
{
    motorE = 1500 - speed;
	motorF = 1500 - speed;
}
void YAxis(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorB = 1500 + Reverse*(speed*joy -> axes[1]);
	motorA = 1500 + Reverse*(speed*joy -> axes[1]);
	motorC = 1500 + Reverse*(speed*joy -> axes[1]);
	motorD = 1500 + Reverse*(speed*joy -> axes[1]);
}
void Tilt(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorE = 1500 - Reverse*(E_sign)*(speed*joy -> axes[5]);
    motorF = 1500 + Reverse*(F_sign)*(speed*joy -> axes[5]);
}
void Yaw(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorB = 1500 + Reverse*(speed*joy -> axes[2]);
	motorA = 1500 - Reverse*(speed*joy -> axes[2]);
	motorC = 1500 - Reverse*(speed*joy -> axes[2]);
	motorD = 1500 + Reverse*(speed*joy -> axes[2]);
}
void DiagonalRight(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorB = 1500 + Reverse*diagonal_mag*diagonal_sign;
    motorA = 1500;
    motorC = 1500 + Reverse*diagonal_mag*diagonal_sign;
    motorD = 1500;
}
void DiagonalLeft(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorA = 1500 + Reverse*diagonal_mag*diagonal_sign;
    motorB = 1500;
    motorD = 1500 + Reverse*diagonal_mag*diagonal_sign;
    motorC = 1500;
}
void LeftOrRight(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorA = 1500 - Reverse*(speed*joy -> axes[0]);
	motorB = 1500 + Reverse*(speed*joy -> axes[0]);
	motorC = 1500 + Reverse*(speed*joy -> axes[0]);
	motorD = 1500 - Reverse*(speed*joy -> axes[0]);
}
void Buttons(const sensor_msgs::Joy::ConstPtr& joy)
{
    if (joy -> buttons[9])
    PH_button = 1;
    else
    PH_button = 0;
     
    if (joy -> buttons[8])
    arm_button = 1;
    else
    arm_button = 0;

    if (joy -> buttons[7])
    t_shapes_button1 = 1;
    else
    t_shapes_button1 = 0;
  

    if (joy -> buttons[6])
    t_shapes_button2 = true;
    else
    t_shapes_button2 = false;
}
void Right()
{
    motorA = 1500 - speed;
	motorB = 1500 + speed;
	motorC = 1500 + speed;
	motorD = 1500 - speed;
}
void Left()
{
    motorA = 1500 + speed;
	motorB = 1500 - speed;
	motorC = 1500 - speed;
	motorD = 1500 + speed;
}
