#ifndef _ROS_motion_map_motors_h
#define _ROS_motion_map_motors_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace motion_map
{

  class motors : public ros::Msg
  {
    public:
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

    motors():
      motorA(0),
      motorB(0),
      motorC(0),
      motorD(0),
      motorE(0),
      motorF(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int64_t real;
        uint64_t base;
      } u_motorA;
      u_motorA.real = this->motorA;
      *(outbuffer + offset + 0) = (u_motorA.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_motorA.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_motorA.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_motorA.base >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (u_motorA.base >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (u_motorA.base >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (u_motorA.base >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (u_motorA.base >> (8 * 7)) & 0xFF;
      offset += sizeof(this->motorA);
      union {
        int64_t real;
        uint64_t base;
      } u_motorB;
      u_motorB.real = this->motorB;
      *(outbuffer + offset + 0) = (u_motorB.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_motorB.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_motorB.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_motorB.base >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (u_motorB.base >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (u_motorB.base >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (u_motorB.base >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (u_motorB.base >> (8 * 7)) & 0xFF;
      offset += sizeof(this->motorB);
      union {
        int64_t real;
        uint64_t base;
      } u_motorC;
      u_motorC.real = this->motorC;
      *(outbuffer + offset + 0) = (u_motorC.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_motorC.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_motorC.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_motorC.base >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (u_motorC.base >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (u_motorC.base >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (u_motorC.base >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (u_motorC.base >> (8 * 7)) & 0xFF;
      offset += sizeof(this->motorC);
      union {
        int64_t real;
        uint64_t base;
      } u_motorD;
      u_motorD.real = this->motorD;
      *(outbuffer + offset + 0) = (u_motorD.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_motorD.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_motorD.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_motorD.base >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (u_motorD.base >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (u_motorD.base >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (u_motorD.base >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (u_motorD.base >> (8 * 7)) & 0xFF;
      offset += sizeof(this->motorD);
      union {
        int64_t real;
        uint64_t base;
      } u_motorE;
      u_motorE.real = this->motorE;
      *(outbuffer + offset + 0) = (u_motorE.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_motorE.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_motorE.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_motorE.base >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (u_motorE.base >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (u_motorE.base >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (u_motorE.base >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (u_motorE.base >> (8 * 7)) & 0xFF;
      offset += sizeof(this->motorE);
      union {
        int64_t real;
        uint64_t base;
      } u_motorF;
      u_motorF.real = this->motorF;
      *(outbuffer + offset + 0) = (u_motorF.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_motorF.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_motorF.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_motorF.base >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (u_motorF.base >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (u_motorF.base >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (u_motorF.base >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (u_motorF.base >> (8 * 7)) & 0xFF;
      offset += sizeof(this->motorF);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int64_t real;
        uint64_t base;
      } u_motorA;
      u_motorA.base = 0;
      u_motorA.base |= ((uint64_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_motorA.base |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_motorA.base |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_motorA.base |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      u_motorA.base |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      u_motorA.base |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      u_motorA.base |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      u_motorA.base |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      this->motorA = u_motorA.real;
      offset += sizeof(this->motorA);
      union {
        int64_t real;
        uint64_t base;
      } u_motorB;
      u_motorB.base = 0;
      u_motorB.base |= ((uint64_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_motorB.base |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_motorB.base |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_motorB.base |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      u_motorB.base |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      u_motorB.base |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      u_motorB.base |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      u_motorB.base |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      this->motorB = u_motorB.real;
      offset += sizeof(this->motorB);
      union {
        int64_t real;
        uint64_t base;
      } u_motorC;
      u_motorC.base = 0;
      u_motorC.base |= ((uint64_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_motorC.base |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_motorC.base |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_motorC.base |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      u_motorC.base |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      u_motorC.base |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      u_motorC.base |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      u_motorC.base |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      this->motorC = u_motorC.real;
      offset += sizeof(this->motorC);
      union {
        int64_t real;
        uint64_t base;
      } u_motorD;
      u_motorD.base = 0;
      u_motorD.base |= ((uint64_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_motorD.base |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_motorD.base |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_motorD.base |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      u_motorD.base |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      u_motorD.base |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      u_motorD.base |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      u_motorD.base |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      this->motorD = u_motorD.real;
      offset += sizeof(this->motorD);
      union {
        int64_t real;
        uint64_t base;
      } u_motorE;
      u_motorE.base = 0;
      u_motorE.base |= ((uint64_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_motorE.base |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_motorE.base |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_motorE.base |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      u_motorE.base |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      u_motorE.base |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      u_motorE.base |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      u_motorE.base |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      this->motorE = u_motorE.real;
      offset += sizeof(this->motorE);
      union {
        int64_t real;
        uint64_t base;
      } u_motorF;
      u_motorF.base = 0;
      u_motorF.base |= ((uint64_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_motorF.base |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_motorF.base |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_motorF.base |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      u_motorF.base |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      u_motorF.base |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      u_motorF.base |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      u_motorF.base |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      this->motorF = u_motorF.real;
      offset += sizeof(this->motorF);
     return offset;
    }

    const char * getType(){ return "motion_map/motors"; };
    const char * getMD5(){ return "7fd885102d37e484f560b36cd48ea41c"; };

  };

}
#endif