// Auto-generated. Do not edit!

// (in-package GUI.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class motors {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.motorA = null;
      this.motorB = null;
      this.motorC = null;
      this.motorD = null;
      this.motorE = null;
      this.motorF = null;
      this.PH_button = null;
      this.TEMP_button = null;
      this.MAG_button = null;
      this.WATER_button = null;
    }
    else {
      if (initObj.hasOwnProperty('motorA')) {
        this.motorA = initObj.motorA
      }
      else {
        this.motorA = 0;
      }
      if (initObj.hasOwnProperty('motorB')) {
        this.motorB = initObj.motorB
      }
      else {
        this.motorB = 0;
      }
      if (initObj.hasOwnProperty('motorC')) {
        this.motorC = initObj.motorC
      }
      else {
        this.motorC = 0;
      }
      if (initObj.hasOwnProperty('motorD')) {
        this.motorD = initObj.motorD
      }
      else {
        this.motorD = 0;
      }
      if (initObj.hasOwnProperty('motorE')) {
        this.motorE = initObj.motorE
      }
      else {
        this.motorE = 0;
      }
      if (initObj.hasOwnProperty('motorF')) {
        this.motorF = initObj.motorF
      }
      else {
        this.motorF = 0;
      }
      if (initObj.hasOwnProperty('PH_button')) {
        this.PH_button = initObj.PH_button
      }
      else {
        this.PH_button = false;
      }
      if (initObj.hasOwnProperty('TEMP_button')) {
        this.TEMP_button = initObj.TEMP_button
      }
      else {
        this.TEMP_button = false;
      }
      if (initObj.hasOwnProperty('MAG_button')) {
        this.MAG_button = initObj.MAG_button
      }
      else {
        this.MAG_button = false;
      }
      if (initObj.hasOwnProperty('WATER_button')) {
        this.WATER_button = initObj.WATER_button
      }
      else {
        this.WATER_button = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type motors
    // Serialize message field [motorA]
    bufferOffset = _serializer.int64(obj.motorA, buffer, bufferOffset);
    // Serialize message field [motorB]
    bufferOffset = _serializer.int64(obj.motorB, buffer, bufferOffset);
    // Serialize message field [motorC]
    bufferOffset = _serializer.int64(obj.motorC, buffer, bufferOffset);
    // Serialize message field [motorD]
    bufferOffset = _serializer.int64(obj.motorD, buffer, bufferOffset);
    // Serialize message field [motorE]
    bufferOffset = _serializer.int64(obj.motorE, buffer, bufferOffset);
    // Serialize message field [motorF]
    bufferOffset = _serializer.int64(obj.motorF, buffer, bufferOffset);
    // Serialize message field [PH_button]
    bufferOffset = _serializer.bool(obj.PH_button, buffer, bufferOffset);
    // Serialize message field [TEMP_button]
    bufferOffset = _serializer.bool(obj.TEMP_button, buffer, bufferOffset);
    // Serialize message field [MAG_button]
    bufferOffset = _serializer.bool(obj.MAG_button, buffer, bufferOffset);
    // Serialize message field [WATER_button]
    bufferOffset = _serializer.bool(obj.WATER_button, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type motors
    let len;
    let data = new motors(null);
    // Deserialize message field [motorA]
    data.motorA = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [motorB]
    data.motorB = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [motorC]
    data.motorC = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [motorD]
    data.motorD = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [motorE]
    data.motorE = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [motorF]
    data.motorF = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [PH_button]
    data.PH_button = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [TEMP_button]
    data.TEMP_button = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [MAG_button]
    data.MAG_button = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [WATER_button]
    data.WATER_button = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 52;
  }

  static datatype() {
    // Returns string type for a message object
    return 'GUI/motors';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '217166abeed0122de3610215eeb90349';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 motorA
    int64 motorB
    int64 motorC
    int64 motorD
    int64 motorE
    int64 motorF
    bool PH_button
    bool TEMP_button
    bool MAG_button
    bool WATER_button
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new motors(null);
    if (msg.motorA !== undefined) {
      resolved.motorA = msg.motorA;
    }
    else {
      resolved.motorA = 0
    }

    if (msg.motorB !== undefined) {
      resolved.motorB = msg.motorB;
    }
    else {
      resolved.motorB = 0
    }

    if (msg.motorC !== undefined) {
      resolved.motorC = msg.motorC;
    }
    else {
      resolved.motorC = 0
    }

    if (msg.motorD !== undefined) {
      resolved.motorD = msg.motorD;
    }
    else {
      resolved.motorD = 0
    }

    if (msg.motorE !== undefined) {
      resolved.motorE = msg.motorE;
    }
    else {
      resolved.motorE = 0
    }

    if (msg.motorF !== undefined) {
      resolved.motorF = msg.motorF;
    }
    else {
      resolved.motorF = 0
    }

    if (msg.PH_button !== undefined) {
      resolved.PH_button = msg.PH_button;
    }
    else {
      resolved.PH_button = false
    }

    if (msg.TEMP_button !== undefined) {
      resolved.TEMP_button = msg.TEMP_button;
    }
    else {
      resolved.TEMP_button = false
    }

    if (msg.MAG_button !== undefined) {
      resolved.MAG_button = msg.MAG_button;
    }
    else {
      resolved.MAG_button = false
    }

    if (msg.WATER_button !== undefined) {
      resolved.WATER_button = msg.WATER_button;
    }
    else {
      resolved.WATER_button = false
    }

    return resolved;
    }
};

module.exports = motors;
