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
const int yaw_pitch_speed = 200;
const int y_speed = 200;
const int x_speed = 200;
int z_speed = 200;

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
std::string micro_str = "";

int motorA = 1500, motorB = 1500, motorC = 1500, motorD= 1500, motorE= 1500, motorF= 1500, motor_def_A, motor_def_B, motor_def_C, motor_def_D, motor_def_E, motor_def_F;
float yaw_control_effort, pitch_control_effort, depth_control_effort;
bool piston_button = false, TEMP_button = false, arm_button = false, t_shapes_button1 = false, t_shapes_button2 = false, micro_rov_key = false, led_button = false;

//Rising edges
int microROV_en = 0, prev_microROV_en = 0;
bool micro_activated = false;


int FrontOff = 1, BackOff = 1, prev_FrontOff = 0, prev_BackOff = 0, prev_Reverse = 0, prev_PID = 0;


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

private:
 void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);
 void yaw_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg);
 void pitch_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg);
 // void depth_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg);
 void direction_Callback(const std_msgs::String::ConstPtr& dir);
 void LineFollowerEnable_Callback(const std_msgs::String::ConstPtr& msg);
 void microCallback(const std_msgs::String::ConstPtr& msg);


 ros::NodeHandle nh_;
 ros::Publisher rov_pub_;
 ros::Subscriber joy_sub_;
 ros::Subscriber yaw_control_effort_sub;
 ros::Subscriber pitch_control_effort_sub;
 // ros::Subscriber depth_control_effort_sub;
 ros::Subscriber LineFollwerEnable_sub;
 ros::Subscriber dir_sub;
 ros::Subscriber micro_sub;
};



TeleopROV::TeleopROV()
{
 
 rov_pub_ = nh_.advertise<std_msgs::String>("motor_values", 1000);
 
 joy_sub_ = nh_.subscribe<sensor_msgs::Joy>("joy", 1000, &TeleopROV::joyCallback, this);
 yaw_control_effort_sub = nh_.subscribe<std_msgs::Float64>("yaw_control_effort", 1000, &TeleopROV::yaw_control_effort_Callback, this);
 pitch_control_effort_sub = nh_.subscribe<std_msgs::Float64>("pitch_control_effort", 1000, &TeleopROV::pitch_control_effort_Callback, this);
 // depth_control_effort_sub = nh_.subscribe<std_msgs::Float64>("depth_control_effort", 1000, &TeleopROV::depth_control_effort_Callback, this);

 dir_sub = nh_.subscribe<std_msgs::String>("direction", 1000, &TeleopROV::direction_Callback, this);
 LineFollwerEnable_sub = nh_.subscribe<std_msgs::String>("line_follower_flag", 1000, &TeleopROV::LineFollowerEnable_Callback, this);
 micro_sub = nh_.subscribe<std_msgs::String>("keyboard/micro", 1000, &TeleopROV::microCallback, this);
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
void concatenate_values ();

//Autonomous motion functions.
void Right();
void Left();
void Down_autonomous();
void Up_autonomous();


void TeleopROV::microCallback(const std_msgs::String::ConstPtr& msg_keyboard)
{
    micro_str= msg_keyboard->data;
    ROS_INFO_STREAM("Micro ROV msg from keyboard ^-^ = " << micro_str);

    concatenate_values();
    rov_pub_.publish(msg);    
}


void TeleopROV::direction_Callback(const std_msgs::String::ConstPtr& dir)
{
    
    dir_var = dir->data;
    ROS_INFO_STREAM("Line follower direction callback \n");
    if (line_enable == "start")
    {
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
            ROS_INFO_STREAM("line_follower stop");
            motorA = 1500;
            motorB = 1500;
            motorC = 1500;
            motorD = 1500;
            motorE = 1500;
            motorF = 1500;
        }
        ROS_INFO_STREAM("Autonomous mode ON!!");
        
    }
    concatenate_values ();
    rov_pub_.publish(msg);
}

void TeleopROV::LineFollowerEnable_Callback(const std_msgs::String::ConstPtr& msg)
{
     line_enable = msg->data; 
}

