# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'danciben.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

FONT_SIZE = 12

class Ui_Form_danciben(object):
    def setupUi(self, Form):
        a=1.8
        Form.setObjectName("Form")
        Form.resize(700*a, 500*a)
        Form.setMinimumSize(QtCore.QSize(700*a, 500*a))
        Form.setMaximumSize(QtCore.QSize(700*a, 500*a))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint, True)

        self.wm_logo = QtWidgets.QLabel(Form)
        self.wm_logo.setGeometry(QtCore.QRect(300*a, 10*a, 181*a, 81*a))
        self.wm_logo.setStyleSheet("background-color: rgb(0, 0, 0, 0);""image: url(:/登录界面/wmlog.png);")
        self.wm_logo.setObjectName("wm_logo")

        self.xianshi = QtWidgets.QWidget(Form)
        self.xianshi.setGeometry(QtCore.QRect(150*a, 100*a, 521*a, 361*a))
        self.xianshi.setStyleSheet("background-color: rgb(255, 251, 242);""border-radius: 15px;")
        self.xianshi.setObjectName("xianshi")

        # $上一页按钮
        self.shangyiye_bt = QtWidgets.QPushButton(self.xianshi)
        self.shangyiye_bt.setGeometry(QtCore.QRect(160*a, 330*a, 50*a, 21*a))
        self.shangyiye_bt.setObjectName("denglu_bt")
        self.shangyiye_bt.setStyleSheet("QPushButton{background-color: LightCyan ;border-radius: 3px;}"
                                        "QPushButton:hover{background-color:#54FF9F;}"
                                        "QPushButton:pressed{background-color:#43CD80}"
                                        )

        # $下一页按钮
        self.xiayiye_bt = QtWidgets.QPushButton(self.xianshi)
        self.xiayiye_bt.setGeometry(QtCore.QRect(300*a, 330*a, 50*a, 21*a))
        self.xiayiye_bt.setObjectName("denglu_bt")
        self.xiayiye_bt.setStyleSheet("QPushButton{background-color: LightCyan ;border-radius: 3px;}"
                                      "QPushButton:hover{background-color:#54FF9F;}"
                                      "QPushButton:pressed{background-color:#43CD80}"
                                      )

        self.shoucang_01 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_01.setGeometry(QtCore.QRect(0, 10, 521*a, 31*10*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_01.setFont(font)
        self.shoucang_01.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        self.shoucang_01.setObjectName("shoucang_01")

        self.sc_srl_button = QtWidgets.QPushButton(self.shoucang_01)
        self.sc_srl_button.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                      QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                      QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button.setObjectName("sc_srl_button")

        self.fanyi_button = QtWidgets.QPushButton(self.shoucang_01)
        self.fanyi_button.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                   QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                   QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button.setObjectName("fanyi_button")

        self.shoucang_02 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_02.setGeometry(QtCore.QRect(0, 42*a, 521*a, 31*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_02.setFont(font)
        self.shoucang_02.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        self.shoucang_02.setObjectName("shoucang_01")

        self.sc_srl_button_02 = QtWidgets.QPushButton(self.shoucang_02)
        self.sc_srl_button_02.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button_02.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                              QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                              QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button_02.setObjectName("sc_srl_button")

        self.fanyi_button_02 = QtWidgets.QPushButton(self.shoucang_02)
        self.fanyi_button_02.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button_02.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                           QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                           QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button_02.setObjectName("fanyi_button")

        self.shoucang_03 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_03.setGeometry(QtCore.QRect(0, 73*a, 521*a, 31*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_03.setFont(font)
        self.shoucang_03.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        self.shoucang_03.setObjectName("shoucang_03")

        self.sc_srl_button_03 = QtWidgets.QPushButton(self.shoucang_03)
        self.sc_srl_button_03.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button_03.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                                      QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                                      QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button_03.setObjectName("sc_srl_button")

        self.fanyi_button_03 = QtWidgets.QPushButton(self.shoucang_03)
        self.fanyi_button_03.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button_03.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                                   QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                                   QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button_03.setObjectName("fanyi_button")

        self.shoucang_04 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_04.setGeometry(QtCore.QRect(0, 104*a, 521*a, 31*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_04.setFont(font)
        self.shoucang_04.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        self.shoucang_04.setObjectName("shoucang_01")

        self.sc_srl_button_04 = QtWidgets.QPushButton(self.shoucang_04)
        self.sc_srl_button_04.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button_04.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                                      QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                                      QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button_04.setObjectName("sc_srl_button")

        self.fanyi_button_04 = QtWidgets.QPushButton(self.shoucang_04)
        self.fanyi_button_04.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button_04.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                                   QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                                   QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button_04.setObjectName("fanyi_button")

        self.shoucang_05 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_05.setGeometry(QtCore.QRect(0, 135*a, 521*a, 31*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_05.setFont(font)
        self.shoucang_05.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        self.shoucang_05.setObjectName("shoucang_01")

        self.sc_srl_button_05 = QtWidgets.QPushButton(self.shoucang_05)
        self.sc_srl_button_05.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button_05.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                                      QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                                      QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button_05.setObjectName("sc_srl_button")

        self.fanyi_button_05 = QtWidgets.QPushButton(self.shoucang_05)
        self.fanyi_button_05.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button_05.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                                   QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                                   QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button_05.setObjectName("fanyi_button")

        self.shoucang_06 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_06.setGeometry(QtCore.QRect(0, 166*a, 521*a, 31*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_06.setFont(font)
        self.shoucang_06.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        self.shoucang_06.setObjectName("shoucang_01")

        self.sc_srl_button_06 = QtWidgets.QPushButton(self.shoucang_06)
        self.sc_srl_button_06.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button_06.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                                      QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                                      QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button_06.setObjectName("sc_srl_button")

        self.fanyi_button_06 = QtWidgets.QPushButton(self.shoucang_06)
        self.fanyi_button_06.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button_06.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                                   QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                                   QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button_06.setObjectName("fanyi_button")

        self.shoucang_07 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_07.setGeometry(QtCore.QRect(0, 197*a, 521*a, 31*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_07.setFont(font)
        self.shoucang_07.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        self.shoucang_07.setObjectName("shoucang_01")

        self.sc_srl_button_07 = QtWidgets.QPushButton(self.shoucang_07)
        self.sc_srl_button_07.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button_07.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                                      QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                                      QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button_07.setObjectName("sc_srl_button")

        self.fanyi_button_07 = QtWidgets.QPushButton(self.shoucang_07)
        self.fanyi_button_07.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button_07.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                                   QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                                   QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button_07.setObjectName("fanyi_button")

        self.shoucang_08 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_08.setGeometry(QtCore.QRect(0, 228*a, 521*a, 31*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_08.setFont(font)
        self.shoucang_08.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        # self.shoucang_08.close()
        self.shoucang_08.setObjectName("shoucang_01")

        self.sc_srl_button_08 = QtWidgets.QPushButton(self.shoucang_08)
        self.sc_srl_button_08.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button_08.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                                      QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                                      QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button_08.setObjectName("sc_srl_button")

        self.fanyi_button_08 = QtWidgets.QPushButton(self.shoucang_08)
        self.fanyi_button_08.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button_08.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                                   QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                                   QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button_08.setObjectName("fanyi_button")

        self.shoucang_09 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_09.setGeometry(QtCore.QRect(0*a, 259*a, 521*a, 31*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_09.setFont(font)
        self.shoucang_09.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        self.shoucang_09.setObjectName("shoucang_01")

        self.sc_srl_button_09 = QtWidgets.QPushButton(self.shoucang_09)
        self.sc_srl_button_09.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button_09.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                                      QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                                      QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button_09.setObjectName("sc_srl_button")

        self.fanyi_button_09 = QtWidgets.QPushButton(self.shoucang_09)
        self.fanyi_button_09.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button_09.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                                   QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                                   QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button_09.setObjectName("fanyi_button")

        self.shoucang_10 = QtWidgets.QTextBrowser(self.xianshi)
        self.shoucang_10.setGeometry(QtCore.QRect(0, 290*a, 521*a, 31*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10*a)
        self.shoucang_10.setFont(font)
        self.shoucang_10.setStyleSheet("border-radius: 10px;""background-color: rgb(255, 251, 255);")
        self.shoucang_10.setObjectName("shoucang_01")

        self.sc_srl_button_10 = QtWidgets.QPushButton(self.shoucang_10)
        self.sc_srl_button_10.setGeometry(QtCore.QRect(444*a, 2*a, 31*a, 31*a))
        # self.qk_srl_button.setStyleSheet("border-image: url(:/登录界面/delete.png);""border-radius: 12px;")
        self.sc_srl_button_10.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/delete.png);border-radius: 5px;}
                                                                      QPushButton:hover{image: url(:/登录界面/delete - red.png);}
                                                                      QPushButton:pressed{image: url(:/登录界面/delete - black.png);}""")

        self.sc_srl_button_10.setObjectName("sc_srl_button")

        self.fanyi_button_10 = QtWidgets.QPushButton(self.shoucang_10)
        self.fanyi_button_10.setGeometry(QtCore.QRect(485*a, 2*a, 26*a, 26*a))
        self.fanyi_button_10.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0, 0);image: url(:/登录界面/fanyi.png);border-radius:5px;}
                                                                   QPushButton:hover{image: url(:/登录界面/fanyi_blue_q.png);}
                                                                   QPushButton:pressed{image: url(:/登录界面/fanyi_blue_s.png);}""")
        self.fanyi_button_10.setObjectName("fanyi_button")


        # self.wanma_logo_zx = QtWidgets.QLabel(self.xianshi)
        # self.wanma_logo_zx.setGeometry(QtCore.QRect(-10, 300, 151, 91))
        # self.wanma_logo_zx.setStyleSheet("image: url(:/登录界面/wm.png);")
        # self.wanma_logo_zx.setText("")
        # self.wanma_logo_zx.setObjectName("wanma_logo_zx")

        self.fanhuizhujiemian_button = QtWidgets.QPushButton(self.xianshi)
        self.fanhuizhujiemian_button.setGeometry(QtCore.QRect(410*a, 330*a, 100*a, 30*a))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # self.fanhuizhujiemian_button.setFont(font)
        self.fanhuizhujiemian_button.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/fhzjm_black.png);}
                                              QPushButton:hover{image: url(:/登录界面/fhzjm_red.png);}
                                              QPushButton:pressed{image: url(:/登录界面/fhzjm_blue.png);}""")
        self.fanhuizhujiemian_button.setObjectName("fanhuizhujiemian_button")

        self.quanjubeijing = QtWidgets.QWidget(Form)
        self.quanjubeijing.setGeometry(QtCore.QRect(0, 0, 701*a, 501*a))
        self.quanjubeijing.setStyleSheet("border-image: url(:/登录界面/dljm_bj.png);")
        self.quanjubeijing.setObjectName("quanjubeijing")

        self.xianshi.raise_()

        self.yonghutouxiang_bt = QtWidgets.QPushButton(Form)
        self.yonghutouxiang_bt.setGeometry(QtCore.QRect(50*a, 115*a, 70*a, 70*a))
        self.yonghutouxiang_bt.setStyleSheet("border-image: url(:/登录界面/1850.png);""border-radius: 15px;")
        self.yonghutouxiang_bt.setText("")
        self.yonghutouxiang_bt.setObjectName("yonghutouxiang_bt")

        self.my_sc = QtWidgets.QPushButton(Form)
        self.my_sc.setGeometry(QtCore.QRect(30*a, 200*a, 111*a, 31*a))
        self.my_sc.setStyleSheet("""QPushButton{image: url(:/登录界面/myshouc_black.png);border-radius:8px;}
                                    QPushButton:hover{image: url(:/登录界面/myshouc_red.png);}
                                    QPushButton:pressed{image: url(:/登录界面/myshouc_blue.png);}""")
        self.my_sc.setObjectName("my_sc")

        self.B_cihui = QtWidgets.QPushButton(Form)
        self.B_cihui.setGeometry(QtCore.QRect(30*a, 250*a, 111*a, 31*a))
        self.B_cihui.setStyleSheet("""QPushButton{image: url(:/登录界面/Bcihui_black.png);border-radius:8px;}
                                            QPushButton:hover{image: url(:/登录界面/Bcihui_red.png);}
                                            QPushButton:pressed{image: url(:/登录界面/Bcihui_blue.png);}""")
        self.B_cihui.setObjectName("B_cihui")

        self.for_cihui = QtWidgets.QPushButton(Form)
        self.for_cihui.setGeometry(QtCore.QRect(30*a, 300*a, 111*a, 31*a))
        self.for_cihui.setStyleSheet("""QPushButton{image: url(:/登录界面/4cihui_black.png);border-radius:8px;}
                                                    QPushButton:hover{image: url(:/登录界面/4cihui_red.png);}
                                                    QPushButton:pressed{image: url(:/登录界面/4cihui_blue.png);}""")
        self.for_cihui.setObjectName("for_cihui")

        self.six_cihui = QtWidgets.QPushButton(Form)
        self.six_cihui.setGeometry(QtCore.QRect(30*a, 350*a, 111*a, 31*a))
        self.six_cihui.setStyleSheet("""QPushButton{image: url(:/登录界面/6cihui_black.png);border-radius:8px;}
                                                    QPushButton:hover{image: url(:/登录界面/6cihui_red.png);}
                                                    QPushButton:pressed{image: url(:/登录界面/6cihui_blue.png);}""")
        self.six_cihui.setObjectName("six_cihui")

        self.neight_cihui = QtWidgets.QPushButton(Form)
        self.neight_cihui.setGeometry(QtCore.QRect(30*a, 400*a, 111*a, 31*a))
        self.neight_cihui.setStyleSheet("""QPushButton{image: url(:/登录界面/8cihui_black.png);border-radius:8px;}
                                                    QPushButton:hover{image: url(:/登录界面/8cihui_red.png);}
                                                    QPushButton:pressed{image: url(:/登录界面/8cihui_blue.png);}""")
        self.neight_cihui.setObjectName("neight_cihui")

        # self.yasi_cihui = QtWidgets.QPushButton(Form)
        # self.yasi_cihui.setGeometry(QtCore.QRect(30, 430, 111, 31))
        # self.yasi_cihui.setStyleSheet("QPushButton{background-color:#f5fefe;border-radius: 8px;}"
        #                          "QPushButton:hover{background-color:#54FF9F;}"
        #                          "QPushButton:pressed{background-color:#43CD80}"
        #                          )
        # self.yasi_cihui.setObjectName("yasi_cihui")

        # close
        self.gb = QtWidgets.QPushButton(Form)
        self.gb.setGeometry(QtCore.QRect(670*a, 0, 24*a, 24*a))
        self.gb.setMinimumSize(QtCore.QSize(24*a, 24*a))
        self.gb.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/close_24px_black.png);}
                                                              QPushButton:hover{image: url(:/登录界面/close_24px_red.png);}
                                                              QPushButton:pressed{image: url(:/登录界面/close_24px_black.png);}""")
        self.gb.setObjectName("gb")
        self.gb.clicked.connect(self.close)

        self.quanjubeijing.raise_()
        self.wm_logo.raise_()
        self.xianshi.raise_()
        self.yonghutouxiang_bt.raise_()
        self.my_sc.raise_()
        self.B_cihui.raise_()
        self.for_cihui.raise_()
        self.six_cihui.raise_()
        self.neight_cihui.raise_()
        self.gb.raise_()
        self.fanhuizhujiemian_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



        self.fanyi_button.close()  #@关闭显示
        self.fanyi_button_02.close()
        self.fanyi_button_03.close()
        self.fanyi_button_04.close()
        self.fanyi_button_05.close()
        self.fanyi_button_06.close()
        self.fanyi_button_07.close()
        self.fanyi_button_08.close()
        self.fanyi_button_09.close()
        self.fanyi_button_10.close()
        self.sc_srl_button.close()
        self.sc_srl_button_10.close()
        self.sc_srl_button_02.close()
        self.sc_srl_button_03.close()
        self.sc_srl_button_04.close()
        self.sc_srl_button_05.close()
        self.sc_srl_button_06.close()
        self.sc_srl_button_07.close()
        self.sc_srl_button_08.close()
        self.sc_srl_button_09.close()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.shangyiye_bt.setText(_translate("Form", "上一页"))
        self.xiayiye_bt.setText(_translate("Form", "下一页"))

        # self.fanhuizhujiemian_button.setText(_translate("Form", "返回主界面"))


class WanMaDicot(QtWidgets.QWidget, Ui_Form_danciben):
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
