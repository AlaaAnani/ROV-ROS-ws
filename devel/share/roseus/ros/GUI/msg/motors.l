;; Auto-generated. Do not edit!


(when (boundp 'GUI::motors)
  (if (not (find-package "GUI"))
    (make-package "GUI"))
  (shadow 'motors (find-package "GUI")))
(unless (find-package "GUI::MOTORS")
  (make-package "GUI::MOTORS"))

(in-package "ROS")
;;//! \htmlinclude motors.msg.html


(defclass GUI::motors
  :super ros::object
  :slots (_motorA _motorB _motorC _motorD _motorE _motorF _PH_button _TEMP_button _MAG_button _WATER_button ))

(defmethod GUI::motors
  (:init
   (&key
    ((:motorA __motorA) 0)
    ((:motorB __motorB) 0)
    ((:motorC __motorC) 0)
    ((:motorD __motorD) 0)
    ((:motorE __motorE) 0)
    ((:motorF __motorF) 0)
    ((:PH_button __PH_button) nil)
    ((:TEMP_button __TEMP_button) nil)
    ((:MAG_button __MAG_button) nil)
    ((:WATER_button __WATER_button) nil)
    )
   (send-super :init)
   (setq _motorA (round __motorA))
   (setq _motorB (round __motorB))
   (setq _motorC (round __motorC))
   (setq _motorD (round __motorD))
   (setq _motorE (round __motorE))
   (setq _motorF (round __motorF))
   (setq _PH_button __PH_button)
   (setq _TEMP_button __TEMP_button)
   (setq _MAG_button __MAG_button)
   (setq _WATER_button __WATER_button)
   self)
  (:motorA
   (&optional __motorA)
   (if __motorA (setq _motorA __motorA)) _motorA)
  (:motorB
   (&optional __motorB)
   (if __motorB (setq _motorB __motorB)) _motorB)
  (:motorC
   (&optional __motorC)
   (if __motorC (setq _motorC __motorC)) _motorC)
  (:motorD
   (&optional __motorD)
   (if __motorD (setq _motorD __motorD)) _motorD)
  (:motorE
   (&optional __motorE)
   (if __motorE (setq _motorE __motorE)) _motorE)
  (:motorF
   (&optional __motorF)
   (if __motorF (setq _motorF __motorF)) _motorF)
  (:PH_button
   (&optional __PH_button)
   (if __PH_button (setq _PH_button __PH_button)) _PH_button)
  (:TEMP_button
   (&optional __TEMP_button)
   (if __TEMP_button (setq _TEMP_button __TEMP_button)) _TEMP_button)
  (:MAG_button
   (&optional __MAG_button)
   (if __MAG_button (setq _MAG_button __MAG_button)) _MAG_button)
  (:WATER_button
   (&optional __WATER_button)
   (if __WATER_button (setq _WATER_button __WATER_button)) _WATER_button)
  (:serialization-length
   ()
   (+
    ;; int64 _motorA
    8
    ;; int64 _motorB
    8
    ;; int64 _motorC
    8
    ;; int64 _motorD
    8
    ;; int64 _motorE
    8
    ;; int64 _motorF
    8
    ;; bool _PH_button
    1
    ;; bool _TEMP_button
    1
    ;; bool _MAG_button
    1
    ;; bool _WATER_button
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _motorA
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _motorA (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _motorA) (= (length (_motorA . bv)) 2)) ;; bignum
              (write-long (ash (elt (_motorA . bv) 0) 0) s)
              (write-long (ash (elt (_motorA . bv) 1) -1) s))
             ((and (class _motorA) (= (length (_motorA . bv)) 1)) ;; big1
              (write-long (elt (_motorA . bv) 0) s)
              (write-long (if (>= _motorA 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _motorA s)(write-long (if (>= _motorA 0) 0 #xffffffff) s)))
     ;; int64 _motorB
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _motorB (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _motorB) (= (length (_motorB . bv)) 2)) ;; bignum
              (write-long (ash (elt (_motorB . bv) 0) 0) s)
              (write-long (ash (elt (_motorB . bv) 1) -1) s))
             ((and (class _motorB) (= (length (_motorB . bv)) 1)) ;; big1
              (write-long (elt (_motorB . bv) 0) s)
              (write-long (if (>= _motorB 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _motorB s)(write-long (if (>= _motorB 0) 0 #xffffffff) s)))
     ;; int64 _motorC
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _motorC (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _motorC) (= (length (_motorC . bv)) 2)) ;; bignum
              (write-long (ash (elt (_motorC . bv) 0) 0) s)
              (write-long (ash (elt (_motorC . bv) 1) -1) s))
             ((and (class _motorC) (= (length (_motorC . bv)) 1)) ;; big1
              (write-long (elt (_motorC . bv) 0) s)
              (write-long (if (>= _motorC 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _motorC s)(write-long (if (>= _motorC 0) 0 #xffffffff) s)))
     ;; int64 _motorD
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _motorD (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _motorD) (= (length (_motorD . bv)) 2)) ;; bignum
              (write-long (ash (elt (_motorD . bv) 0) 0) s)
              (write-long (ash (elt (_motorD . bv) 1) -1) s))
             ((and (class _motorD) (= (length (_motorD . bv)) 1)) ;; big1
              (write-long (elt (_motorD . bv) 0) s)
              (write-long (if (>= _motorD 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _motorD s)(write-long (if (>= _motorD 0) 0 #xffffffff) s)))
     ;; int64 _motorE
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _motorE (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _motorE) (= (length (_motorE . bv)) 2)) ;; bignum
              (write-long (ash (elt (_motorE . bv) 0) 0) s)
              (write-long (ash (elt (_motorE . bv) 1) -1) s))
             ((and (class _motorE) (= (length (_motorE . bv)) 1)) ;; big1
              (write-long (elt (_motorE . bv) 0) s)
              (write-long (if (>= _motorE 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _motorE s)(write-long (if (>= _motorE 0) 0 #xffffffff) s)))
     ;; int64 _motorF
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _motorF (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _motorF) (= (length (_motorF . bv)) 2)) ;; bignum
              (write-long (ash (elt (_motorF . bv) 0) 0) s)
              (write-long (ash (elt (_motorF . bv) 1) -1) s))
             ((and (class _motorF) (= (length (_motorF . bv)) 1)) ;; big1
              (write-long (elt (_motorF . bv) 0) s)
              (write-long (if (>= _motorF 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _motorF s)(write-long (if (>= _motorF 0) 0 #xffffffff) s)))
     ;; bool _PH_button
       (if _PH_button (write-byte -1 s) (write-byte 0 s))
     ;; bool _TEMP_button
       (if _TEMP_button (write-byte -1 s) (write-byte 0 s))
     ;; bool _MAG_button
       (if _MAG_button (write-byte -1 s) (write-byte 0 s))
     ;; bool _WATER_button
       (if _WATER_button (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _motorA
#+(or :alpha :irix6 :x86_64)
      (setf _motorA (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _motorA (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _motorB
#+(or :alpha :irix6 :x86_64)
      (setf _motorB (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _motorB (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _motorC
#+(or :alpha :irix6 :x86_64)
      (setf _motorC (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _motorC (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _motorD
#+(or :alpha :irix6 :x86_64)
      (setf _motorD (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _motorD (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _motorE
#+(or :alpha :irix6 :x86_64)
      (setf _motorE (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _motorE (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _motorF
#+(or :alpha :irix6 :x86_64)
      (setf _motorF (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _motorF (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; bool _PH_button
     (setq _PH_button (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _TEMP_button
     (setq _TEMP_button (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _MAG_button
     (setq _MAG_button (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _WATER_button
     (setq _WATER_button (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get GUI::motors :md5sum-) "217166abeed0122de3610215eeb90349")
(setf (get GUI::motors :datatype-) "GUI/motors")
(setf (get GUI::motors :definition-)
      "int64 motorA
int64 motorB
int64 motorC
int64 motorD
int64 motorE
int64 motorF
bool PH_button
bool TEMP_button
bool MAG_button
bool WATER_button

")



(provide :GUI/motors "217166abeed0122de3610215eeb90349")