void TeleopROV::yaw_control_effort_Callback(const std_msgs::Float64::ConstPtr& yaw_ce_msg)
{
        ROS_INFO_STREAM("receiving yaw control effort");
        yaw_control_effort = yaw_ce_msg->data;
        motorA -= int (yaw_control_effort);
        motorB += int (yaw_control_effort);
        motorC -= int (yaw_control_effort);
        motorD += int (yaw_control_effort);
        motorE = motorE + int (pitch_control_effort);
        motorF = motorF + int (pitch_control_effort);

        concatenate_values();
        rov_pub_.publish(msg);        
        
        motorA += int (yaw_control_effort);
        motorB -= int (yaw_control_effort);
        motorC += int (yaw_control_effort);
        motorD -= int (yaw_control_effort);
        motorE = motorE - int (pitch_control_effort);
        motorF = motorF - int (pitch_control_effort);
}

void TeleopROV::pitch_control_effort_Callback(const std_msgs::Float64::ConstPtr& pitch_ce_msg)
{
        ROS_INFO_STREAM("receiving pitch control effort");
        pitch_control_effort = pitch_ce_msg->data;
        motorA -= int (yaw_control_effort);
        motorB += int (yaw_control_effort);
        motorC -= int (yaw_control_effort);
        motorD += int (yaw_control_effort);
        motorE = motorE + int (pitch_control_effort);
        motorF = motorF + int (pitch_control_effort);

        concatenate_values();
        rov_pub_.publish(msg);        
        
        motorA += int (yaw_control_effort);
        motorB -= int (yaw_control_effort);
        motorC += int (yaw_control_effort);
        motorD -= int (yaw_control_effort);
        motorE = motorE - int (pitch_control_effort);
        motorF = motorF - int (pitch_control_effort);
}
/*
void TeleopROV::depth_control_effort_Callback(const std_msgs::Float64::ConstPtr& msg)
{
  depth_control_effort = msg->data;
}
*/
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
    //joy normal motion 
    if(joy->axes[5] != 0)     //Tilting
        {
            Tilt(joy);  
            ROS_INFO_STREAM("normal pitch");
        }

    else if(joy->buttons[4]) //Z-Axis UP
        {
            Up(joy); 
            ROS_INFO_STREAM("normal up");
        }
    else if(joy->buttons[2]) //Z-axis DOWN
        {
            Down(joy); 
            ROS_INFO_STREAM("normal down");
        }
    else
    {
        motorE = 1500;
        motorF = 1500;
    }
    if(joy->axes [2] > 0.2 || joy->axes [2] < -0.4)     //Z-Axis Rotation is required in joystick, give motors D and E reverse values
        {
            Yaw(joy);
            ROS_INFO_STREAM("normal yaw");
        }

    else if(joy->axes[1] != 0)        //Move forward/backward
        {
            YAxis(joy);
            ROS_INFO_STREAM("normal forward and backward");
        }
    else if(joy->axes[0] != 0)         // Move left/right
        {
            LeftOrRight(joy);
            ROS_INFO_STREAM("normal left & right");
        }
    else
    {
        motorA = 1500;
        motorB = 1500;
        motorC = 1500;
        motorD = 1500;
    }
    
 
}


    if (yaw_control_effort == 0 && pitch_control_effort == 0 && line_enable == "stop")
    {         
        concatenate_values();  
        rov_pub_.publish(msg);
    }    

    // ROS_INFO_STREAM("joy is changing");
    prev_microROV_en = joy -> buttons[9];
    prev_FrontOff   = joy ->buttons[8];
    prev_BackOff    = joy-> buttons[10];
    prev_Reverse    = joy-> buttons[11];
    prev_PID = joy-> buttons[1];

}



int main(int argc, char** argv)
{
    ros::init(argc, argv, "map_motors");    
    ROS_INFO_STREAM("Executing main");
    TeleopROV teleop_ROV;
    ros::spin();
    return 0;
}

