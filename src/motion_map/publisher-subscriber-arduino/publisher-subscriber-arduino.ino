/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/String.h>
#include "motors.h"

ros::NodeHandle  nh;

//Publisher
std_msgs::String str_msg;
ros::Publisher chatter("arduino_response", &str_msg);



void messageCb( const motion_map::motors& MotorMsgVariable)
{ 
  if(MotorMsgVariable.motorA > 1500)
    digitalWrite(13, HIGH);
  else
    digitalWrite(13, LOW);

      chatter.publish( &str_msg );
}

ros::Subscriber<motion_map:: motors> sub("motor_values", &messageCb );

void setup()
{ 
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(chatter);
}

void loop()
{  
  nh.spinOnce();
  //delay(10);
  
}
