# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xincidian_0630.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import youfy
from dljiemian import Ui_Form_dljm, yanzhengma
import tp
class Ui_WanMa_dictionaries(object):
    def setupUi(self, WanMa_dictionaries):
        # 将边框隐藏那个不显示
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint, True)
        #去掉标题栏
        # self.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        # 设置窗口透明度
        # WanMa_dictionaries.setWindowOpacity(0.5)
        # #添加标题栏图标
        # self.steWindowIcon(QtGui.QIcon('图片名称'))
        WanMa_dictionaries.setObjectName("jhjhgjhgjhg")
        WanMa_dictionaries.resize(700, 500)
        WanMa_dictionaries.setMinimumSize(QtCore.QSize(700, 500))
        WanMa_dictionaries.setMaximumSize(QtCore.QSize(700, 500))
        WanMa_dictionaries.setStyleSheet("background-color: #fcfdfd;bround-radiys:15px;")

        self.layoutWidget = QtWidgets.QWidget(WanMa_dictionaries)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.layoutWidget1 = QtWidgets.QWidget(WanMa_dictionaries)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.layoutWidget2 = QtWidgets.QWidget(WanMa_dictionaries)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget2.setObjectName("layoutWidget2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.layoutWidget3 = QtWidgets.QWidget(WanMa_dictionaries)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget3.setObjectName("layoutWidget3")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.widget = QtWidgets.QWidget(WanMa_dictionaries)
        self.widget.setGeometry(QtCore.QRect(0, 0, 201, 51))
        self.widget.setMinimumSize(QtCore.QSize(201, 51))
        self.widget.setStyleSheet("image: url(:/图片素材/wmcd.png);")
        self.widget.setObjectName("widget")


        # self.widget_2.setObjectName("widget_2")
        self.widget_2 = QtWidgets.QWidget(WanMa_dictionaries)
        self.widget_2.setGeometry(QtCore.QRect(0, 50, 201, 401))
        self.widget_2.setMinimumSize(QtCore.QSize(201, 401))
        self.widget_2.setObjectName("widget_2")


        #查词功能标签
        self.chaci_gn = QtWidgets.QPushButton(self.widget_2)
        self.chaci_gn.setGeometry(QtCore.QRect(40, 20, 101, 31))
        self.chaci_gn.setMinimumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.chaci_gn.setFont(font)
        self.chaci_gn.setStyleSheet("QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/图片素材/dccx.png);}"
                                    "QPushButton:hover{color: rgb(0, 170, 255);}")
        self.chaci_gn.setObjectName("chaci_gn")

        #单词本标签
        self.danciben_gn = QtWidgets.QPushButton(self.widget_2)
        self.danciben_gn.setGeometry(QtCore.QRect(40, 60, 101, 31))
        self.danciben_gn.setMinimumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.danciben_gn.setFont(font)
        self.danciben_gn.setStyleSheet("QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/图片素材/dcb1.png);}"
                                    "QPushButton:hover{color: rgb(0, 170, 255);}")
        self.danciben_gn.setObjectName("danciben_gn")

        #精品课标签
        self.jingpinke_gn = QtWidgets.QPushButton(self.widget_2)
        self.jingpinke_gn.setGeometry(QtCore.QRect(40, 100, 101, 31))
        self.jingpinke_gn.setMinimumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jingpinke_gn.setFont(font)
        self.jingpinke_gn.setStyleSheet("QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/图片素材/jpk1.png);}"
                                    "QPushButton:hover{color: rgb(0, 170, 255);}")
        self.jingpinke_gn.setObjectName("jingpinke_gn")

        #人工翻译标签
        self.rengongfanyi_gn = QtWidgets.QPushButton(self.widget_2)
        self.rengongfanyi_gn.setGeometry(QtCore.QRect(40, 140, 101, 31))
        self.rengongfanyi_gn.setMinimumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rengongfanyi_gn.setFont(font)
        self.rengongfanyi_gn.setStyleSheet("QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/图片素材/rgfy1.png);}"
                                    "QPushButton:hover{color: rgb(0, 170, 255);}")
        self.rengongfanyi_gn.setObjectName("rengongfanyi_gn")

        #取词标签
        self.quci_gn = QtWidgets.QCheckBox(self.widget_2)
        self.quci_gn.setGeometry(QtCore.QRect(60, 270, 81, 20))
        self.quci_gn.setMinimumSize(QtCore.QSize(81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quci_gn.setFont(font)
        self.quci_gn.setStyleSheet("color: rgb(0, 170, 255);")
        self.quci_gn.setObjectName("quci_gn")

        #划词标签
        self.huaci_gn = QtWidgets.QCheckBox(self.widget_2)
        self.huaci_gn.setGeometry(QtCore.QRect(60, 290, 81, 20))
        self.huaci_gn.setMinimumSize(QtCore.QSize(81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.huaci_gn.setFont(font)
        self.huaci_gn.setStyleSheet("color: rgb(0, 170, 255);")
        self.huaci_gn.setObjectName("huaci_gn")


        self.gd1 = QtWidgets.QWidget(self.widget_2)
        self.gd1.setGeometry(QtCore.QRect(10, 170, 191, 101))
        self.gd1.setStyleSheet("image: url(:/图片素材/cxc.jpg);")
        self.gd1.setObjectName("gd1")


        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 320, 181, 101))
        self.widget_3.setObjectName("widget_3")

        self.shuchu_edit = QtWidgets.QTextBrowser(WanMa_dictionaries)
        self.shuchu_edit.setGeometry(QtCore.QRect(210, 50, 481, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shuchu_edit.setFont(font)
        self.shuchu_edit.setObjectName("shuchu_edit")

        #退出功能
        self.tuichu_gn = QtWidgets.QPushButton(WanMa_dictionaries)
        self.tuichu_gn.setGeometry(QtCore.QRect(660, 10, 31, 31))
        self.tuichu_gn.setMinimumSize(QtCore.QSize(31, 31))

        self.tuichu_gn.setText("")
        self.tuichu_gn.setObjectName("tuichu_gn")

        #最小化
        self.ck_zxh = QtWidgets.QToolButton(WanMa_dictionaries)
        self.ck_zxh.setGeometry(QtCore.QRect(630, 10, 30, 30))
        self.ck_zxh.setMinimumSize(QtCore.QSize(30, 30))
        self.ck_zxh.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.ck_zxh.setText("")
        self.ck_zxh.setObjectName("ck_zxh")

        #系统设置
        self.shezhi_gn = QtWidgets.QToolButton(WanMa_dictionaries)
        self.shezhi_gn.setGeometry(QtCore.QRect(600, 10, 31, 31))
        self.shezhi_gn.setMinimumSize(QtCore.QSize(31, 31))
        self.shezhi_gn.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.shezhi_gn.setText("")
        self.shezhi_gn.setObjectName("shezhi_gn")


        #文档翻译标签
        self.wendang_gn = QtWidgets.QPushButton(WanMa_dictionaries)
        self.wendang_gn.setGeometry(QtCore.QRect(220, 450, 101, 31))
        self.wendang_gn.setMinimumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wendang_gn.setFont(font)
        self.wendang_gn.setStyleSheet("QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/图片素材/wdcx.png);}"
                                    "QPushButton:hover{color: rgb(0, 170, 255);}")
        self.wendang_gn.setObjectName("wendang_gn")

        #截屏翻译标签
        self.jieping_gn = QtWidgets.QPushButton(WanMa_dictionaries)
        self.jieping_gn.setGeometry(QtCore.QRect(340, 450, 101, 31))
        self.jieping_gn.setMinimumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jieping_gn.setFont(font)
        self.jieping_gn.setStyleSheet("QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/图片素材/jt.png);}"
                                    "QPushButton:hover{color: rgb(0, 170, 255);}")
        self.jieping_gn.setObjectName("jieping_gn")

        #翻译按钮
        self.fanyi_button = QtWidgets.QPushButton(WanMa_dictionaries)
        self.fanyi_button.setGeometry(QtCore.QRect(580, 450, 100, 30))
        self.fanyi_button.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fanyi_button.setFont(font)
        self.fanyi_button.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.fanyi_button.setObjectName("fanyi_button")
        self.fanyi_button.clicked.connect(self.slot_method)#调用按钮函数

        #输入信息栏
        self.shuru_edit = QtWidgets.QTextEdit(WanMa_dictionaries)
        self.shuru_edit.setGeometry(QtCore.QRect(210, 260, 481, 181))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.shuru_edit.setFont(font)
        self.shuru_edit.setObjectName("shuru_edit")

        #清空按钮
        self.qingkong_gn = QtWidgets.QPushButton(WanMa_dictionaries)
        self.qingkong_gn.setGeometry(QtCore.QRect(510, 450, 31, 31))
        self.qingkong_gn.setMinimumSize(QtCore.QSize(31, 31))

        # self.qingkong_gn.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.qingkong_gn.setStyleSheet("QPushButton{background-color:#D30000;border:none;color:#ffffff;font-size:20px;}"
                              "QPushButton:hover{background-color:#333333;}")
        self.qingkong_gn.setText("")
        self.qingkong_gn.setObjectName("qingkong_gn")

        #历史记录按钮
        self.lishijilu = QtWidgets.QToolButton(WanMa_dictionaries)
        self.lishijilu.setGeometry(QtCore.QRect(540, 450, 31, 31))
        self.lishijilu.setMinimumSize(QtCore.QSize(31, 31))
        self.lishijilu.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.lishijilu.setText("")
        self.lishijilu.setObjectName("lishijilu")





        self.shuru_edit.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.shuchu_edit.raise_()
        self.tuichu_gn.raise_()
        self.ck_zxh.raise_()
        self.shezhi_gn.raise_()
        self.wendang_gn.raise_()
        self.jieping_gn.raise_()
        self.fanyi_button.raise_()
        self.qingkong_gn.raise_()
        self.lishijilu.raise_()

        self.retranslateUi(WanMa_dictionaries)
        QtCore.QMetaObject.connectSlotsByName(WanMa_dictionaries)

    #翻译按钮调用函数
    def slot_method(self):
        # 输出信息
        #self.shuru_edit.toPlainText()获取输入框信息
        a= self.shuru_edit.toPlainText()
        x="翻译结果：" + youfy.fanyi_youdao(a)
        self.shuchu_edit.setText(x)
        #显示框自动跳到底部
        # self.shuchu_edit.moveCursor(+End)
        #每次输入完毕清空输入框
        # self.shuru_edit.setPlainText("")

    #信息显示栏显示内容
    # def show_dljm(self):
    #
    def retranslateUi(self, WanMa_dictionaries):
        _translate = QtCore.QCoreApplication.translate
        WanMa_dictionaries.setWindowTitle(_translate("WanMa_dictionaries", "标题栏"))
        self.chaci_gn.setText(_translate("WanMa_dictionaries", "    查词翻译"))
        self.danciben_gn.setText(_translate("WanMa_dictionaries", "    单词本"))
        self.jingpinke_gn.setText(_translate("WanMa_dictionaries", "    精品课"))
        self.rengongfanyi_gn.setText(_translate("WanMa_dictionaries", "    人工翻译"))
        self.quci_gn.setText(_translate("WanMa_dictionaries", "  取  词"))
        self.huaci_gn.setText(_translate("WanMa_dictionaries", "  划  词"))
        self.wendang_gn.setText(_translate("WanMa_dictionaries", "    文档翻译"))
        self.jieping_gn.setText(_translate("WanMa_dictionaries", "    截屏翻译"))
        self.fanyi_button.setText(_translate("WanMa_dictionaries", "翻 译"))

