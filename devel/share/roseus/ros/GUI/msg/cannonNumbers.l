;; Auto-generated. Do not edit!


(when (boundp 'GUI::cannonNumbers)
  (if (not (find-package "GUI"))
    (make-package "GUI"))
  (shadow 'cannonNumbers (find-package "GUI")))
(unless (find-package "GUI::CANNONNUMBERS")
  (make-package "GUI::CANNONNUMBERS"))

(in-package "ROS")
;;//! \htmlinclude cannonNumbers.msg.html


(defclass GUI::cannonNumbers
  :super ros::object
  :slots (_r1 _r2 _r3 _l _vol _weight ))

(defmethod GUI::cannonNumbers
  (:init
   (&key
    ((:r1 __r1) 0.0)
    ((:r2 __r2) 0.0)
    ((:r3 __r3) 0.0)
    ((:l __l) 0.0)
    ((:vol __vol) 0.0)
    ((:weight __weight) 0.0)
    )
   (send-super :init)
   (setq _r1 (float __r1))
   (setq _r2 (float __r2))
   (setq _r3 (float __r3))
   (setq _l (float __l))
   (setq _vol (float __vol))
   (setq _weight (float __weight))
   self)
  (:r1
   (&optional __r1)
   (if __r1 (setq _r1 __r1)) _r1)
  (:r2
   (&optional __r2)
   (if __r2 (setq _r2 __r2)) _r2)
  (:r3
   (&optional __r3)
   (if __r3 (setq _r3 __r3)) _r3)
  (:l
   (&optional __l)
   (if __l (setq _l __l)) _l)
  (:vol
   (&optional __vol)
   (if __vol (setq _vol __vol)) _vol)
  (:weight
   (&optional __weight)
   (if __weight (setq _weight __weight)) _weight)
  (:serialization-length
   ()
   (+
    ;; float64 _r1
    8
    ;; float64 _r2
    8
    ;; float64 _r3
    8
    ;; float64 _l
    8
    ;; float64 _vol
    8
    ;; float64 _weight
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _r1
       (sys::poke _r1 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _r2
       (sys::poke _r2 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _r3
       (sys::poke _r3 (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _l
       (sys::poke _l (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _vol
       (sys::poke _vol (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _weight
       (sys::poke _weight (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _r1
     (setq _r1 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _r2
     (setq _r2 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _r3
     (setq _r3 (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _l
     (setq _l (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _vol
     (setq _vol (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _weight
     (setq _weight (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get GUI::cannonNumbers :md5sum-) "b96d3a629a34dfd2040e80b4afc99711")
(setf (get GUI::cannonNumbers :datatype-) "GUI/cannonNumbers")
(setf (get GUI::cannonNumbers :definition-)
      "float64 r1
float64 r2
float64 r3
float64 l
float64 vol
float64 weight

")



(provide :GUI/cannonNumbers "b96d3a629a34dfd2040e80b4afc99711")


