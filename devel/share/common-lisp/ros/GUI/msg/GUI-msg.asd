
(cl:in-package :asdf)

(defsystem "GUI-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
    (:file "cannonNumbers" :depends-on ("_package_cannonNumbers"))
    (:file "_package_cannonNumbers" :depends-on ("_package"))
    (:file "motors" :depends-on ("_package_motors"))
    (:file "_package_motors" :depends-on ("_package"))
  ))