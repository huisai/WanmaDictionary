# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gerenziliao.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

font_size = 9
font_size_small = 6

class Ui_Form_gerenziliao(object):
    def setupUi(self, Form):
        a=30
        b=1.8
        Form.setObjectName("Form")
        Form.resize(700*b, 500*b)
        Form.setMinimumSize(QtCore.QSize(700*b, 500*b))
        Form.setMaximumSize(QtCore.QSize(700*b, 500*b))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint, True)

        self.wm_logo = QtWidgets.QLabel(Form)
        self.wm_logo.setGeometry(QtCore.QRect(260*b, 10*b, 181*b, 81*b))
        self.wm_logo.setStyleSheet("background-color: rgb(0, 0, 0, 0);""image: url(:/登录界面/wmlog.png);")
        self.wm_logo.setObjectName("wm_logo")

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80*b, 100*b, 541*b, 381*b))
        self.widget.setStyleSheet("background-color: rgb(255, 251, 242);""border-radius: 15px;")
        self.widget.setObjectName("widget")

        self.yonghu_tx_lb = QtWidgets.QLabel(self.widget)
        self.yonghu_tx_lb.setGeometry(QtCore.QRect(150*b, 60*b, 71*b, 31*b))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(10)
        # self.yonghu_tx_lb.setFont(font)
        self.yonghu_tx_lb.setObjectName("yonghu_tx_lb")

        self.yonghutouxiang_bt = QtWidgets.QPushButton(self.widget)
        self.yonghutouxiang_bt.setGeometry(QtCore.QRect(240*b, (10+a)*b, 70*b, 70*b))
        self.yonghutouxiang_bt.setStyleSheet("border-image: url(:/登录界面/1850.png);""border-radius: 15px;")
        self.yonghutouxiang_bt.setText("")
        self.yonghutouxiang_bt.setObjectName("yonghutouxiang_bt")

        self.nicheng_bq = QtWidgets.QLabel(self.widget)
        self.nicheng_bq.setGeometry(QtCore.QRect(150*b, (90+a)*b, 71*b, 21*b))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(10)
        # self.nicheng_bq.setFont(font)
        self.nicheng_bq.setObjectName("nicheng_bq")

        self.xingbie_bq = QtWidgets.QLabel(self.widget)
        self.xingbie_bq.setGeometry(QtCore.QRect(150*b, (120+a)*b, 71*b, 21*b))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(10)
        # self.xingbie_bq.setFont(font)
        self.xingbie_bq.setObjectName("xingbie_bq")

        self.gerenshuoming_bq = QtWidgets.QLabel(self.widget)
        self.gerenshuoming_bq.setGeometry(QtCore.QRect(150*b, (140+a)*b, 71*b, 31*b))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(10)
        # self.gerenshuoming_bq.setFont(font)
        self.gerenshuoming_bq.setObjectName("gerenshuoming_bq")

        self.xingquaihao_bq = QtWidgets.QLabel(self.widget)
        self.xingquaihao_bq.setGeometry(QtCore.QRect(150*b, (170+a)*b, 71*b, 31*b))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(10)
        # self.xingquaihao_bq.setFont(font)
        self.xingquaihao_bq.setObjectName("xingquaihao_bq")

        self.wodeshengri_bq = QtWidgets.QLabel(self.widget)
        self.wodeshengri_bq.setGeometry(QtCore.QRect(150*b, (200+a)*b, 71*b, 31*b))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(10)
        # self.wodeshengri_bq.setFont(font)
        self.wodeshengri_bq.setObjectName("wodeshengri_bq")

        self.gerenziliao_bq = QtWidgets.QLabel(self.widget)
        self.gerenziliao_bq.setGeometry(QtCore.QRect(150*b, (230+a)*b, 71*b, 31*b))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(10)
        # self.gerenziliao_bq.setFont(font)
        self.gerenziliao_bq.setObjectName("gerenziliao_bq")

        self.shoujihaoma_bq = QtWidgets.QLabel(self.widget)
        self.shoujihaoma_bq.setGeometry(QtCore.QRect(150*b, (260+a)*b, 71*b, 31*b))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(10)
        # self.shoujihaoma_bq.setFont(font)
        self.shoujihaoma_bq.setObjectName("shoujihaoma_bq")

        self.wanma_logo_zx = QtWidgets.QLabel(self.widget)
        self.wanma_logo_zx.setGeometry(QtCore.QRect(-20*b, 315*b, 151*b, 91*b))
        self.wanma_logo_zx.setStyleSheet("background-color: rgb(0, 0, 0, 0);""image: url(:/登录界面/wm.png);")
        self.wanma_logo_zx.setText("")
        self.wanma_logo_zx.setObjectName("wanma_logo_zx")

        self.fanhuizhujiemian_button = QtWidgets.QPushButton(self.widget)
        self.fanhuizhujiemian_button.setGeometry(QtCore.QRect(425*b, 345*b, 100*b, 30*b))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # self.fanhuizhujiemian_button.setFont(font)
        self.fanhuizhujiemian_button.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/fhzjm_black.png);}
                                                      QPushButton:hover{image: url(:/登录界面/fhzjm_red.png);}
                                                      QPushButton:pressed{image: url(:/登录界面/fhzjm_blue.png);}""")
        self.fanhuizhujiemian_button.setObjectName("fanhuizhujiemian_button")

        self.xiugaigerenziliao_button = QtWidgets.QPushButton(self.widget)
        self.xiugaigerenziliao_button.setGeometry(QtCore.QRect(10*b, 10*b, 101*b, 31*b))
        self.xiugaigerenziliao_button.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/xggrzl_blue.png);}
                                                              QPushButton:hover{image: url(:/登录界面/xggrzl_red.png);}
                                                              QPushButton:pressed{image: url(:/登录界面/xggrzl_black.png);}""")
        self.xiugaigerenziliao_button.setObjectName("xiugaigerenziliao_button")

        self.quanjubeijing = QtWidgets.QWidget(Form)
        self.quanjubeijing.setGeometry(QtCore.QRect(0, 0, 701*b, 501*b))
        self.quanjubeijing.setStyleSheet("border-image: url(:/登录界面/dljm_bj.png);")
        self.quanjubeijing.setObjectName("quanjubeijing")

        # close
        self.gb = QtWidgets.QPushButton(Form)
        self.gb.setGeometry(QtCore.QRect(670*b, 0, 24*b, 24*b))
        self.gb.setMinimumSize(QtCore.QSize(24*b, 24*b))
        self.gb.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/close_24px_black.png);}
                                                      QPushButton:hover{image: url(:/登录界面/close_24px_red.png);}
                                                      QPushButton:pressed{image: url(:/登录界面/close_24px_black.png);}""")
        self.gb.setObjectName("gb")
        self.gb.clicked.connect(self.close)

        self.quanjubeijing.raise_()
        self.wm_logo.raise_()
        self.widget.raise_()
        self.gb.raise_()
        self.fanhuizhujiemian_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.yonghu_tx_lb.setText(_translate("Form", "用户头像："))
        self.nicheng_bq.setText(_translate("Form", "昵称："))
        self.xingbie_bq.setText(_translate("Form", "性别："))
        self.gerenshuoming_bq.setText(_translate("Form", "个人说明："))
        self.xingquaihao_bq.setText(_translate("Form", "兴趣爱好："))
        self.wodeshengri_bq.setText(_translate("Form", "我的生日："))
        self.gerenziliao_bq.setText(_translate("Form", "个人职业："))
        self.shoujihaoma_bq.setText(_translate("Form", "手机号码："))
        # self.fanhuizhujiemian_button.setText(_translate("Form", "返回主界面"))
        # self.xiugaigerenziliao_button.setText(_translate("Form", "修改个人资料"))


class WanMaDicot(QtWidgets.QWidget, Ui_Form_gerenziliao):
	def __init__(self):
		super().__init__() # 初始化父类构造方法
		self.setupUi(self) # 调用父类属性设置方法
if __name__ == "__main__":
    import dljm_sc
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = WanMaDicot()   #MyForm是自己的窗体类名
    myapp.show()
    sys.exit(app.exec_())