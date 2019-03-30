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

class cannonNumbers {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.r1 = null;
      this.r2 = null;
      this.r3 = null;
      this.l = null;
      this.vol = null;
      this.weight = null;
    }
    else {
      if (initObj.hasOwnProperty('r1')) {
        this.r1 = initObj.r1
      }
      else {
        this.r1 = 0.0;
      }
      if (initObj.hasOwnProperty('r2')) {
        this.r2 = initObj.r2
      }
      else {
        this.r2 = 0.0;
      }
      if (initObj.hasOwnProperty('r3')) {
        this.r3 = initObj.r3
      }
      else {
        this.r3 = 0.0;
      }
      if (initObj.hasOwnProperty('l')) {
        this.l = initObj.l
      }
      else {
        this.l = 0.0;
      }
      if (initObj.hasOwnProperty('vol')) {
        this.vol = initObj.vol
      }
      else {
        this.vol = 0.0;
      }
      if (initObj.hasOwnProperty('weight')) {
        this.weight = initObj.weight
      }
      else {
        this.weight = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type cannonNumbers
    // Serialize message field [r1]
    bufferOffset = _serializer.float64(obj.r1, buffer, bufferOffset);
    // Serialize message field [r2]
    bufferOffset = _serializer.float64(obj.r2, buffer, bufferOffset);
    // Serialize message field [r3]
    bufferOffset = _serializer.float64(obj.r3, buffer, bufferOffset);
    // Serialize message field [l]
    bufferOffset = _serializer.float64(obj.l, buffer, bufferOffset);
    // Serialize message field [vol]
    bufferOffset = _serializer.float64(obj.vol, buffer, bufferOffset);
    // Serialize message field [weight]
    bufferOffset = _serializer.float64(obj.weight, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type cannonNumbers
    let len;
    let data = new cannonNumbers(null);
    // Deserialize message field [r1]
    data.r1 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [r2]
    data.r2 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [r3]
    data.r3 = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [l]
    data.l = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [vol]
    data.vol = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [weight]
    data.weight = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'GUI/cannonNumbers';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b96d3a629a34dfd2040e80b4afc99711';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 r1
    float64 r2
    float64 r3
    float64 l
    float64 vol
    float64 weight
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new cannonNumbers(null);
    if (msg.r1 !== undefined) {
      resolved.r1 = msg.r1;
    }
    else {
      resolved.r1 = 0.0
    }

    if (msg.r2 !== undefined) {
      resolved.r2 = msg.r2;
    }
    else {
      resolved.r2 = 0.0
    }

    if (msg.r3 !== undefined) {
      resolved.r3 = msg.r3;
    }
    else {
      resolved.r3 = 0.0
    }

    if (msg.l !== undefined) {
      resolved.l = msg.l;
    }
    else {
      resolved.l = 0.0
    }

    if (msg.vol !== undefined) {
      resolved.vol = msg.vol;
    }
    else {
      resolved.vol = 0.0
    }

    if (msg.weight !== undefined) {
      resolved.weight = msg.weight;
    }
    else {
      resolved.weight = 0.0
    }

    return resolved;
    }
};

module.exports = cannonNumbers;
