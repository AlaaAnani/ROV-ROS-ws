
(cl:in-package :asdf)

(defsystem "motion_map-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "motors" :depends-on ("_package_motors"))
    (:file "_package_motors" :depends-on ("_package"))
  ))