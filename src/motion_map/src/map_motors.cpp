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



std_msgs::String msg;
std::string dir_var;
std::string line_enable = "stop";
const int speed = 250;
int motorA, motorB, motorC, motorD, motorE, motorF, motor_def_A, motor_def_B, motor_def_C, motor_def_D, motor_def_E, motor_def_F;
float yaw_control_effort, pitch_control_effort, depth_control_effort;
bool PH_button = false, TEMP_button = false, arm_button = false, t_shapes_button1 = false, t_shapes_button2 = false, micro_rov_key = false, led_button = false;
const int A_sign = -1;
const int B_sign = 1;
const int C_sign = -1;
const int D_sign = -1;
const int E_sign = 1;
const int F_sign = -1;

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

void TeleopROV::direction_Callback(const std_msgs::String::ConstPtr& dir)
{
   dir_var = dir->data;
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

    ss << "A" << motor_def_A << "B" <<  motor_def_B << "C" <<  buffer << "D" <<  motor_def_D << "E" <<  motor_def_E << "F" <<  motor_def_F << "G" << PH_button << arm_button << t_shapes_button1<< t_shapes_button2<< "K";
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
    float z_axis_analog = (joy->axes[3] + 1)/2.0;
    int diagonal_mag = sqrt(pow(joy->axes[0], 2) + pow(joy->axes[1], 2));
    int diagonal_sign = ((joy->axes[1]<0)? -1:1);

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


        ///////////////////////////////// end

if (line_enable == "stop") // if line follwer is not enabled
{
    if (joy -> buttons[5]) // reverse motion  ---->>> (check an unused button for activating the reverse motion)
     {
         if(joy->axes[5] != 0)     //Tilting
	    {
	      motorE = 1500 + (speed*joy -> axes[5]);
	      motorF = 1500 - (speed*joy -> axes[5]);
	    }
  	    
	    else if(joy->buttons[4]) //Z-Axis UP
	    {
	     motorE = 1500 + (speed*z_axis_analog);
	     motorF = 1500 + (speed*z_axis_analog);
	    }
	    
	    else if(joy->buttons[2]) //Z-axis DOWN
	    {
		motorE = 1500 - (speed*z_axis_analog);
		motorF = 1500 - (speed*z_axis_analog);
	    }
	    else
	    {
		motorE = 1500;
		motorF = 1500;
	    }


	    if(joy->axes [2] != 0  && (joy->axes [2] > 0.5 || joy->axes [2] < -0.3))     //Z-Axis Rotation is required in joystick, give motors D and E reverse values
	    {
		motorB = 1500 - (speed*joy -> axes[2]);
		motorA = 1500 + (speed*joy -> axes[2]);
		motorC = 1500 + (speed*joy -> axes[2]);
		motorD = 1500 - (speed*joy -> axes[2]);
	     
	    }
	    else if(joy->axes[1] != 0 && joy->axes[0] != 0 ) //X and Y--> Diagonal
	    {
		if((joy->axes[1] < 0 && joy->axes[0] < 0) && (joy->axes[1] > 0 && joy->axes[0] > 0))
		{
		    motorB = 1500 - diagonal_mag*diagonal_sign;
		    motorA = 1500;
		    motorC = 1500 - diagonal_mag*diagonal_sign;
		    motorD = 1500;
		}
		else
		{
		    motorA = 1500 - diagonal_mag*diagonal_sign;
		    motorB = 1500;
		    motorD = 1500 - diagonal_mag*diagonal_sign;
		    motorC = 1500;
		}    
	    }
	    else if(joy->axes[1] != 0)        //Move forward/backward
	    {
	    motorB = 1500 - (speed*joy -> axes[1]);
	    motorA = 1500 - (speed*joy -> axes[1]);
	    motorC = 1500 - (speed*joy -> axes[1]);
	    motorD = 1500 - (speed*joy -> axes[1]);
	    }
	    else if(joy->axes[0] != 0)         // Move left/right
	    {
	    motorA = 1500 + (speed*joy -> axes[0]);
	    motorB = 1500 - (speed*joy -> axes[0]);
	    motorC = 1500 - (speed*joy -> axes[0]);
	    motorD = 1500 + (speed*joy -> axes[0]);
	    }
	    else 
	    {
		motorA = 1500;
		motorB = 1500;
		motorC = 1500;
		motorD = 1500;
	    }
      }

    else // joy normal motion 
      {

    if(joy->axes[5] != 0)     //Tilting
    {
      motorE = 1500 - (E_sign)*(speed*joy -> axes[5]);
      motorF = 1500 + (F_sign)*(speed*joy -> axes[5]);
    }
    
    else if(joy->buttons[4]) //Z-Axis UP
    {
     motorE = 1500 + (E_sign)*(speed*z_axis_analog);
     motorF = 1500 + (F_sign)*(speed*z_axis_analog);
    }
    
    else if(joy->buttons[2]) //Z-axis DOWN
    {
        motorE = 1500 - (E_sign)*(speed*z_axis_analog);
        motorF = 1500 - (F_sign)*(speed*z_axis_analog);
    }
    else
    {
        motorE = 1500;
        motorF = 1500;
    }


    if(joy->axes [2] != 0  && (joy->axes [2] > 0.5 || joy->axes [2] < -0.8))     //Z-Axis Rotation is required in joystick, give motors D and E reverse values
    {
        motorB = 1500 + (B_sign)*(speed*joy -> axes[2]);
        motorA = 1500 - (A_sign)*(speed*joy -> axes[2]);
        motorC = 1500 - (C_sign)*(speed*joy -> axes[2]);
        motorD = 1500 + (D_sign)*(speed*joy -> axes[2]);
     
    }
    else if(joy->axes[1] != 0 && joy->axes[0] != 0 ) //X and Y--> Diagonal
    {
        if((joy->axes[1] < 0 && joy->axes[0] < 0) && (joy->axes[1] > 0 && joy->axes[0] > 0))
        {
            motorB = 1500 + (B_sign) *diagonal_mag*diagonal_sign;
            motorA = 1500;
            motorC = 1500 + (C_sign) * diagonal_mag*diagonal_sign;
            motorD = 1500;
        }
        else
        {
            motorA = 1500 + (A_sign) * diagonal_mag*diagonal_sign;
            motorB = 1500;
            motorD = 1500 + (D_sign) * diagonal_mag*diagonal_sign;
            motorC = 1500;
        }    
    }
    else if(joy->axes[1] != 0)        //Move forward/backward
    {
        // ROS_INFO_STREAM("I'm in the right case");
    motorB = 1500 + (B_sign)* (speed*joy -> axes[1]);
    motorA = 1500 + (A_sign)* (speed*joy -> axes[1]);
    motorC = 1500 + (C_sign)* (speed*joy -> axes[1]);
    motorD = 1500 + (D_sign)* (speed*joy -> axes[1]);
    }
    else if(joy->axes[0] != 0)         // Move left/right
    {
    motorA = 1500 - (A_sign)*(speed*joy -> axes[0]);
    motorB = 1500 + (B_sign)* (speed*joy -> axes[0]);
    motorC = 1500 + (C_sign)*(speed*joy -> axes[0]);
    motorD = 1500 - (D_sign)*(speed*joy -> axes[0]);
    }
    else
    {
        motorA = 1500;
        motorB = 1500;
        motorC = 1500;
        motorD = 1500;
    }
      }
}

    if (yaw_control_effort == 0 && pitch_control_effort == 0 && depth_control_effort == 0 && line_enable == "stop")
        {
            ROS_INFO_STREAM("I'm in the callback function");
            std::stringstream ss;
            char buffer[4] = "";
            sprintf(buffer, "%d", motorF);

            ss << "A" << motor_def_A << "B" <<  motor_def_B << "C" <<  buffer << "D" <<  motor_def_D << "E" <<  motor_def_E << "F" <<  motor_def_F << "G" << PH_button << arm_button << t_shapes_button1<< t_shapes_button2<< "K";
            msg.data = ss.str();
            rov_pub_.publish(msg);   
        }

    // PID part
    
    // ros::Duration(0.01).sleep();

}



