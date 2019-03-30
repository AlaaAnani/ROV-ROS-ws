// Generated by gencpp from file GUI/motors.msg
// DO NOT EDIT!


#ifndef GUI_MESSAGE_MOTORS_H
#define GUI_MESSAGE_MOTORS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace GUI
{
template <class ContainerAllocator>
struct motors_
{
  typedef motors_<ContainerAllocator> Type;

  motors_()
    : motorA(0)
    , motorB(0)
    , motorC(0)
    , motorD(0)
    , motorE(0)
    , motorF(0)
    , PH_button(false)
    , TEMP_button(false)
    , MAG_button(false)
    , WATER_button(false)  {
    }
  motors_(const ContainerAllocator& _alloc)
    : motorA(0)
    , motorB(0)
    , motorC(0)
    , motorD(0)
    , motorE(0)
    , motorF(0)
    , PH_button(false)
    , TEMP_button(false)
    , MAG_button(false)
    , WATER_button(false)  {
  (void)_alloc;
    }



   typedef int64_t _motorA_type;
  _motorA_type motorA;

   typedef int64_t _motorB_type;
  _motorB_type motorB;

   typedef int64_t _motorC_type;
  _motorC_type motorC;

   typedef int64_t _motorD_type;
  _motorD_type motorD;

   typedef int64_t _motorE_type;
  _motorE_type motorE;

   typedef int64_t _motorF_type;
  _motorF_type motorF;

   typedef uint8_t _PH_button_type;
  _PH_button_type PH_button;

   typedef uint8_t _TEMP_button_type;
  _TEMP_button_type TEMP_button;

   typedef uint8_t _MAG_button_type;
  _MAG_button_type MAG_button;

   typedef uint8_t _WATER_button_type;
  _WATER_button_type WATER_button;





  typedef boost::shared_ptr< ::GUI::motors_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::GUI::motors_<ContainerAllocator> const> ConstPtr;

}; // struct motors_

typedef ::GUI::motors_<std::allocator<void> > motors;

typedef boost::shared_ptr< ::GUI::motors > motorsPtr;
typedef boost::shared_ptr< ::GUI::motors const> motorsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::GUI::motors_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::GUI::motors_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace GUI

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'GUI': ['/home/alaa/rov_ws/src/GUI/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::GUI::motors_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::GUI::motors_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::GUI::motors_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::GUI::motors_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::GUI::motors_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::GUI::motors_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::GUI::motors_<ContainerAllocator> >
{
  static const char* value()
  {
    return "217166abeed0122de3610215eeb90349";
  }

  static const char* value(const ::GUI::motors_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x217166abeed0122dULL;
  static const uint64_t static_value2 = 0xe3610215eeb90349ULL;
};

template<class ContainerAllocator>
struct DataType< ::GUI::motors_<ContainerAllocator> >
{
  static const char* value()
  {
    return "GUI/motors";
  }

  static const char* value(const ::GUI::motors_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::GUI::motors_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 motorA\n\
int64 motorB\n\
int64 motorC\n\
int64 motorD\n\
int64 motorE\n\
int64 motorF\n\
bool PH_button\n\
bool TEMP_button\n\
bool MAG_button\n\
bool WATER_button\n\
";
  }

  static const char* value(const ::GUI::motors_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::GUI::motors_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.motorA);
      stream.next(m.motorB);
      stream.next(m.motorC);
      stream.next(m.motorD);
      stream.next(m.motorE);
      stream.next(m.motorF);
      stream.next(m.PH_button);
      stream.next(m.TEMP_button);
      stream.next(m.MAG_button);
      stream.next(m.WATER_button);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct motors_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::GUI::motors_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::GUI::motors_<ContainerAllocator>& v)
  {
    s << indent << "motorA: ";
    Printer<int64_t>::stream(s, indent + "  ", v.motorA);
    s << indent << "motorB: ";
    Printer<int64_t>::stream(s, indent + "  ", v.motorB);
    s << indent << "motorC: ";
    Printer<int64_t>::stream(s, indent + "  ", v.motorC);
    s << indent << "motorD: ";
    Printer<int64_t>::stream(s, indent + "  ", v.motorD);
    s << indent << "motorE: ";
    Printer<int64_t>::stream(s, indent + "  ", v.motorE);
    s << indent << "motorF: ";
    Printer<int64_t>::stream(s, indent + "  ", v.motorF);
    s << indent << "PH_button: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.PH_button);
    s << indent << "TEMP_button: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.TEMP_button);
    s << indent << "MAG_button: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.MAG_button);
    s << indent << "WATER_button: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.WATER_button);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GUI_MESSAGE_MOTORS_H
