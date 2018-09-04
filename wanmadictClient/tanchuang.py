# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tanchuang.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        a=1.8
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint, True)
        Form.setObjectName("Form")
        Form.resize(300*a, 143*a)
        Form.setStyleSheet("background-color: rgb(255, 255, 210);")
        self.z_img = QtWidgets.QLabel(Form)
        self.z_img.setGeometry(QtCore.QRect(0, 30*a, 81*a, 80*a))
        self.z_img.setPixmap(QtGui.QPixmap("登录界面图片/Flap.png"))
        # self.z_img.setStyleSheet("background-color: rgb(49, 255, 100);")
        # "border:2px solid red;"边框属性
        self.z_img.setScaledContents(True)
        self.z_img.setObjectName("label")

        self.tishilan = QtWidgets.QLabel(Form)
        self.tishilan.setGeometry(QtCore.QRect(170, 40*a, 180*a, 60*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(15)
        self.tishilan.setFont(font)

        # self.tishilan.setStyleSheet("text - align: center;")

        #垂直居中
        self.tishilan.setAlignment(QtCore.Qt.AlignVCenter)
        # 水平居中
        # self.tishilan.setAlignment(QtCore.Qt.AlignCenter)
        self.tishilan.setObjectName("textBrowser")

        self.biaoti = QtWidgets.QLabel(Form)
        self.biaoti.setGeometry(QtCore.QRect(0, 0, 301*a, 21*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(11*a)
        self.biaoti.setFont(font)
        self.biaoti.setStyleSheet("background-color: #407d94;")
        self.biaoti.setAlignment(QtCore.Qt.AlignCenter)

        self.biaoti.setObjectName("label_2")

        # 确认按钮
        self.ok_bt = QtWidgets.QPushButton(Form)
        self.ok_bt.setGeometry(QtCore.QRect(0, 120*a+4, 301*a, 21*a))
        self.ok_bt.setObjectName("denglu_bt")
        self.ok_bt.setStyleSheet("QPushButton{background-color:#407d94;border-radius: 3px;}"
                                     "QPushButton:hover{background-color:#54FF9F;}"
                                     "QPushButton:pressed{background-color:#43CD80}"
                                 )
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(11 * 1.5)
        self.ok_bt.setFont(font)
        self.ok_bt.clicked.connect(self.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.biaoti.setText(_translate("Form", "信息提示栏"))
        self.ok_bt.setText(_translate("Form", "确认"))

# def qidong(x):
#     # if __name__ == "__main__":
#     import dljm_sc
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     myapp = Ui_Form(x)
#     myapp.show()
#     sys.exit(app.exec_())
