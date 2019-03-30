#include <ros/ros.h>
#include <serial/serial.h>
#include <std_msgs/String.h>
#include <std_msgs/Empty.h>

serial::Serial ser;
std_msgs::String result;
bool flag = false;



void write_callback(const std_msgs::String::ConstPtr& msg)
{	
    //ROS_INFO_STREAM("I'm in the callback function");
     if(ser.available())
    {
            //ROS_INFO_STREAM("Reading from serial port in callback func ");
            result.data = ser.readline(65536, "Z");
            ROS_INFO_STREAM("Read from callback: " << result.data);
            ser.flush();
            // read_pub.publish(result);
    }

    // ser.write(reinterpret_cast<const uint8_t*>(&msg->data), 24);
    // ser.write(msg->data);
    // ROS_INFO_STREAM("Writing to serial port " << msg->data);
    // ros::Duration(0.08).sleep();
    ser.flush();	

}

int main (int argc, char** argv){
    ros::init(argc, argv, "second_serial_node");
    ros::NodeHandle nh;
    ros::Publisher read_pub = nh.advertise<std_msgs::String>("read", 1000); 
    ros::Subscriber write_sub = nh.subscribe("motor_values", 1, write_callback);

    try
    {
        ser.setPort("/dev/ttyACM0");
        ser.setBaudrate(57600);
        serial::Timeout to = serial::Timeout::simpleTimeout(1000);
        ser.setTimeout(to);
        ser.open();
    }
    catch (serial::IOException& e)
    {
        ROS_ERROR_STREAM("Unable to open port ");
        return -1;
    }

    if(ser.isOpen()){
        ROS_INFO_STREAM("Serial Port initialized");
    }else{
        return -1;
    }

    ros::Rate loop_rate(2000);
    while(ros::ok())
    {
        ros::spinOnce();

        if(ser.available())
        {
            ROS_INFO_STREAM("Reading from serial port");
            result.data = ser.readline(65536, "Z");
            ROS_INFO_STREAM("Read: " << result.data);
            ser.flush();
            flag = true;
            read_pub.publish(result);
        }
        loop_rate.sleep();

    }
}

