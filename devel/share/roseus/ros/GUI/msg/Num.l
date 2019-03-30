;; Auto-generated. Do not edit!


(when (boundp 'GUI::Num)
  (if (not (find-package "GUI"))
    (make-package "GUI"))
  (shadow 'Num (find-package "GUI")))
(unless (find-package "GUI::NUM")
  (make-package "GUI::NUM"))

(in-package "ROS")
;;//! \htmlinclude Num.msg.html


(defclass GUI::Num
  :super ros::object
  :slots (_circlesNo _trianglesNo _linesNo _squaresNo ))

(defmethod GUI::Num
  (:init
   (&key
    ((:circlesNo __circlesNo) 0)
    ((:trianglesNo __trianglesNo) 0)
    ((:linesNo __linesNo) 0)
    ((:squaresNo __squaresNo) 0)
    )
   (send-super :init)
   (setq _circlesNo (round __circlesNo))
   (setq _trianglesNo (round __trianglesNo))
   (setq _linesNo (round __linesNo))
   (setq _squaresNo (round __squaresNo))
   self)
  (:circlesNo
   (&optional __circlesNo)
   (if __circlesNo (setq _circlesNo __circlesNo)) _circlesNo)
  (:trianglesNo
   (&optional __trianglesNo)
   (if __trianglesNo (setq _trianglesNo __trianglesNo)) _trianglesNo)
  (:linesNo
   (&optional __linesNo)
   (if __linesNo (setq _linesNo __linesNo)) _linesNo)
  (:squaresNo
   (&optional __squaresNo)
   (if __squaresNo (setq _squaresNo __squaresNo)) _squaresNo)
  (:serialization-length
   ()
   (+
    ;; int64 _circlesNo
    8
    ;; int64 _trianglesNo
    8
    ;; int64 _linesNo
    8
    ;; int64 _squaresNo
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _circlesNo
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _circlesNo (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _circlesNo) (= (length (_circlesNo . bv)) 2)) ;; bignum
              (write-long (ash (elt (_circlesNo . bv) 0) 0) s)
              (write-long (ash (elt (_circlesNo . bv) 1) -1) s))
             ((and (class _circlesNo) (= (length (_circlesNo . bv)) 1)) ;; big1
              (write-long (elt (_circlesNo . bv) 0) s)
              (write-long (if (>= _circlesNo 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _circlesNo s)(write-long (if (>= _circlesNo 0) 0 #xffffffff) s)))
     ;; int64 _trianglesNo
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _trianglesNo (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _trianglesNo) (= (length (_trianglesNo . bv)) 2)) ;; bignum
              (write-long (ash (elt (_trianglesNo . bv) 0) 0) s)
              (write-long (ash (elt (_trianglesNo . bv) 1) -1) s))
             ((and (class _trianglesNo) (= (length (_trianglesNo . bv)) 1)) ;; big1
              (write-long (elt (_trianglesNo . bv) 0) s)
              (write-long (if (>= _trianglesNo 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _trianglesNo s)(write-long (if (>= _trianglesNo 0) 0 #xffffffff) s)))
     ;; int64 _linesNo
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _linesNo (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _linesNo) (= (length (_linesNo . bv)) 2)) ;; bignum
              (write-long (ash (elt (_linesNo . bv) 0) 0) s)
              (write-long (ash (elt (_linesNo . bv) 1) -1) s))
             ((and (class _linesNo) (= (length (_linesNo . bv)) 1)) ;; big1
              (write-long (elt (_linesNo . bv) 0) s)
              (write-long (if (>= _linesNo 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _linesNo s)(write-long (if (>= _linesNo 0) 0 #xffffffff) s)))
     ;; int64 _squaresNo
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _squaresNo (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _squaresNo) (= (length (_squaresNo . bv)) 2)) ;; bignum
              (write-long (ash (elt (_squaresNo . bv) 0) 0) s)
              (write-long (ash (elt (_squaresNo . bv) 1) -1) s))
             ((and (class _squaresNo) (= (length (_squaresNo . bv)) 1)) ;; big1
              (write-long (elt (_squaresNo . bv) 0) s)
              (write-long (if (>= _squaresNo 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _squaresNo s)(write-long (if (>= _squaresNo 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _circlesNo
#+(or :alpha :irix6 :x86_64)
      (setf _circlesNo (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _circlesNo (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _trianglesNo
#+(or :alpha :irix6 :x86_64)
      (setf _trianglesNo (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _trianglesNo (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _linesNo
#+(or :alpha :irix6 :x86_64)
      (setf _linesNo (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _linesNo (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _squaresNo
#+(or :alpha :irix6 :x86_64)
      (setf _squaresNo (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _squaresNo (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get GUI::Num :md5sum-) "cc4fa4ab5eb670e25a1c738431aed253")
(setf (get GUI::Num :datatype-) "GUI/Num")
(setf (get GUI::Num :definition-)
      "int64 circlesNo
int64 trianglesNo
int64 linesNo
int64 squaresNo

")



(provide :GUI/Num "cc4fa4ab5eb670e25a1c738431aed253")


