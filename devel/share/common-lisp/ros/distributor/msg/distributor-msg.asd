
(cl:in-package :asdf)

(defsystem "distributor-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "rov_msgs" :depends-on ("_package_rov_msgs"))
    (:file "_package_rov_msgs" :depends-on ("_package"))
  ))