; Auto-generated. Do not edit!


(cl:in-package GUI-msg)


;//! \htmlinclude motors.msg.html

(cl:defclass <motors> (roslisp-msg-protocol:ros-message)
  ((motorA
    :reader motorA
    :initarg :motorA
    :type cl:integer
    :initform 0)
   (motorB
    :reader motorB
    :initarg :motorB
    :type cl:integer
    :initform 0)
   (motorC
    :reader motorC
    :initarg :motorC
    :type cl:integer
    :initform 0)
   (motorD
    :reader motorD
    :initarg :motorD
    :type cl:integer
    :initform 0)
   (motorE
    :reader motorE
    :initarg :motorE
    :type cl:integer
    :initform 0)
   (motorF
    :reader motorF
    :initarg :motorF
    :type cl:integer
    :initform 0)
   (PH_button
    :reader PH_button
    :initarg :PH_button
    :type cl:boolean
    :initform cl:nil)
   (TEMP_button
    :reader TEMP_button
    :initarg :TEMP_button
    :type cl:boolean
    :initform cl:nil)
   (MAG_button
    :reader MAG_button
    :initarg :MAG_button
    :type cl:boolean
    :initform cl:nil)
   (WATER_button
    :reader WATER_button
    :initarg :WATER_button
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass motors (<motors>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <motors>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'motors)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name GUI-msg:<motors> is deprecated: use GUI-msg:motors instead.")))

(cl:ensure-generic-function 'motorA-val :lambda-list '(m))
(cl:defmethod motorA-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:motorA-val is deprecated.  Use GUI-msg:motorA instead.")
  (motorA m))

(cl:ensure-generic-function 'motorB-val :lambda-list '(m))
(cl:defmethod motorB-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:motorB-val is deprecated.  Use GUI-msg:motorB instead.")
  (motorB m))

(cl:ensure-generic-function 'motorC-val :lambda-list '(m))
(cl:defmethod motorC-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:motorC-val is deprecated.  Use GUI-msg:motorC instead.")
  (motorC m))

(cl:ensure-generic-function 'motorD-val :lambda-list '(m))
(cl:defmethod motorD-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:motorD-val is deprecated.  Use GUI-msg:motorD instead.")
  (motorD m))

(cl:ensure-generic-function 'motorE-val :lambda-list '(m))
(cl:defmethod motorE-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:motorE-val is deprecated.  Use GUI-msg:motorE instead.")
  (motorE m))

(cl:ensure-generic-function 'motorF-val :lambda-list '(m))
(cl:defmethod motorF-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:motorF-val is deprecated.  Use GUI-msg:motorF instead.")
  (motorF m))

(cl:ensure-generic-function 'PH_button-val :lambda-list '(m))
(cl:defmethod PH_button-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:PH_button-val is deprecated.  Use GUI-msg:PH_button instead.")
  (PH_button m))

(cl:ensure-generic-function 'TEMP_button-val :lambda-list '(m))
(cl:defmethod TEMP_button-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:TEMP_button-val is deprecated.  Use GUI-msg:TEMP_button instead.")
  (TEMP_button m))

(cl:ensure-generic-function 'MAG_button-val :lambda-list '(m))
(cl:defmethod MAG_button-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:MAG_button-val is deprecated.  Use GUI-msg:MAG_button instead.")
  (MAG_button m))

(cl:ensure-generic-function 'WATER_button-val :lambda-list '(m))
(cl:defmethod WATER_button-val ((m <motors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader GUI-msg:WATER_button-val is deprecated.  Use GUI-msg:WATER_button instead.")
  (WATER_button m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <motors>) ostream)
  "Serializes a message object of type '<motors>"
  (cl:let* ((signed (cl:slot-value msg 'motorA)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'motorB)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'motorC)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'motorD)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'motorE)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'motorF)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'PH_button) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'TEMP_button) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'MAG_button) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'WATER_button) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <motors>) istream)
  "Deserializes a message object of type '<motors>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motorA) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motorB) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motorC) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motorD) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motorE) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'motorF) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:setf (cl:slot-value msg 'PH_button) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'TEMP_button) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'MAG_button) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'WATER_button) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<motors>)))
  "Returns string type for a message object of type '<motors>"
  "GUI/motors")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'motors)))
  "Returns string type for a message object of type 'motors"
  "GUI/motors")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<motors>)))
  "Returns md5sum for a message object of type '<motors>"
  "217166abeed0122de3610215eeb90349")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'motors)))
  "Returns md5sum for a message object of type 'motors"
  "217166abeed0122de3610215eeb90349")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<motors>)))
  "Returns full string definition for message of type '<motors>"
  (cl:format cl:nil "int64 motorA~%int64 motorB~%int64 motorC~%int64 motorD~%int64 motorE~%int64 motorF~%bool PH_button~%bool TEMP_button~%bool MAG_button~%bool WATER_button~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'motors)))
  "Returns full string definition for message of type 'motors"
  (cl:format cl:nil "int64 motorA~%int64 motorB~%int64 motorC~%int64 motorD~%int64 motorE~%int64 motorF~%bool PH_button~%bool TEMP_button~%bool MAG_button~%bool WATER_button~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <motors>))
  (cl:+ 0
     8
     8
     8
     8
     8
     8
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <motors>))
  "Converts a ROS message object to a list"
  (cl:list 'motors
    (cl:cons ':motorA (motorA msg))
    (cl:cons ':motorB (motorB msg))
    (cl:cons ':motorC (motorC msg))
    (cl:cons ':motorD (motorD msg))
    (cl:cons ':motorE (motorE msg))
    (cl:cons ':motorF (motorF msg))
    (cl:cons ':PH_button (PH_button msg))
    (cl:cons ':TEMP_button (TEMP_button msg))
    (cl:cons ':MAG_button (MAG_button msg))
    (cl:cons ':WATER_button (WATER_button msg))
))