void Up(const sensor_msgs::Joy::ConstPtr& joy)
{
     motorE = 1500 + (E_sign)*(z_speed *z_axis_analog);
     motorF = 1500 + (F_sign)*(z_speed *z_axis_analog);
}
void Up_autonomous()
{
    motorE = 1500 + 200;
    motorF = 1500 + 200;
}
void Down(const sensor_msgs::Joy::ConstPtr& joy)
{
     motorE = 1500 - (E_sign)*(z_speed *z_axis_analog);
     motorF = 1500 - (F_sign)*(z_speed *z_axis_analog);
}
void Down_autonomous()
{
    motorE = 1500 - 200;
	motorF = 1500 - 200;
}
void YAxis(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorA = 1500 + FrontOff*Reverse*(y_speed*joy -> axes[1]);
    motorB = 1500 + FrontOff*Reverse*(y_speed*joy -> axes[1]);
	motorC = 1500 + BackOff*Reverse*(y_speed*joy -> axes[1]);
	motorD = 1500 + BackOff*Reverse*(y_speed*joy -> axes[1]);
}
void Tilt(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorE = 1500 - Reverse*(E_sign)*(yaw_pitch_speed*joy -> axes[5]);
    motorF = 1500 + Reverse*(F_sign)*(yaw_pitch_speed*joy -> axes[5]);
}
void Yaw(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorA = 1500 - FrontOff*Reverse*(yaw_pitch_speed*joy -> axes[2]);
    motorB = 1500 + FrontOff*Reverse*(yaw_pitch_speed*joy -> axes[2]);
	motorC = 1500 - BackOff*Reverse*(yaw_pitch_speed*joy -> axes[2]);
	motorD = 1500 + BackOff*Reverse*(yaw_pitch_speed*joy -> axes[2]);
}

void LeftOrRight(const sensor_msgs::Joy::ConstPtr& joy)
{
    motorA = 1500 - FrontOff*Reverse*(x_speed*joy -> axes[0]);
	motorB = 1500 + FrontOff*Reverse*(x_speed*joy -> axes[0]);
	motorC = 1500 + BackOff*Reverse*(x_speed*joy -> axes[0]);
	motorD = 1500 - BackOff*Reverse*(x_speed*joy -> axes[0]);
}
void Buttons(const sensor_msgs::Joy::ConstPtr& joy)
{
    if (joy -> buttons[5]) // led
    led_button = 1;
    else
    led_button = 0;
     
    if (joy -> buttons[3]) // piston
    piston_button = 1;
    else
    piston_button = 0;

    if (joy -> buttons[0]) // arm
    arm_button = 1;
    else
    arm_button = 0;

    if (!prev_PID && joy -> buttons[1]) //pid
    {
        if (yaw_control_effort != 0) yaw_control_effort = 0;
        if (pitch_control_effort != 0) pitch_control_effort = 0;
    }
  
        
    if(!prev_Reverse && joy -> buttons[11])
    {
        if (Reverse == 1) Reverse = -1;
        else if (Reverse == -1) Reverse = 1;
    }


    if((prev_microROV_en == 0) && (joy -> buttons[9]==1))
    {
        micro_activated = !micro_activated;
        if(micro_activated)
        ROS_INFO_STREAM("Micro ROV activated!");
        else
        ROS_INFO_STREAM("Micro ROV deactivated!");
    }

    if((prev_BackOff == 0) && (joy -> buttons[10]==1))
    {
        BackOff = BackOff? 0:1;
        if(BackOff)
        ROS_INFO_STREAM("Back thrusters off mode off!!");
        else
        ROS_INFO_STREAM("Back thrusters off mode ON!!");
    }

    if((prev_FrontOff == 0) && (joy -> buttons[8]==1))
    {
        FrontOff = FrontOff? 0:1;
        if(FrontOff)
        ROS_INFO_STREAM("Front thrusters off mode off!!");
        else
        ROS_INFO_STREAM("Front thrusters off mode ON!!");
    }

}
void Right()
{
    motorA = 1500 - 100;
	motorB = 1500 + 100;
	motorC = 1500 + 100;
	motorD = 1500 - 100;
}
void Left()
{
    motorA = 1500 + 100;
	motorB = 1500 - 100;
	motorC = 1500 - 100;
	motorD = 1500 + 100;
}

void concatenate_values ()
{
    std::stringstream ss;
    char buffer[4] = "";
    sprintf(buffer, "%d", motorF);
    if (!micro_activated)
    ss << "A" << motor_def_A << "B" <<  motor_def_B << "C" <<  motor_def_C << "D" <<  motor_def_D << "E" <<  motor_def_E << "F" <<  buffer << "G" << arm_button << piston_button << led_button << "K";
    else
    ss << "A" << motor_def_A << "B" <<  motor_def_B << "C" <<  motor_def_C << "D" <<  motor_def_D << "E" <<  motor_def_E << "F" <<  buffer << "G" << arm_button << piston_button << led_button << micro_str << "K";
    
    msg.data = ss.str();
}


/*
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
*/
