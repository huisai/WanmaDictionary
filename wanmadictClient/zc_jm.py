# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zc_jm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

font_size = 9*1.8
font_size_small = 6*1.8

class Ui_Form_zc_jm(object):
    def setupUi(self, Form):
        a=1.8
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint, True)
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(700*a, 500*a)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")

        # 全局背景图
        self.beijing = QtWidgets.QLabel(Form)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 700*a, 500*a))
        self.beijing.setStyleSheet("border-image: url(:/登录界面/dljm_bj.png);")
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")

        #昵称标签
        self.nc_bq = QtWidgets.QLabel(Form)
        self.nc_bq.setGeometry(QtCore.QRect(200*a, 130*a, 41*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.nc_bq.setFont(font)
        self.nc_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.nc_bq.setObjectName("nc_bq")

        #昵称输入栏
        self.nc_shuru = QtWidgets.QLineEdit(Form)
        self.nc_shuru.setGeometry(QtCore.QRect(250*a, 130*a, 181*a, 35*a))
        self.nc_shuru.setObjectName("nc_shuru")
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.nc_shuru.setFont(font)
        self.nc_shuru.setStyleSheet("QLineEdit{border-radius: 5px;}")

        # 性别标签
        self.xb_bq = QtWidgets.QLabel(Form)
        self.xb_bq.setGeometry(QtCore.QRect(200*a, 166*a, 41*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.xb_bq.setFont(font)
        self.xb_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.xb_bq.setObjectName("xb_bq")

        # 选择器男
        self.nan = QtWidgets.QRadioButton(Form)
        self.nan.setGeometry(QtCore.QRect(260*a, 172*a, 41*a, 21*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size_small)
        self.nan.setFont(font)
        self.nan.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.nan.setObjectName("nan")

        # 选择器女
        self.nv = QtWidgets.QRadioButton(Form)
        self.nv.setGeometry(QtCore.QRect(320*a, 172*a, 41*a, 21*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size_small)
        self.nv.setFont(font)
        self.nv.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.nv.setObjectName("nv")

        # 出生日期标签
        self.chushengriqi_bq = QtWidgets.QLabel(Form)
        self.chushengriqi_bq.setGeometry(QtCore.QRect(170*a, 200*a, 71*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.chushengriqi_bq.setFont(font)
        self.chushengriqi_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.chushengriqi_bq.setObjectName("chushengriqi_bq")

        # 出生日期选择
        self.chushengriqi = QtWidgets.QDateTimeEdit(Form)
        self.chushengriqi.setGeometry(QtCore.QRect(250*a, 200*a, 181*a, 35*a))
        self.chushengriqi.setObjectName("chushengriqi")
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.chushengriqi.setFont(font)
        self.chushengriqi.setStyleSheet("QDateTimeEdit{border-radius: 3px;}")

        #登录密码标签
        self.denglumimamingcheng = QtWidgets.QLabel(Form)
        self.denglumimamingcheng.setGeometry(QtCore.QRect(170*a, 240*a, 81*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.denglumimamingcheng.setFont(font)
        self.denglumimamingcheng.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.denglumimamingcheng.setObjectName("denglumimamingcheng")

        # 登录密码输入栏
        self.denglumimashuru = QtWidgets.QLineEdit(Form)

        self.denglumimashuru.setGeometry(QtCore.QRect(250*a, 240*a, 181*a, 35*a))
        self.denglumimashuru.setMinimumSize(QtCore.QSize(181*a, 35*a))
        self.denglumimashuru.setObjectName("denglumimashuru")
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(6*a)
        self.denglumimashuru.setFont(font)
        self.denglumimashuru.setStyleSheet("QLineEdit{border-radius: 5px;}")
        self.denglumimashuru.setEchoMode(QtWidgets.QLineEdit.Password)


        #确认密码标签
        self.querenmima_bq = QtWidgets.QLabel(Form)
        self.querenmima_bq.setGeometry(QtCore.QRect(170*a, 280*a, 81*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.querenmima_bq.setFont(font)
        self.querenmima_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.querenmima_bq.setObjectName("querenmima_bq")

        #确认密码输入栏
        self.querenmima_shuru = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(6*a)
        self.querenmima_shuru.setFont(font)
        self.querenmima_shuru.setGeometry(QtCore.QRect(250*a, 280*a, 181*a, 35*a))
        self.querenmima_shuru.setStyleSheet("QLineEdit{border-radius: 5px;}")
        self.querenmima_shuru.setEchoMode(QtWidgets.QLineEdit.Password)
        self.querenmima_shuru.setObjectName("querenmima_shuru")

        # 邮箱标签
        self.youxiang_bq = QtWidgets.QLabel(Form)
        self.youxiang_bq.setGeometry(QtCore.QRect(200*a, 320*a, 41*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.youxiang_bq.setFont(font)
        self.youxiang_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.youxiang_bq.setObjectName("youxiang_bq")

        # 邮箱输入栏
        self.youxiang_shuru = QtWidgets.QLineEdit(Form)
        self.youxiang_shuru.setGeometry(QtCore.QRect(250*a, 320*a, 181*a, 35*a))
        self.youxiang_shuru.setStyleSheet("QLineEdit{border-radius: 5px;}")
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.youxiang_shuru.setFont(font)
        self.youxiang_shuru.setObjectName("youxiang_shuru")

        # 注册按钮
        self.zhuce_button = QtWidgets.QPushButton(Form)
        self.zhuce_button.setGeometry(QtCore.QRect(280*a, 365*a, 121*a, 31*a))
        self.zhuce_button.setObjectName("zhuce_button")
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(font_size)
        self.zhuce_button.setFont(font)
        self.zhuce_button.setStyleSheet("QPushButton{background-color:#E0FFFF;border-radius: 3px;}"
                                        "QPushButton:hover{background-color:#54FF9F;}"
                                        "QPushButton:pressed{background-color:#43CD80}"
                                        )



        # close
        self.gb = QtWidgets.QPushButton(Form)
        self.gb.setGeometry(QtCore.QRect(670*a, 0, 24*a, 24*a))
        self.gb.setMinimumSize(QtCore.QSize(24*a, 24*a))
        self.gb.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/close_24px_black.png);}
                                      QPushButton:hover{image: url(:/登录界面/close_24px_red.png);}
                                      QPushButton:pressed{image: url(:/登录界面/close_24px_black.png);}""")
        self.gb.setObjectName("gb")

        #logo
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(10*a, 350*a, 200*a, 200*a))
        self.logo.setStyleSheet("background-color: rgb(0, 0, 0, 0);""border-image: url(:/登录界面/wm.png);")
        self.logo.setObjectName("logo")



        # 用户头像
        self.touxiang = QtWidgets.QPushButton(Form)
        self.touxiang.setGeometry(QtCore.QRect(300*a, 50*a, 70*a, 70*a))
        self.touxiang.setMinimumSize(QtCore.QSize(70, 70))
        self.touxiang.setStyleSheet("border-image: url(:/登录界面/1850.png);""border-radius: 35px;")
        self.touxiang.setObjectName("touxiang")

        # close
        self.gb = QtWidgets.QPushButton(Form)
        self.gb.setGeometry(QtCore.QRect(670*a, 0, 24*a, 24*a))
        self.gb.setMinimumSize(QtCore.QSize(24*a, 24*a))
        self.gb.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/close_24px_black.png);}
                                              QPushButton:hover{image: url(:/登录界面/close_24px_red.png);}
                                              QPushButton:pressed{image: url(:/登录界面/close_24px_black.png);}""")
        self.gb.setObjectName("gb")
        self.gb.clicked.connect(self.close)


        self.beijing.raise_()
        self.nc_bq.raise_()
        self.nc_shuru.raise_()
        self.denglumimamingcheng.raise_()
        self.querenmima_bq.raise_()
        self.denglumimashuru.raise_()
        self.querenmima_shuru.raise_()
        self.nan.raise_()
        self.nv.raise_()
        self.chushengriqi.raise_()
        self.xb_bq.raise_()
        self.chushengriqi_bq.raise_()
        self.zhuce_button.raise_()
        # self.yanzhengma_bq.raise_()
        # self.yanzhengma_shuru.raise_()
        # self.yanzhengma_xianshi.raise_()
        self.youxiang_bq.raise_()
        self.youxiang_shuru.raise_()
        self.gb.raise_()
        self.logo.raise_()
        self.touxiang.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nc_bq.setText(_translate("Form", "账号"))
        self.denglumimamingcheng.setText(_translate("Form", "登录密码"))
        self.querenmima_bq.setText(_translate("Form", "确认密码"))
        self.nan.setText(_translate("Form", "男"))
        self.nv.setText(_translate("Form", "女"))
        self.chushengriqi.setDisplayFormat(_translate("Form", "yyyy/M/d"))
        self.xb_bq.setText(_translate("Form", "性别"))
        self.chushengriqi_bq.setText(_translate("Form", "出生日期"))
        self.zhuce_button.setText(_translate("Form", "注册"))
        # self.yanzhengma_bq.setText(_translate("Form", "   验证码"))
        self.youxiang_bq.setText(_translate("Form", "邮箱"))


class WanMaDicot(QtWidgets.QWidget, Ui_Form_zc_jm):
	def __init__(self):
		super().__init__() # 初始化父类构造方法
		self.setupUi(self) # 调用父类属性设置方法
if __name__ == "__main__":
    import dljm_sc
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = WanMaDicot()   #MyForm是自己的窗体类名
    # myapp.youxianggeshi.close()
    # myapp.mimabuyizhi.close()
    myapp.show()
    sys.exit(app.exec_())

