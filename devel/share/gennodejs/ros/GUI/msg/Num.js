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

class Num {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.circlesNo = null;
      this.trianglesNo = null;
      this.linesNo = null;
      this.squaresNo = null;
    }
    else {
      if (initObj.hasOwnProperty('circlesNo')) {
        this.circlesNo = initObj.circlesNo
      }
      else {
        this.circlesNo = 0;
      }
      if (initObj.hasOwnProperty('trianglesNo')) {
        this.trianglesNo = initObj.trianglesNo
      }
      else {
        this.trianglesNo = 0;
      }
      if (initObj.hasOwnProperty('linesNo')) {
        this.linesNo = initObj.linesNo
      }
      else {
        this.linesNo = 0;
      }
      if (initObj.hasOwnProperty('squaresNo')) {
        this.squaresNo = initObj.squaresNo
      }
      else {
        this.squaresNo = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Num
    // Serialize message field [circlesNo]
    bufferOffset = _serializer.int64(obj.circlesNo, buffer, bufferOffset);
    // Serialize message field [trianglesNo]
    bufferOffset = _serializer.int64(obj.trianglesNo, buffer, bufferOffset);
    // Serialize message field [linesNo]
    bufferOffset = _serializer.int64(obj.linesNo, buffer, bufferOffset);
    // Serialize message field [squaresNo]
    bufferOffset = _serializer.int64(obj.squaresNo, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Num
    let len;
    let data = new Num(null);
    // Deserialize message field [circlesNo]
    data.circlesNo = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [trianglesNo]
    data.trianglesNo = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [linesNo]
    data.linesNo = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [squaresNo]
    data.squaresNo = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'GUI/Num';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cc4fa4ab5eb670e25a1c738431aed253';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 circlesNo
    int64 trianglesNo
    int64 linesNo
    int64 squaresNo
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Num(null);
    if (msg.circlesNo !== undefined) {
      resolved.circlesNo = msg.circlesNo;
    }
    else {
      resolved.circlesNo = 0
    }

    if (msg.trianglesNo !== undefined) {
      resolved.trianglesNo = msg.trianglesNo;
    }
    else {
      resolved.trianglesNo = 0
    }

    if (msg.linesNo !== undefined) {
      resolved.linesNo = msg.linesNo;
    }
    else {
      resolved.linesNo = 0
    }

    if (msg.squaresNo !== undefined) {
      resolved.squaresNo = msg.squaresNo;
    }
    else {
      resolved.squaresNo = 0
    }

    return resolved;
    }
};

module.exports = Num;
