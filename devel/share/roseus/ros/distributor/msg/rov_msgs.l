;; Auto-generated. Do not edit!


(when (boundp 'distributor::rov_msgs)
  (if (not (find-package "DISTRIBUTOR"))
    (make-package "DISTRIBUTOR"))
  (shadow 'rov_msgs (find-package "DISTRIBUTOR")))
(unless (find-package "DISTRIBUTOR::ROV_MSGS")
  (make-package "DISTRIBUTOR::ROV_MSGS"))

(in-package "ROS")
;;//! \htmlinclude rov_msgs.msg.html


(defclass distributor::rov_msgs
  :super ros::object
  :slots (_pitch _roll _yaw _acc_x _acc_y _acc_z _gyro_x _gyro_y _gyro_z _paro _PH _water _temp _mag1 _mag2 _mag3 ))

(defmethod distributor::rov_msgs
  (:init
   (&key
    ((:pitch __pitch) 0.0)
    ((:roll __roll) 0.0)
    ((:yaw __yaw) 0.0)
    ((:acc_x __acc_x) 0.0)
    ((:acc_y __acc_y) 0.0)
    ((:acc_z __acc_z) 0.0)
    ((:gyro_x __gyro_x) 0.0)
    ((:gyro_y __gyro_y) 0.0)
    ((:gyro_z __gyro_z) 0.0)
    ((:paro __paro) 0.0)
    ((:PH __PH) 0.0)
    ((:water __water) 0.0)
    ((:temp __temp) 0.0)
    ((:mag1 __mag1) 0.0)
    ((:mag2 __mag2) 0.0)
    ((:mag3 __mag3) 0.0)
    )
   (send-super :init)
   (setq _pitch (float __pitch))
   (setq _roll (float __roll))
   (setq _yaw (float __yaw))
   (setq _acc_x (float __acc_x))
   (setq _acc_y (float __acc_y))
   (setq _acc_z (float __acc_z))
   (setq _gyro_x (float __gyro_x))
   (setq _gyro_y (float __gyro_y))
   (setq _gyro_z (float __gyro_z))
   (setq _paro (float __paro))
   (setq _PH (float __PH))
   (setq _water (float __water))
   (setq _temp (float __temp))
   (setq _mag1 (float __mag1))
   (setq _mag2 (float __mag2))
   (setq _mag3 (float __mag3))
   self)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:acc_x
   (&optional __acc_x)
   (if __acc_x (setq _acc_x __acc_x)) _acc_x)
  (:acc_y
   (&optional __acc_y)
   (if __acc_y (setq _acc_y __acc_y)) _acc_y)
  (:acc_z
   (&optional __acc_z)
   (if __acc_z (setq _acc_z __acc_z)) _acc_z)
  (:gyro_x
   (&optional __gyro_x)
   (if __gyro_x (setq _gyro_x __gyro_x)) _gyro_x)
  (:gyro_y
   (&optional __gyro_y)
   (if __gyro_y (setq _gyro_y __gyro_y)) _gyro_y)
  (:gyro_z
   (&optional __gyro_z)
   (if __gyro_z (setq _gyro_z __gyro_z)) _gyro_z)
  (:paro
   (&optional __paro)
   (if __paro (setq _paro __paro)) _paro)
  (:PH
   (&optional __PH)
   (if __PH (setq _PH __PH)) _PH)
  (:water
   (&optional __water)
   (if __water (setq _water __water)) _water)
  (:temp
   (&optional __temp)
   (if __temp (setq _temp __temp)) _temp)
  (:mag1
   (&optional __mag1)
   (if __mag1 (setq _mag1 __mag1)) _mag1)
  (:mag2
   (&optional __mag2)
   (if __mag2 (setq _mag2 __mag2)) _mag2)
  (:mag3
   (&optional __mag3)
   (if __mag3 (setq _mag3 __mag3)) _mag3)
  (:serialization-length
   ()
   (+
    ;; float64 _pitch
    8
    ;; float64 _roll
    8
    ;; float64 _yaw
    8
    ;; float64 _acc_x
    8
    ;; float64 _acc_y
    8
    ;; float64 _acc_z
    8
    ;; float64 _gyro_x
    8
    ;; float64 _gyro_y
    8
    ;; float64 _gyro_z
    8
    ;; float64 _paro
    8
    ;; float64 _PH
    8
    ;; float64 _water
    8
    ;; float64 _temp
    8
    ;; float64 _mag1
    8
    ;; float64 _mag2
    8
    ;; float64 _mag3
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _acc_x
       (sys::poke _acc_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _acc_y
       (sys::poke _acc_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _acc_z
       (sys::poke _acc_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gyro_x
       (sys::poke _gyro_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gyro_y
       (sys::poke _gyro_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gyro_z
       (sys::poke _gyro_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _paro
       (sys::poke _paro (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _PH
       (sys::poke _PH (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _water
       (sys::poke _water (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _temp
       (sys::poke _temp (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _mag1
       (sys::poke _mag1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _mag2
       (sys::poke _mag2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _mag3
       (sys::poke _mag3 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _pitch
     (setq _pitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _roll
     (setq _roll (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _acc_x
     (setq _acc_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _acc_y
     (setq _acc_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _acc_z
     (setq _acc_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gyro_x
     (setq _gyro_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gyro_y
     (setq _gyro_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gyro_z
     (setq _gyro_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _paro
     (setq _paro (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _PH
     (setq _PH (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _water
     (setq _water (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _temp
     (setq _temp (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _mag1
     (setq _mag1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _mag2
     (setq _mag2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _mag3
     (setq _mag3 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get distributor::rov_msgs :md5sum-) "580798bc75b1af001886c0456174d658")
(setf (get distributor::rov_msgs :datatype-) "distributor/rov_msgs")
(setf (get distributor::rov_msgs :definition-)
      "float64 pitch
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
")



(provide :distributor/rov_msgs "580798bc75b1af001886c0456174d658")


