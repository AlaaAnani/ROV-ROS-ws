// Auto-generated. Do not edit!

// (in-package distributor.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class rov_msgs {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pitch = null;
      this.roll = null;
      this.yaw = null;
      this.acc_x = null;
      this.acc_y = null;
      this.acc_z = null;
      this.gyro_x = null;
      this.gyro_y = null;
      this.gyro_z = null;
      this.paro = null;
      this.PH = null;
      this.water = null;
      this.temp = null;
      this.mag1 = null;
      this.mag2 = null;
      this.mag3 = null;
    }
    else {
      if (initObj.hasOwnProperty('pitch')) {
        this.pitch = initObj.pitch
      }
      else {
        this.pitch = 0.0;
      }
      if (initObj.hasOwnProperty('roll')) {
        this.roll = initObj.roll
      }
      else {
        this.roll = 0.0;
      }
      if (initObj.hasOwnProperty('yaw')) {
        this.yaw = initObj.yaw
      }
      else {
        this.yaw = 0.0;
      }
      if (initObj.hasOwnProperty('acc_x')) {
        this.acc_x = initObj.acc_x
      }
      else {
        this.acc_x = 0.0;
      }
      if (initObj.hasOwnProperty('acc_y')) {
        this.acc_y = initObj.acc_y
      }
      else {
        this.acc_y = 0.0;
      }
      if (initObj.hasOwnProperty('acc_z')) {
        this.acc_z = initObj.acc_z
      }
      else {
        this.acc_z = 0.0;
      }
      if (initObj.hasOwnProperty('gyro_x')) {
        this.gyro_x = initObj.gyro_x
      }
      else {
        this.gyro_x = 0.0;
      }
      if (initObj.hasOwnProperty('gyro_y')) {
        this.gyro_y = initObj.gyro_y
      }
      else {
        this.gyro_y = 0.0;
      }
      if (initObj.hasOwnProperty('gyro_z')) {
        this.gyro_z = initObj.gyro_z
      }
      else {
        this.gyro_z = 0.0;
      }
      if (initObj.hasOwnProperty('paro')) {
        this.paro = initObj.paro
      }
      else {
        this.paro = 0.0;
      }
      if (initObj.hasOwnProperty('PH')) {
        this.PH = initObj.PH
      }
      else {
        this.PH = 0.0;
      }
      if (initObj.hasOwnProperty('water')) {
        this.water = initObj.water
      }
      else {
        this.water = 0.0;
      }
      if (initObj.hasOwnProperty('temp')) {
        this.temp = initObj.temp
      }
      else {
        this.temp = 0.0;
      }
      if (initObj.hasOwnProperty('mag1')) {
        this.mag1 = initObj.mag1
      }
      else {
        this.mag1 = 0.0;
      }
      if (initObj.hasOwnProperty('mag2')) {
        this.mag2 = initObj.mag2
      }
      else {
        this.mag2 = 0.0;
      }
      if (initObj.hasOwnProperty('mag3')) {
        this.mag3 = initObj.mag3
      }
      else {
        this.mag3 = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type rov_msgs
    // Serialize message field [pitch]
    bufferOffset = _serializer.float64(obj.pitch, buffer, bufferOffset);
    // Serialize message field [roll]
    bufferOffset = _serializer.float64(obj.roll, buffer, bufferOffset);
    // Serialize message field [yaw]
    bufferOffset = _serializer.float64(obj.yaw, buffer, bufferOffset);
    // Serialize message field [acc_x]
    bufferOffset = _serializer.float64(obj.acc_x, buffer, bufferOffset);
    // Serialize message field [acc_y]
    bufferOffset = _serializer.float64(obj.acc_y, buffer, bufferOffset);
    // Serialize message field [acc_z]
    bufferOffset = _serializer.float64(obj.acc_z, buffer, bufferOffset);
    // Serialize message field [gyro_x]
    bufferOffset = _serializer.float64(obj.gyro_x, buffer, bufferOffset);
    // Serialize message field [gyro_y]
    bufferOffset = _serializer.float64(obj.gyro_y, buffer, bufferOffset);
    // Serialize message field [gyro_z]
    bufferOffset = _serializer.float64(obj.gyro_z, buffer, bufferOffset);
    // Serialize message field [paro]
    bufferOffset = _serializer.float64(obj.paro, buffer, bufferOffset);
    // Serialize message field [PH]
    bufferOffset = _serializer.float64(obj.PH, buffer, bufferOffset);
    // Serialize message field [water]
    bufferOffset = _serializer.float64(obj.water, buffer, bufferOffset);
    // Serialize message field [temp]
    bufferOffset = _serializer.float64(obj.temp, buffer, bufferOffset);
    // Serialize message field [mag1]
    bufferOffset = _serializer.float64(obj.mag1, buffer, bufferOffset);
    // Serialize message field [mag2]
    bufferOffset = _serializer.float64(obj.mag2, buffer, bufferOffset);
    // Serialize message field [mag3]
    bufferOffset = _serializer.float64(obj.mag3, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type rov_msgs
    let len;
    let data = new rov_msgs(null);
    // Deserialize message field [pitch]
    data.pitch = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [roll]
    data.roll = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yaw]
    data.yaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [acc_x]
    data.acc_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [acc_y]
    data.acc_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [acc_z]
    data.acc_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [gyro_x]
    data.gyro_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [gyro_y]
    data.gyro_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [gyro_z]
    data.gyro_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [paro]
    data.paro = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [PH]
    data.PH = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [water]
    data.water = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [temp]
    data.temp = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [mag1]
    data.mag1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [mag2]
    data.mag2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [mag3]
    data.mag3 = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 128;
  }

  static datatype() {
    // Returns string type for a message object
    return 'distributor/rov_msgs';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '580798bc75b1af001886c0456174d658';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 pitch
    float64 roll
    float64 yaw
    float64 acc_x
    float64 acc_y
    float64 acc_z
    float64 gyro_x
    float64 gyro_y
    float64 gyro_z
    float64 paro
    float64 PH
    float64 water
    float64 temp
    float64 mag1
    float64 mag2
    float64 mag3
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new rov_msgs(null);
    if (msg.pitch !== undefined) {
      resolved.pitch = msg.pitch;
    }
    else {
      resolved.pitch = 0.0
    }

    if (msg.roll !== undefined) {
      resolved.roll = msg.roll;
    }
    else {
      resolved.roll = 0.0
    }

    if (msg.yaw !== undefined) {
      resolved.yaw = msg.yaw;
    }
    else {
      resolved.yaw = 0.0
    }

    if (msg.acc_x !== undefined) {
      resolved.acc_x = msg.acc_x;
    }
    else {
      resolved.acc_x = 0.0
    }

    if (msg.acc_y !== undefined) {
      resolved.acc_y = msg.acc_y;
    }
    else {
      resolved.acc_y = 0.0
    }

    if (msg.acc_z !== undefined) {
      resolved.acc_z = msg.acc_z;
    }
    else {
      resolved.acc_z = 0.0
    }

    if (msg.gyro_x !== undefined) {
      resolved.gyro_x = msg.gyro_x;
    }
    else {
      resolved.gyro_x = 0.0
    }

    if (msg.gyro_y !== undefined) {
      resolved.gyro_y = msg.gyro_y;
    }
    else {
      resolved.gyro_y = 0.0
    }

    if (msg.gyro_z !== undefined) {
      resolved.gyro_z = msg.gyro_z;
    }
    else {
      resolved.gyro_z = 0.0
    }

    if (msg.paro !== undefined) {
      resolved.paro = msg.paro;
    }
    else {
      resolved.paro = 0.0
    }

    if (msg.PH !== undefined) {
      resolved.PH = msg.PH;
    }
    else {
      resolved.PH = 0.0
    }

    if (msg.water !== undefined) {
      resolved.water = msg.water;
    }
    else {
      resolved.water = 0.0
    }

    if (msg.temp !== undefined) {
      resolved.temp = msg.temp;
    }
    else {
      resolved.temp = 0.0
    }

    if (msg.mag1 !== undefined) {
      resolved.mag1 = msg.mag1;
    }
    else {
      resolved.mag1 = 0.0
    }

    if (msg.mag2 !== undefined) {
      resolved.mag2 = msg.mag2;
    }
    else {
      resolved.mag2 = 0.0
    }

    if (msg.mag3 !== undefined) {
      resolved.mag3 = msg.mag3;
    }
    else {
      resolved.mag3 = 0.0
    }

    return resolved;
    }
};

module.exports = rov_msgs;