int main(int argc, char** argv)
{
    ros::init(argc, argv, "map_motors");
    
    TeleopROV teleop_ROV;

    ros::Rate loop_rate(10);
    
    while (ros::ok())
    {
        if (line_enable == "start") // if the line follwer task is on
{
	  if (dir_var == "right")
	   {
           ROS_INFO_STREAM("line_follower right");
	    motorA = 1500 + (A_sign)*(100);
        motorB = 1500 - (B_sign)*(100);
        motorC = 1500 - (C_sign)*(100);
        motorD = 1500 + (D_sign)*(100);
	   }
	  else if (dir_var == "left")
	   {
           ROS_INFO_STREAM("line_follower left");
	    motorA = 1500 - (A_sign)*(100);
        motorB = 1500 + (B_sign)*(100);
        motorC = 1500 + (C_sign)*(100);
        motorD = 1500 - (D_sign)*(100);
	   }
	   else if (dir_var == "up")
	    {
            ROS_INFO_STREAM("line_follower up");
	    motorE = 1500 + (E_sign)*(200);
        motorF = 1500 + (F_sign)*(200);
	    }
	   else if (dir_var == "down")
	    {
            ROS_INFO_STREAM("line_follower down");
	    motorE = 1500 - (E_sign)*(200);
        motorF = 1500 - (F_sign)*(200);
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
}


        if (yaw_control_effort != 0 || pitch_control_effort != 0 || depth_control_effort != 0)
        {
        ROS_INFO_STREAM("I'm in the while loop" << yaw_control_effort);
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
        else
        {
            teleop_ROV.publish();
        }
        

        yaw_control_effort = 0;
        pitch_control_effort = 0;
        depth_control_effort = 0;
        
        ros::spinOnce();
        loop_rate.sleep();
    } 


  return 0;
}
