# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_ui_form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1149, 723)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Qtab = QtGui.QTabWidget(Form)
        self.Qtab.setObjectName(_fromUtf8("Qtab"))
        self.MainTab = QtGui.QWidget()
        self.MainTab.setObjectName(_fromUtf8("MainTab"))
        self.splitter_23 = QtGui.QSplitter(self.MainTab)
        self.splitter_23.setGeometry(QtCore.QRect(9, 9, 228, 218))
        self.splitter_23.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_23.setObjectName(_fromUtf8("splitter_23"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_23)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.Yaw_label = QtGui.QLabel(self.splitter_2)
        self.Yaw_label.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Yaw_label.setObjectName(_fromUtf8("Yaw_label"))
        self.Pitch_label = QtGui.QLabel(self.splitter_2)
        self.Pitch_label.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Pitch_label.setObjectName(_fromUtf8("Pitch_label"))
        self.Roll_label = QtGui.QLabel(self.splitter_2)
        self.Roll_label.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Roll_label.setObjectName(_fromUtf8("Roll_label"))
        self.splitter = QtGui.QSplitter(self.splitter_23)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.Yaw_value = QtGui.QTextBrowser(self.splitter)
        self.Yaw_value.setObjectName(_fromUtf8("Yaw_value"))
        self.Pitch = QtGui.QTextBrowser(self.splitter)
        self.Pitch.setObjectName(_fromUtf8("Pitch"))
        self.Roll = QtGui.QTextBrowser(self.splitter)
        self.Roll.setStyleSheet(_fromUtf8("body {\n"
"  color: red;\n"
"}\n"
"\n"
"h1 {\n"
"  color: #00ff00;\n"
"}\n"
"\n"
"p.ex {\n"
"  color: rgb(0,0,255);\n"
"}"))
        self.Roll.setObjectName(_fromUtf8("Roll"))
        self.splitter_7 = QtGui.QSplitter(self.MainTab)
        self.splitter_7.setGeometry(QtCore.QRect(9, 566, 228, 99))
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName(_fromUtf8("splitter_7"))
        self.Temp_sens_label_4 = QtGui.QLabel(self.splitter_7)
        self.Temp_sens_label_4.setStyleSheet(_fromUtf8("background-color: rgb(117, 80, 123);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Temp_sens_label_4.setObjectName(_fromUtf8("Temp_sens_label_4"))
        self.splitter_6 = QtGui.QSplitter(self.splitter_7)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.Magnet1 = QtGui.QTextBrowser(self.splitter_6)
        self.Magnet1.setStyleSheet(_fromUtf8("body {\n"
"  color: red;\n"
"}\n"
"\n"
"h1 {\n"
"  color: #00ff00;\n"
"}\n"
"\n"
"p.ex {\n"
"  color: rgb(0,0,255);\n"
"}"))
        self.Magnet1.setObjectName(_fromUtf8("Magnet1"))
        self.Magnet2 = QtGui.QTextBrowser(self.splitter_6)
        self.Magnet2.setStyleSheet(_fromUtf8("body {\n"
"  color: red;\n"
"}\n"
"\n"
"h1 {\n"
"  color: #00ff00;\n"
"}\n"
"\n"
"p.ex {\n"
"  color: rgb(0,0,255);\n"
"}"))
        self.Magnet2.setObjectName(_fromUtf8("Magnet2"))
        self.Magnet3 = QtGui.QTextBrowser(self.splitter_6)
        self.Magnet3.setStyleSheet(_fromUtf8("body {\n"
"  color: red;\n"
"}\n"
"\n"
"h1 {\n"
"  color: #00ff00;\n"
"}\n"
"\n"
"p.ex {\n"
"  color: rgb(0,0,255);\n"
"}"))
        self.Magnet3.setObjectName(_fromUtf8("Magnet3"))
        self.splitter_27 = QtGui.QSplitter(self.MainTab)
        self.splitter_27.setGeometry(QtCore.QRect(9, 338, 228, 146))
        self.splitter_27.setOrientation(QtCore.Qt.Vertical)
        self.splitter_27.setObjectName(_fromUtf8("splitter_27"))
        self.splitter_24 = QtGui.QSplitter(self.splitter_27)
        self.splitter_24.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_24.setObjectName(_fromUtf8("splitter_24"))
        self.splitter_4 = QtGui.QSplitter(self.splitter_24)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.Temp_sens_label = QtGui.QLabel(self.splitter_4)
        self.Temp_sens_label.setStyleSheet(_fromUtf8("background-color: rgb(117, 80, 123);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Temp_sens_label.setObjectName(_fromUtf8("Temp_sens_label"))
        self.Temp_value = QtGui.QTextBrowser(self.splitter_4)
        self.Temp_value.setStyleSheet(_fromUtf8("body {\n"
"  color: red;\n"
"}\n"
"\n"
"h1 {\n"
"  color: #00ff00;\n"
"}\n"
"\n"
"p.ex {\n"
"  color: rgb(0,0,255);\n"
"}"))
        self.Temp_value.setObjectName(_fromUtf8("Temp_value"))
        self.unit_label_8 = QtGui.QLabel(self.splitter_24)
        self.unit_label_8.setStyleSheet(_fromUtf8("background-color: rgb(115, 210, 22);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.unit_label_8.setObjectName(_fromUtf8("unit_label_8"))
        self.splitter_26 = QtGui.QSplitter(self.splitter_27)
        self.splitter_26.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_26.setObjectName(_fromUtf8("splitter_26"))
        self.Temp_sens_label_2 = QtGui.QLabel(self.splitter_26)
        self.Temp_sens_label_2.setStyleSheet(_fromUtf8("background-color: rgb(117, 80, 123);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Temp_sens_label_2.setObjectName(_fromUtf8("Temp_sens_label_2"))
        self.Water_sens = QtGui.QTextBrowser(self.splitter_26)
        self.Water_sens.setStyleSheet(_fromUtf8("body {\n"
"  color: red;\n"
"}\n"
"\n"
"h1 {\n"
"  color: #00ff00;\n"
"}\n"
"\n"
"p.ex {\n"
"  color: rgb(0,0,255);\n"
"}"))
        self.Water_sens.setObjectName(_fromUtf8("Water_sens"))
        self.splitter_8 = QtGui.QSplitter(self.MainTab)
        self.splitter_8.setGeometry(QtCore.QRect(243, 233, 875, 99))
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName(_fromUtf8("splitter_8"))
        self.splitter_9 = QtGui.QSplitter(self.splitter_8)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName(_fromUtf8("splitter_9"))
        self.Joy_values_label_8 = QtGui.QLabel(self.splitter_9)
        self.Joy_values_label_8.setStyleSheet(_fromUtf8("background-color: rgb(239, 41, 41);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label_8.setObjectName(_fromUtf8("Joy_values_label_8"))
        self.Joy_values_label_9 = QtGui.QLabel(self.splitter_9)
        self.Joy_values_label_9.setStyleSheet(_fromUtf8("background-color: rgb(239, 41, 41);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";\n"
""))
        self.Joy_values_label_9.setObjectName(_fromUtf8("Joy_values_label_9"))
        self.Joy_values_label_10 = QtGui.QLabel(self.splitter_9)
        self.Joy_values_label_10.setStyleSheet(_fromUtf8("background-color: rgb(239, 41, 41);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label_10.setObjectName(_fromUtf8("Joy_values_label_10"))
        self.Joy_values_label_11 = QtGui.QLabel(self.splitter_9)
        self.Joy_values_label_11.setStyleSheet(_fromUtf8("background-color: rgb(239, 41, 41);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";\n"
""))
        self.Joy_values_label_11.setObjectName(_fromUtf8("Joy_values_label_11"))
        self.Joy_values_label_12 = QtGui.QLabel(self.splitter_9)
        self.Joy_values_label_12.setStyleSheet(_fromUtf8("background-color: rgb(239, 41, 41);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label_12.setObjectName(_fromUtf8("Joy_values_label_12"))
        self.Joy_values_label_13 = QtGui.QLabel(self.splitter_9)
        self.Joy_values_label_13.setStyleSheet(_fromUtf8("background-color: rgb(239, 41, 41);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";\n"
""))
        self.Joy_values_label_13.setObjectName(_fromUtf8("Joy_values_label_13"))
        self.splitter_11 = QtGui.QSplitter(self.splitter_8)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName(_fromUtf8("splitter_11"))
        self.MotorCurr1 = QtGui.QTextBrowser(self.splitter_11)
        self.MotorCurr1.setObjectName(_fromUtf8("MotorCurr1"))
        self.MotorCurr2 = QtGui.QTextBrowser(self.splitter_11)
        self.MotorCurr2.setObjectName(_fromUtf8("MotorCurr2"))
        self.MotorCurr3 = QtGui.QTextBrowser(self.splitter_11)
        self.MotorCurr3.setObjectName(_fromUtf8("MotorCurr3"))
        self.MotorCurr4 = QtGui.QTextBrowser(self.splitter_11)
        self.MotorCurr4.setObjectName(_fromUtf8("MotorCurr4"))
        self.MotorCurr5 = QtGui.QTextBrowser(self.splitter_11)
        self.MotorCurr5.setObjectName(_fromUtf8("MotorCurr5"))
        self.MotorCurr6 = QtGui.QTextBrowser(self.splitter_11)
        self.MotorCurr6.setObjectName(_fromUtf8("MotorCurr6"))
        self.splitter_13 = QtGui.QSplitter(self.MainTab)
        self.splitter_13.setGeometry(QtCore.QRect(243, 40, 871, 25))
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName(_fromUtf8("splitter_13"))
        self.Joy_values_label_14 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_14.setStyleSheet(_fromUtf8("background-color: rgb(38, 95, 122);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label_14.setObjectName(_fromUtf8("Joy_values_label_14"))
        self.Joy_values_label_15 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_15.setStyleSheet(_fromUtf8("background-color: rgb(38, 95, 122);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label_15.setObjectName(_fromUtf8("Joy_values_label_15"))
        self.Joy_values_label_16 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_16.setStyleSheet(_fromUtf8("background-color: rgb(38, 95, 122);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label_16.setObjectName(_fromUtf8("Joy_values_label_16"))
        self.Joy_values_label_17 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_17.setStyleSheet(_fromUtf8("background-color: rgb(38, 95, 122);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label_17.setObjectName(_fromUtf8("Joy_values_label_17"))
        self.Joy_values_label_18 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_18.setStyleSheet(_fromUtf8("background-color: rgb(38, 95, 122);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label_18.setObjectName(_fromUtf8("Joy_values_label_18"))
        self.Joy_values_label_19 = QtGui.QLabel(self.splitter_13)
        self.Joy_values_label_19.setStyleSheet(_fromUtf8("background-color: rgb(38, 95, 122);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label_19.setObjectName(_fromUtf8("Joy_values_label_19"))
        self.Current_sens_label = QtGui.QLabel(self.MainTab)
        self.Current_sens_label.setGeometry(QtCore.QRect(243, 202, 162, 25))
        self.Current_sens_label.setStyleSheet(_fromUtf8("background-color: rgb(136, 138, 133);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Current_sens_label.setObjectName(_fromUtf8("Current_sens_label"))
        self.Joy_values_label = QtGui.QLabel(self.MainTab)
        self.Joy_values_label.setGeometry(QtCore.QRect(243, 9, 114, 25))
        self.Joy_values_label.setStyleSheet(_fromUtf8("background-color: rgb(136, 138, 133);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Joy_values_label.setObjectName(_fromUtf8("Joy_values_label"))
        self.splitter_3 = QtGui.QSplitter(self.MainTab)
        self.splitter_3.setGeometry(QtCore.QRect(9, 233, 228, 99))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.PH_label = QtGui.QLabel(self.splitter_3)
        self.PH_label.setStyleSheet(_fromUtf8("background-color: rgb(239, 41, 41);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.PH_label.setObjectName(_fromUtf8("PH_label"))
        self.PHvalue = QtGui.QTextBrowser(self.splitter_3)
        self.PHvalue.setStyleSheet(_fromUtf8("body {\n"
"  color: red;\n"
"}\n"
"\n"
"h1 {\n"
"  color: #00ff00;\n"
"}\n"
"\n"
"p.ex {\n"
"  color: rgb(0,0,255);\n"
"}"))
        self.PHvalue.setObjectName(_fromUtf8("PHvalue"))
        self.splitter_12 = QtGui.QSplitter(self.MainTab)
        self.splitter_12.setGeometry(QtCore.QRect(243, 71, 875, 71))
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName(_fromUtf8("splitter_12"))
        self.MotorValue1 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue1.setObjectName(_fromUtf8("MotorValue1"))
        self.MotorValue2 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue2.setObjectName(_fromUtf8("MotorValue2"))
        self.MotorValue3 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue3.setObjectName(_fromUtf8("MotorValue3"))
        self.MotorValue4 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue4.setObjectName(_fromUtf8("MotorValue4"))
        self.MotorValue5 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue5.setObjectName(_fromUtf8("MotorValue5"))
        self.MotorValue6 = QtGui.QTextBrowser(self.splitter_12)
        self.MotorValue6.setObjectName(_fromUtf8("MotorValue6"))
        self.splitter_15 = QtGui.QSplitter(self.MainTab)
        self.splitter_15.setGeometry(QtCore.QRect(9, 490, 228, 70))
        self.splitter_15.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_15.setObjectName(_fromUtf8("splitter_15"))
        self.Temp_sens_label_3 = QtGui.QLabel(self.splitter_15)
        self.Temp_sens_label_3.setStyleSheet(_fromUtf8("background-color: rgb(117, 80, 123);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Temp_sens_label_3.setObjectName(_fromUtf8("Temp_sens_label_3"))
        self.Press_sens = QtGui.QTextBrowser(self.splitter_15)
        self.Press_sens.setStyleSheet(_fromUtf8("body {\n"
"  color: red;\n"
"}\n"
"\n"
"h1 {\n"
"  color: #00ff00;\n"
"}\n"
"\n"
"p.ex {\n"
"  color: rgb(0,0,255);\n"
"}"))
        self.Press_sens.setObjectName(_fromUtf8("Press_sens"))
        self.splitter_42 = QtGui.QSplitter(self.MainTab)
        self.splitter_42.setGeometry(QtCore.QRect(300, 390, 291, 101))
        self.splitter_42.setOrientation(QtCore.Qt.Vertical)
        self.splitter_42.setObjectName(_fromUtf8("splitter_42"))
        self.splitter_33 = QtGui.QSplitter(self.splitter_42)
        self.splitter_33.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_33.setObjectName(_fromUtf8("splitter_33"))
        self.cam_start_butt = QtGui.QPushButton(self.splitter_33)
        self.cam_start_butt.setStyleSheet(_fromUtf8("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.cam_start_butt.setObjectName(_fromUtf8("cam_start_butt"))
        self.cam_stop_butt = QtGui.QPushButton(self.splitter_33)
        self.cam_stop_butt.setStyleSheet(_fromUtf8("  background-color: rgb(239, 41, 41);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.cam_stop_butt.setObjectName(_fromUtf8("cam_stop_butt"))
        self.splitter_41 = QtGui.QSplitter(self.splitter_42)
        self.splitter_41.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_41.setObjectName(_fromUtf8("splitter_41"))
        self.Roll_label_2 = QtGui.QLabel(self.splitter_41)
        self.Roll_label_2.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Roll_label_2.setObjectName(_fromUtf8("Roll_label_2"))
        self.in_cam_index = QtGui.QLineEdit(self.splitter_41)
        self.in_cam_index.setObjectName(_fromUtf8("in_cam_index"))
        self.splitter_43 = QtGui.QSplitter(self.MainTab)
        self.splitter_43.setGeometry(QtCore.QRect(680, 390, 321, 71))
        self.splitter_43.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_43.setObjectName(_fromUtf8("splitter_43"))
        self.rov_start_butt = QtGui.QPushButton(self.splitter_43)
        self.rov_start_butt.setStyleSheet(_fromUtf8("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.rov_start_butt.setObjectName(_fromUtf8("rov_start_butt"))
        self.rov_stop_butt = QtGui.QPushButton(self.splitter_43)
        self.rov_stop_butt.setStyleSheet(_fromUtf8("  background-color: rgb(239, 41, 41);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.rov_stop_butt.setObjectName(_fromUtf8("rov_stop_butt"))
        self.splitter_46 = QtGui.QSplitter(self.MainTab)
        self.splitter_46.setGeometry(QtCore.QRect(680, 470, 321, 91))
        self.splitter_46.setOrientation(QtCore.Qt.Vertical)
        self.splitter_46.setObjectName(_fromUtf8("splitter_46"))
        self.splitter_45 = QtGui.QSplitter(self.splitter_46)
        self.splitter_45.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_45.setObjectName(_fromUtf8("splitter_45"))
        self.Roll_label_3 = QtGui.QLabel(self.splitter_45)
        self.Roll_label_3.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Roll_label_3.setObjectName(_fromUtf8("Roll_label_3"))
        self.in_com_port = QtGui.QLineEdit(self.splitter_45)
        self.in_com_port.setObjectName(_fromUtf8("in_com_port"))
        self.splitter_44 = QtGui.QSplitter(self.splitter_46)
        self.splitter_44.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_44.setObjectName(_fromUtf8("splitter_44"))
        self.Roll_label_4 = QtGui.QLabel(self.splitter_44)
        self.Roll_label_4.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"font: 75 15pt \"URW Bookman L\";"))
        self.Roll_label_4.setObjectName(_fromUtf8("Roll_label_4"))
        self.in_joy_port = QtGui.QLineEdit(self.splitter_44)
        self.in_joy_port.setObjectName(_fromUtf8("in_joy_port"))
        self.Qtab.addTab(self.MainTab, _fromUtf8(""))
        self.CannonMission = QtGui.QWidget()
        self.CannonMission.setObjectName(_fromUtf8("CannonMission"))
        self.gridLayout_4 = QtGui.QGridLayout(self.CannonMission)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.splitter_37 = QtGui.QSplitter(self.CannonMission)
        self.splitter_37.setOrientation(QtCore.Qt.Vertical)
        self.splitter_37.setObjectName(_fromUtf8("splitter_37"))
        self.splitter_36 = QtGui.QSplitter(self.splitter_37)
        self.splitter_36.setOrientation(QtCore.Qt.Vertical)
        self.splitter_36.setObjectName(_fromUtf8("splitter_36"))
        self.splitter_35 = QtGui.QSplitter(self.splitter_36)
        self.splitter_35.setOrientation(QtCore.Qt.Vertical)
        self.splitter_35.setObjectName(_fromUtf8("splitter_35"))
        self.splitter_34 = QtGui.QSplitter(self.splitter_35)
        self.splitter_34.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_34.setObjectName(_fromUtf8("splitter_34"))
        self.Canon_T_Label = QtGui.QLabel(self.splitter_34)
        self.Canon_T_Label.setStyleSheet(_fromUtf8("background-color: rgb(186, 189, 182);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Canon_T_Label.setObjectName(_fromUtf8("Canon_T_Label"))
        self.splitter_19 = QtGui.QSplitter(self.splitter_34)
        self.splitter_19.setOrientation(QtCore.Qt.Vertical)
        self.splitter_19.setObjectName(_fromUtf8("splitter_19"))
        self.AF_RB = QtGui.QRadioButton(self.splitter_19)
        self.AF_RB.setStyleSheet(_fromUtf8("background-color: rgb(138, 226, 52);"))
        self.AF_RB.setObjectName(_fromUtf8("AF_RB"))
        self.Else_RB = QtGui.QRadioButton(self.splitter_19)
        self.Else_RB.setStyleSheet(_fromUtf8("background-color: rgb(138, 226, 52);"))
        self.Else_RB.setObjectName(_fromUtf8("Else_RB"))
        self.Start_cannon = QtGui.QPushButton(self.splitter_35)
        self.Start_cannon.setStyleSheet(_fromUtf8("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Start_cannon.setObjectName(_fromUtf8("Start_cannon"))
        self.splitter_21 = QtGui.QSplitter(self.splitter_36)
        self.splitter_21.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_21.setObjectName(_fromUtf8("splitter_21"))
        self.splitter_17 = QtGui.QSplitter(self.splitter_21)
        self.splitter_17.setOrientation(QtCore.Qt.Vertical)
        self.splitter_17.setObjectName(_fromUtf8("splitter_17"))
        self.Radius1_Label = QtGui.QLabel(self.splitter_17)
        self.Radius1_Label.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Radius1_Label.setObjectName(_fromUtf8("Radius1_Label"))
        self.Radius2_Label = QtGui.QLabel(self.splitter_17)
        self.Radius2_Label.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Radius2_Label.setObjectName(_fromUtf8("Radius2_Label"))
        self.Radius3_Label = QtGui.QLabel(self.splitter_17)
        self.Radius3_Label.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Radius3_Label.setObjectName(_fromUtf8("Radius3_Label"))
        self.length_label = QtGui.QLabel(self.splitter_17)
        self.length_label.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.length_label.setObjectName(_fromUtf8("length_label"))
        self.Volume_label = QtGui.QLabel(self.splitter_17)
        self.Volume_label.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Volume_label.setObjectName(_fromUtf8("Volume_label"))
        self.Weight_label = QtGui.QLabel(self.splitter_17)
        self.Weight_label.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Weight_label.setObjectName(_fromUtf8("Weight_label"))
        self.splitter_18 = QtGui.QSplitter(self.splitter_21)
        self.splitter_18.setOrientation(QtCore.Qt.Vertical)
        self.splitter_18.setObjectName(_fromUtf8("splitter_18"))
        self.Radius1Value = QtGui.QTextBrowser(self.splitter_18)
        self.Radius1Value.setObjectName(_fromUtf8("Radius1Value"))
        self.Radius2Value = QtGui.QTextBrowser(self.splitter_18)
        self.Radius2Value.setObjectName(_fromUtf8("Radius2Value"))
        self.Radius3Value = QtGui.QTextBrowser(self.splitter_18)
        self.Radius3Value.setObjectName(_fromUtf8("Radius3Value"))
        self.Cannon_length_value = QtGui.QTextBrowser(self.splitter_18)
        self.Cannon_length_value.setObjectName(_fromUtf8("Cannon_length_value"))
        self.Cannon_volume_value = QtGui.QTextBrowser(self.splitter_18)
        self.Cannon_volume_value.setObjectName(_fromUtf8("Cannon_volume_value"))
        self.Canno_Weight_value = QtGui.QTextBrowser(self.splitter_18)
        self.Canno_Weight_value.setObjectName(_fromUtf8("Canno_Weight_value"))
        self.splitter_20 = QtGui.QSplitter(self.splitter_21)
        self.splitter_20.setOrientation(QtCore.Qt.Vertical)
        self.splitter_20.setObjectName(_fromUtf8("splitter_20"))
        self.unit_label_2 = QtGui.QLabel(self.splitter_20)
        self.unit_label_2.setStyleSheet(_fromUtf8("background-color: rgb(115, 210, 22);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.unit_label_2.setObjectName(_fromUtf8("unit_label_2"))
        self.unit_label_3 = QtGui.QLabel(self.splitter_20)
        self.unit_label_3.setStyleSheet(_fromUtf8("background-color: rgb(115, 210, 22);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.unit_label_3.setObjectName(_fromUtf8("unit_label_3"))
        self.unit_label_4 = QtGui.QLabel(self.splitter_20)
        self.unit_label_4.setStyleSheet(_fromUtf8("background-color: rgb(115, 210, 22);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.unit_label_4.setObjectName(_fromUtf8("unit_label_4"))
        self.unit_label_6 = QtGui.QLabel(self.splitter_20)
        self.unit_label_6.setStyleSheet(_fromUtf8("background-color: rgb(115, 210, 22);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.unit_label_6.setObjectName(_fromUtf8("unit_label_6"))
        self.unit_label_5 = QtGui.QLabel(self.splitter_20)
        self.unit_label_5.setStyleSheet(_fromUtf8("background-color: rgb(115, 210, 22);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.unit_label_5.setObjectName(_fromUtf8("unit_label_5"))
        self.unit_label_7 = QtGui.QLabel(self.splitter_20)
        self.unit_label_7.setStyleSheet(_fromUtf8("background-color: rgb(115, 210, 22);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.unit_label_7.setObjectName(_fromUtf8("unit_label_7"))
        self.Terminate_Cannon_button = QtGui.QPushButton(self.splitter_37)
        self.Terminate_Cannon_button.setStyleSheet(_fromUtf8("background-color: rgb(239, 41, 41);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Terminate_Cannon_button.setObjectName(_fromUtf8("Terminate_Cannon_button"))
        self.gridLayout_4.addWidget(self.splitter_37, 0, 0, 1, 1)
        self.splitter_38 = QtGui.QSplitter(self.CannonMission)
        self.splitter_38.setOrientation(QtCore.Qt.Vertical)
        self.splitter_38.setObjectName(_fromUtf8("splitter_38"))
        self.Canon_T_Label_6 = QtGui.QLabel(self.splitter_38)
        self.Canon_T_Label_6.setStyleSheet(_fromUtf8("background-color: rgb(239, 41, 41);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Canon_T_Label_6.setObjectName(_fromUtf8("Canon_T_Label_6"))
        self.splitter_32 = QtGui.QSplitter(self.splitter_38)
        self.splitter_32.setOrientation(QtCore.Qt.Vertical)
        self.splitter_32.setObjectName(_fromUtf8("splitter_32"))
        self.canon_judge = QtGui.QPushButton(self.splitter_32)
        self.canon_judge.setStyleSheet(_fromUtf8("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.canon_judge.setObjectName(_fromUtf8("canon_judge"))
        self.splitter_31 = QtGui.QSplitter(self.splitter_32)
        self.splitter_31.setOrientation(QtCore.Qt.Vertical)
        self.splitter_31.setObjectName(_fromUtf8("splitter_31"))
        self.splitter_30 = QtGui.QSplitter(self.splitter_31)
        self.splitter_30.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_30.setObjectName(_fromUtf8("splitter_30"))
        self.Canon_T_Label_2 = QtGui.QLabel(self.splitter_30)
        self.Canon_T_Label_2.setStyleSheet(_fromUtf8("background-color: rgb(186, 189, 182);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Canon_T_Label_2.setObjectName(_fromUtf8("Canon_T_Label_2"))
        self.in_rad_1 = QtGui.QLineEdit(self.splitter_30)
        self.in_rad_1.setObjectName(_fromUtf8("in_rad_1"))
        self.splitter_29 = QtGui.QSplitter(self.splitter_31)
        self.splitter_29.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_29.setObjectName(_fromUtf8("splitter_29"))
        self.Canon_T_Label_3 = QtGui.QLabel(self.splitter_29)
        self.Canon_T_Label_3.setStyleSheet(_fromUtf8("background-color: rgb(186, 189, 182);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Canon_T_Label_3.setObjectName(_fromUtf8("Canon_T_Label_3"))
        self.in_rad_2 = QtGui.QLineEdit(self.splitter_29)
        self.in_rad_2.setObjectName(_fromUtf8("in_rad_2"))
        self.splitter_28 = QtGui.QSplitter(self.splitter_31)
        self.splitter_28.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_28.setObjectName(_fromUtf8("splitter_28"))
        self.Canon_T_Label_4 = QtGui.QLabel(self.splitter_28)
        self.Canon_T_Label_4.setStyleSheet(_fromUtf8("background-color: rgb(186, 189, 182);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Canon_T_Label_4.setObjectName(_fromUtf8("Canon_T_Label_4"))
        self.in_rad_3 = QtGui.QLineEdit(self.splitter_28)
        self.in_rad_3.setObjectName(_fromUtf8("in_rad_3"))
        self.splitter_14 = QtGui.QSplitter(self.splitter_31)
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName(_fromUtf8("splitter_14"))
        self.Canon_T_Label_5 = QtGui.QLabel(self.splitter_14)
        self.Canon_T_Label_5.setStyleSheet(_fromUtf8("background-color: rgb(186, 189, 182);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Canon_T_Label_5.setObjectName(_fromUtf8("Canon_T_Label_5"))
        self.in_len = QtGui.QLineEdit(self.splitter_14)
        self.in_len.setObjectName(_fromUtf8("in_len"))
        self.gridLayout_4.addWidget(self.splitter_38, 0, 1, 1, 1)
        self.Qtab.addTab(self.CannonMission, _fromUtf8(""))
        self.LineFollowerMission = QtGui.QWidget()
        self.LineFollowerMission.setObjectName(_fromUtf8("LineFollowerMission"))
        self.gridLayout_8 = QtGui.QGridLayout(self.LineFollowerMission)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.splitter_83 = QtGui.QSplitter(self.LineFollowerMission)
        self.splitter_83.setOrientation(QtCore.Qt.Vertical)
        self.splitter_83.setObjectName(_fromUtf8("splitter_83"))
        self.splitter_5 = QtGui.QSplitter(self.splitter_83)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.splitter_10 = QtGui.QSplitter(self.splitter_5)
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName(_fromUtf8("splitter_10"))
        self.circle_start = QtGui.QRadioButton(self.splitter_10)
        self.circle_start.setStyleSheet(_fromUtf8("background-color: rgb(138, 226, 52);"))
        self.circle_start.setObjectName(_fromUtf8("circle_start"))
        self.square_start = QtGui.QRadioButton(self.splitter_10)
        self.square_start.setStyleSheet(_fromUtf8("background-color: rgb(38, 95, 122);"))
        self.square_start.setObjectName(_fromUtf8("square_start"))
        self.Track_line_push = QtGui.QPushButton(self.splitter_5)
        self.Track_line_push.setStyleSheet(_fromUtf8("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Track_line_push.setObjectName(_fromUtf8("Track_line_push"))
        self.Cr_len_label_2 = QtGui.QLabel(self.splitter_5)
        self.Cr_len_label_2.setStyleSheet(_fromUtf8("background-color: rgb(114, 159, 207);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.Cr_len_label_2.setObjectName(_fromUtf8("Cr_len_label_2"))
        self.crack_value = QtGui.QTextBrowser(self.splitter_5)
        self.crack_value.setObjectName(_fromUtf8("crack_value"))
        self.unit_label = QtGui.QLabel(self.splitter_5)
        self.unit_label.setStyleSheet(_fromUtf8("background-color: rgb(115, 210, 22);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";"))
        self.unit_label.setObjectName(_fromUtf8("unit_label"))
        self.StopButton = QtGui.QPushButton(self.splitter_5)
        self.StopButton.setStyleSheet(_fromUtf8("  background-color: rgb(239, 41, 41);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.StopButton.setObjectName(_fromUtf8("StopButton"))
        self.splitter_82 = QtGui.QSplitter(self.splitter_83)
        self.splitter_82.setOrientation(QtCore.Qt.Vertical)
        self.splitter_82.setObjectName(_fromUtf8("splitter_82"))
        self.Cr_len_label_5 = QtGui.QLabel(self.splitter_82)
        self.Cr_len_label_5.setStyleSheet(_fromUtf8("background-color: rgb(0, 189, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 11pt \"URW Bookman L\";\n"
""))
        self.Cr_len_label_5.setObjectName(_fromUtf8("Cr_len_label_5"))
        self.splitter_81 = QtGui.QSplitter(self.splitter_82)
        self.splitter_81.setOrientation(QtCore.Qt.Vertical)
        self.splitter_81.setObjectName(_fromUtf8("splitter_81"))
        self.splitter_39 = QtGui.QSplitter(self.splitter_81)
        self.splitter_39.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_39.setObjectName(_fromUtf8("splitter_39"))
        self.grid_1_1 = QtGui.QTextBrowser(self.splitter_39)
        self.grid_1_1.setObjectName(_fromUtf8("grid_1_1"))
        self.grid_2_1 = QtGui.QTextBrowser(self.splitter_39)
        self.grid_2_1.setObjectName(_fromUtf8("grid_2_1"))
        self.grid_3_1 = QtGui.QTextBrowser(self.splitter_39)
        self.grid_3_1.setObjectName(_fromUtf8("grid_3_1"))
        self.grid_4_1 = QtGui.QTextBrowser(self.splitter_39)
        self.grid_4_1.setObjectName(_fromUtf8("grid_4_1"))
        self.splitter_40 = QtGui.QSplitter(self.splitter_81)
        self.splitter_40.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_40.setObjectName(_fromUtf8("splitter_40"))
        self.grid_1_2 = QtGui.QTextBrowser(self.splitter_40)
        self.grid_1_2.setObjectName(_fromUtf8("grid_1_2"))
        self.grid_2_2 = QtGui.QTextBrowser(self.splitter_40)
        self.grid_2_2.setObjectName(_fromUtf8("grid_2_2"))
        self.grid_3_2 = QtGui.QTextBrowser(self.splitter_40)
        self.grid_3_2.setObjectName(_fromUtf8("grid_3_2"))
        self.grid_4_2 = QtGui.QTextBrowser(self.splitter_40)
        self.grid_4_2.setObjectName(_fromUtf8("grid_4_2"))
        self.splitter_80 = QtGui.QSplitter(self.splitter_81)
        self.splitter_80.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_80.setObjectName(_fromUtf8("splitter_80"))
        self.grid_1_3 = QtGui.QTextBrowser(self.splitter_80)
        self.grid_1_3.setObjectName(_fromUtf8("grid_1_3"))
        self.grid_2_3 = QtGui.QTextBrowser(self.splitter_80)
        self.grid_2_3.setObjectName(_fromUtf8("grid_2_3"))
        self.grid_3_3 = QtGui.QTextBrowser(self.splitter_80)
        self.grid_3_3.setObjectName(_fromUtf8("grid_3_3"))
        self.grid_4_3 = QtGui.QTextBrowser(self.splitter_80)
        self.grid_4_3.setObjectName(_fromUtf8("grid_4_3"))
        self.gridLayout_8.addWidget(self.splitter_83, 0, 0, 1, 1)
        self.Qtab.addTab(self.LineFollowerMission, _fromUtf8(""))
        self.SpeceiesDetection = QtGui.QWidget()
        self.SpeceiesDetection.setObjectName(_fromUtf8("SpeceiesDetection"))
        self.splitter_25 = QtGui.QSplitter(self.SpeceiesDetection)
        self.splitter_25.setGeometry(QtCore.QRect(370, 130, 271, 421))
        self.splitter_25.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_25.setObjectName(_fromUtf8("splitter_25"))
        self.splitter_22 = QtGui.QSplitter(self.splitter_25)
        self.splitter_22.setOrientation(QtCore.Qt.Vertical)
        self.splitter_22.setObjectName(_fromUtf8("splitter_22"))
        self.circle_no = QtGui.QTextBrowser(self.splitter_22)
        self.circle_no.setObjectName(_fromUtf8("circle_no"))
        self.triangle_no = QtGui.QTextBrowser(self.splitter_22)
        self.triangle_no.setObjectName(_fromUtf8("triangle_no"))
        self.line_no = QtGui.QTextBrowser(self.splitter_22)
        self.line_no.setObjectName(_fromUtf8("line_no"))
        self.square_no = QtGui.QTextBrowser(self.splitter_22)
        self.square_no.setObjectName(_fromUtf8("square_no"))
        self.label_4 = QtGui.QLabel(self.splitter_25)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("pixmaps/shapes.png")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.splitter_16 = QtGui.QSplitter(self.SpeceiesDetection)
        self.splitter_16.setGeometry(QtCore.QRect(280, 30, 434, 48))
        self.splitter_16.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_16.setObjectName(_fromUtf8("splitter_16"))
        self.Species_start = QtGui.QPushButton(self.splitter_16)
        self.Species_start.setStyleSheet(_fromUtf8("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Species_start.setObjectName(_fromUtf8("Species_start"))
        self.Species_terminate = QtGui.QPushButton(self.splitter_16)
        self.Species_terminate.setStyleSheet(_fromUtf8("  background-color: rgb(239, 41, 41);\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;"))
        self.Species_terminate.setObjectName(_fromUtf8("Species_terminate"))
        self.Qtab.addTab(self.SpeceiesDetection, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Video = QtGui.QLabel(self.tab)
        self.Video.setFrameShape(QtGui.QFrame.Box)
        self.Video.setText(_fromUtf8(""))
        self.Video.setObjectName(_fromUtf8("Video"))
        self.gridLayout_2.addWidget(self.Video, 0, 0, 1, 1)
        self.Qtab.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.Qtab, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.Qtab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Yaw_label.setText(_translate("Form", "Yaw", None))
        self.Pitch_label.setText(_translate("Form", "Pitch", None))
        self.Roll_label.setText(_translate("Form", "Roll", None))
        self.Yaw_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Temp_sens_label_4.setText(_translate("Form", "MagnetoMeter", None))
        self.Temp_sens_label.setText(_translate("Form", "Temp Sens", None))
        self.unit_label_8.setText(_translate("Form", "deg C", None))
        self.Temp_sens_label_2.setText(_translate("Form", "water Sens", None))
        self.Joy_values_label_8.setText(_translate("Form", "MotorCurr1", None))
        self.Joy_values_label_9.setText(_translate("Form", "MotorCurr2", None))
        self.Joy_values_label_10.setText(_translate("Form", "MotorCurr3", None))
        self.Joy_values_label_11.setText(_translate("Form", "MotorCurr4", None))
        self.Joy_values_label_12.setText(_translate("Form", "MotorCurr5", None))
        self.Joy_values_label_13.setText(_translate("Form", "MotorCurr6", None))
        self.MotorCurr1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorCurr2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorCurr3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorCurr4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorCurr5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorCurr6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Joy_values_label_14.setText(_translate("Form", "MotorValue1", None))
        self.Joy_values_label_15.setText(_translate("Form", "MotorValue2", None))
        self.Joy_values_label_16.setText(_translate("Form", "MotorValue3", None))
        self.Joy_values_label_17.setText(_translate("Form", "MotorValue4", None))
        self.Joy_values_label_18.setText(_translate("Form", "MotorValue5", None))
        self.Joy_values_label_19.setText(_translate("Form", "MotorValue6", None))
        self.Current_sens_label.setText(_translate("Form", "Current Sensors", None))
        self.Joy_values_label.setText(_translate("Form", "JOY Values", None))
        self.PH_label.setText(_translate("Form", "PH Sensor", None))
        self.MotorValue1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.MotorValue6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Temp_sens_label_3.setText(_translate("Form", "Pressure Sens", None))
        self.cam_start_butt.setText(_translate("Form", "Start Cam", None))
        self.cam_stop_butt.setText(_translate("Form", "Stop Cam", None))
        self.Roll_label_2.setText(_translate("Form", "Index", None))
        self.rov_start_butt.setText(_translate("Form", "Launch ROV", None))
        self.rov_stop_butt.setText(_translate("Form", "Stop ROV", None))
        self.Roll_label_3.setText(_translate("Form", "com port", None))
        self.Roll_label_4.setText(_translate("Form", "Joy port", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.MainTab), _translate("Form", "Main Tab", None))
        self.Canon_T_Label.setText(_translate("Form", "Canon Type", None))
        self.AF_RB.setText(_translate("Form", "AF", None))
        self.Else_RB.setText(_translate("Form", "Else", None))
        self.Start_cannon.setText(_translate("Form", "Start Measuring", None))
        self.Radius1_Label.setText(_translate("Form", "Radius1", None))
        self.Radius2_Label.setText(_translate("Form", "Radius2", None))
        self.Radius3_Label.setText(_translate("Form", "Radius3", None))
        self.length_label.setText(_translate("Form", "Length", None))
        self.Volume_label.setText(_translate("Form", "Volume", None))
        self.Weight_label.setText(_translate("Form", "Weight", None))
        self.Radius1Value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Radius2Value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Radius3Value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Cannon_length_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Cannon_volume_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Canno_Weight_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.unit_label_2.setText(_translate("Form", "CM", None))
        self.unit_label_3.setText(_translate("Form", "CM", None))
        self.unit_label_4.setText(_translate("Form", "CM", None))
        self.unit_label_6.setText(_translate("Form", "CM", None))
        self.unit_label_5.setText(_translate("Form", "CM^3", None))
        self.unit_label_7.setText(_translate("Form", "Newton", None))
        self.Terminate_Cannon_button.setText(_translate("Form", "Terminate Process", None))
        self.Canon_T_Label_6.setText(_translate("Form", "Case_failed", None))
        self.canon_judge.setText(_translate("Form", "Judge call", None))
        self.Canon_T_Label_2.setText(_translate("Form", "In_Rad_1", None))
        self.Canon_T_Label_3.setText(_translate("Form", "In_Rad_2", None))
        self.Canon_T_Label_4.setText(_translate("Form", "In_Rad_3", None))
        self.Canon_T_Label_5.setText(_translate("Form", "In_Len_4", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.CannonMission), _translate("Form", "Cannon Mission", None))
        self.circle_start.setText(_translate("Form", "Start Circle", None))
        self.square_start.setText(_translate("Form", "Start Square", None))
        self.Track_line_push.setText(_translate("Form", "Start Line Track", None))
        self.Cr_len_label_2.setText(_translate("Form", " Crack Length:", None))
        self.crack_value.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.unit_label.setText(_translate("Form", "  cm", None))
        self.StopButton.setText(_translate("Form", "EMERGENCY STOP", None))
        self.Cr_len_label_5.setText(_translate("Form", "Grid_Mapping", None))
        self.grid_1_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_2_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_3_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_4_1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_1_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_2_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_3_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_4_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_1_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_2_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_3_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.grid_4_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.LineFollowerMission), _translate("Form", "Line Follower Mission", None))
        self.circle_no.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.triangle_no.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.line_no.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.square_no.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Species_start.setText(_translate("Form", "Start Species Mission", None))
        self.Species_terminate.setText(_translate("Form", "Terminate Mission", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.SpeceiesDetection), _translate("Form", "Species Detection", None))
        self.Qtab.setTabText(self.Qtab.indexOf(self.tab), _translate("Form", "Video Feed", None))

