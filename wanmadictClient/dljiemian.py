# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dljiemian.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint
from . import yanzhengma
from . import dljm_sc


FONT_SIZE = 16



class Ui_Form_dljm(object):
    def setupUi(self, Form):
        a=1.8
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint, True)
        Form.setObjectName("Form")
        Form.resize(701*a, 500*a)
        Form.setMinimumSize(QtCore.QSize(701*a, 500*a))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")


        # $start
        self.setMinimumWidth(250*a)
        self.setMouseTracking(True)  # 设置widget鼠标跟踪
        self.initDrag()
        # $end



# 全局背景图片
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 701*a, 501*a))
        self.widget.setStyleSheet("border-image: url(:/登录界面/dljm_bj.png);")
        self.widget.setObjectName("widget")

        # 账号输入栏
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(270*a, 110*a, 181*a, 35*a))
        self.username.setMinimumSize(QtCore.QSize(181*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12*a)
        self.username.setFont(font)
        self.username.setMaxLength(20*a)
        self.username.setObjectName("username")
        self.username.setStyleSheet("QLineEdit{border-radius: 5px;}")

        # 密码输入栏
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(270*a, 155*a, 181*a, 35*a))
        self.password.setMinimumSize(QtCore.QSize(181*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(6*a)
        self.password.setFont(font)
        self.password.setMaxLength(12*a)
        self.password.setObjectName("password")
        self.password.setStyleSheet("QLineEdit{border-radius: 5px;}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        # 账号标签
        self.zhuce_bqian = QtWidgets.QLabel(Form)
        self.zhuce_bqian.setGeometry(QtCore.QRect(225*a, 110*a, 41*a, 40*a))
        self.zhuce_bqian.setMinimumSize(QtCore.QSize(41*a, 35*a))
        self.zhuce_bqian.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        font_zh = QtGui.QFont()
        font_zh.setFamily("ADMUI3Lg")
        font_zh.setPointSize(8*a)
        self.zhuce_bqian.setFont(font_zh)
        self.zhuce_bqian.setObjectName("label")

        # 密码标签
        self.mima_bq = QtWidgets.QPushButton(Form)
        self.mima_bq.setGeometry(QtCore.QRect(225*a, 155*a, 41*a, 35*a))
        self.mima_bq.setMinimumSize(QtCore.QSize(41*a, 35*a))
        self.mima_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8*a)
        self.mima_bq.setFont(font)
        self.mima_bq.setObjectName("label_3")

        #$密码错误
        self.mimacuowu = QtWidgets.QPushButton(Form)
        self.mimacuowu.setGeometry(QtCore.QRect(450*a, 155*a, 80*a, 35*a))
        self.mimacuowu.setMinimumSize(QtCore.QSize(41*a, 35*a))
        self.mimacuowu.setStyleSheet("background-color: rgb(0, 0, 0, 0);""color:red;")
        self.mimacuowu.close()#$密码输入错误标签默认关闭
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(15*a)
        self.mimacuowu.setFont(font)
        self.mimacuowu.setObjectName("mimacuowu")

        #记录账号选项框
        self.Jilu_Zhanghao = QtWidgets.QCheckBox(Form)
        self.Jilu_Zhanghao.setGeometry(QtCore.QRect(270*a, 210*a, 100*a, 20*a))
        self.Jilu_Zhanghao.setMinimumSize(QtCore.QSize(80*a, 20*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8*a)
        self.Jilu_Zhanghao.setFont(font)
        self.Jilu_Zhanghao.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.Jilu_Zhanghao.setObjectName("Jilu_Zhanghao")

        # 记录密码选项框
        self.jilu_mima = QtWidgets.QCheckBox(Form)
        self.jilu_mima.setGeometry(QtCore.QRect(380*a, 210*a, 100*a, 20*a))
        self.jilu_mima.setMinimumSize(QtCore.QSize(80*a, 20*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8*a)
        self.jilu_mima.setFont(font)
        self.jilu_mima.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        self.jilu_mima.setObjectName("jilu_mima")

        #登录按钮
        self.denglu_bt = QtWidgets.QPushButton(Form)
        self.denglu_bt.setGeometry(QtCore.QRect(320*a, 295*a, 81*a, 31*a))
        self.denglu_bt.setObjectName("denglu_bt")
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8 * a)
        self.denglu_bt.setFont(font)
        self.denglu_bt.setStyleSheet("QPushButton{background-color:#f5fefe;border-radius: 3px;}"
                                      "QPushButton:hover{background-color:#54FF9F;}"
                                      "QPushButton:pressed{background-color:#43CD80}"
                                      )

        #验证码输入框
        self.yanzhengma_shuru = QtWidgets.QLineEdit(Form)
        self.yanzhengma_shuru.setGeometry(QtCore.QRect(271*a, 241*a, 90*a, 31*a))
        self.yanzhengma_shuru.setMinimumSize(QtCore.QSize(90*a, 31*a))
        self.yanzhengma_shuru.setMaximumSize(QtCore.QSize(95*a, 31*a))
        self.yanzhengma_shuru.setMaxLength(5*a)
        self.yanzhengma_shuru.setObjectName("lineEdit_3")
        self.yanzhengma_shuru.setStyleSheet("QLineEdit{border-radius: 5px;}")

        #验证码图片显示窗口
        self.yanzhengma_xianshi = QtWidgets.QLabel(Form)
        self.yanzhengma_xianshi.setGeometry(QtCore.QRect(364*a, 241*a, 90*a, 31*a))
        self.yanzhengma_xianshi.setMinimumSize(QtCore.QSize(90*a, 30*a))
        self.yanzhengma_xianshi.setMaximumSize(QtCore.QSize(95*a, 31*a))
        img, self.content = yanzhengma.get_code()
        tp_path='hupian.jpg'
        img.save(tp_path)
        self.yanzhengma_xianshi.setPixmap(QtGui.QPixmap(tp_path))
        self.yanzhengma_xianshi.setObjectName("widget_2")

        # 验证码切换
        self.yzm_qh = QtWidgets.QPushButton(Form)
        self.yzm_qh.setGeometry(QtCore.QRect(460*a, 241*a, 95*a, 31*a))
        self.yzm_qh.setMinimumSize(QtCore.QSize(95*a, 31*a))
        self.yzm_qh.setStyleSheet("QPushButton{background-color:rgb(0, 0, 0, 0);}"
                                      "QPushButton:hover{color:red;}")
        self.yzm_qh.clicked.connect(self.shuaxin)
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8*a)
        self.yzm_qh.setFont(font)
        self.yzm_qh.setObjectName("label")

        #$验证码错误
        self.yanzhengmacuowu = QtWidgets.QLabel(Form)
        self.yanzhengmacuowu.setGeometry(QtCore.QRect(275*a, 265*a, 80*a, 35*a))
        self.yanzhengmacuowu.setMinimumSize(QtCore.QSize(41*a, 35*a))
        self.yanzhengmacuowu.setStyleSheet("background-color: rgb(0, 0, 0, 0);""color:red;")
        self.yanzhengmacuowu.close()#$验证码错误提示标签默认关闭状态
        font_zh = QtGui.QFont()
        font_zh.setFamily("ADMUI3Lg")
        font_zh.setPointSize(15*a)
        self.yanzhengmacuowu.setFont(font_zh)
        self.yanzhengmacuowu.setObjectName("yanzhengmacuowu")


        # 注册账号标签
        self.zc_zhanghao = QtWidgets.QPushButton(Form)
        self.zc_zhanghao.setGeometry(QtCore.QRect(255*a, 340*a, 100*a, 16*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8*a)
        self.zc_zhanghao.setFont(font)
        self.zc_zhanghao.setStyleSheet("QPushButton{background-color:rgb(0, 0, 0, 0);}"
                                  "QPushButton:hover{color:blue;}")
        self.zc_zhanghao.setObjectName("zc_zhanghao")

        #忘记密码标签
        self.wangji_mima = QtWidgets.QPushButton(Form)
        self.wangji_mima.setGeometry(QtCore.QRect(365*a, 340*a, 100*a, 16*a))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(8*a)
        self.wangji_mima.setFont(font)
        self.wangji_mima.setStyleSheet("QPushButton{background-color:rgb(0, 0, 0, 0);}"
                                  "QPushButton:hover{color:red;}")
        # self.wangji_mima.setObjectName("zc_zhanghao_2")

        #用户头像
        self.touxiang = QtWidgets.QPushButton(Form)
        self.touxiang.setGeometry(QtCore.QRect(320*a, 30*a, 70*a, 70*a))
        self.touxiang.setMinimumSize(QtCore.QSize(70*a, 70*a))
        self.touxiang.setStyleSheet("border-image: url(:/登录界面/1850.png);""border-radius: 35px;")
        self.touxiang.setObjectName("touxiang")

        # qq
        self.qq = QtWidgets.QPushButton(Form)
        self.qq.setGeometry(QtCore.QRect(270*a, 370*a, 30*a, 30*a))
        self.qq.setMinimumSize(QtCore.QSize(30*a, 30*a))
        self.qq.setStyleSheet("border-image: url(:/登录界面/qq.jpg);""border-radius: 15px;")
        self.qq.setObjectName("qq")

        #wx
        self.wx = QtWidgets.QPushButton(Form)
        self.wx.setGeometry(QtCore.QRect(310*a, 370*a, 30*a, 30*a))
        self.wx.setMinimumSize(QtCore.QSize(30*a, 30*a))
        self.wx.setStyleSheet("border-image: url(:/登录界面/wx.jpg);""border-radius: 15px;")
        self.wx.setObjectName("wx")

        # wb
        self.wb = QtWidgets.QPushButton(Form)
        self.wb.setGeometry(QtCore.QRect(350*a, 370*a, 30*a, 30*a))
        self.wb.setMinimumSize(QtCore.QSize(30*a, 30*a))
        self.wb.setStyleSheet("border-image: url(:/登录界面/wb.jpg);""border-radius: 15px;")
        self.wb.setObjectName("wb")

        # yx
        self.yx = QtWidgets.QPushButton(Form)
        self.yx.setGeometry(QtCore.QRect(390*a, 370*a, 30*a, 30*a))
        self.yx.setMinimumSize(QtCore.QSize(30*a, 30*a))
        self.yx.setStyleSheet("border-image: url(:/登录界面/yx.jpg);""border-radius: 15px;")
        self.yx.setObjectName("yx")

        # wb
        self.px = QtWidgets.QPushButton(Form)
        self.px.setGeometry(QtCore.QRect(430*a, 370*a, 30*a, 30*a))
        self.px.setMinimumSize(QtCore.QSize(30, 30))
        self.px.setStyleSheet("border-image: url(:/登录界面/px.jpg);""border-radius: 15px;")
        self.px.setObjectName("px")

        # close
        self.gb = QtWidgets.QPushButton(Form)
        self.gb.setGeometry(QtCore.QRect(670*a, 0*a, 24*a, 24*a))
        self.gb.setMinimumSize(QtCore.QSize(24*a, 24*a))
        self.gb.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/close_24px_black.png);}
                              QPushButton:hover{image: url(:/登录界面/close_24px_red.png);}
                              QPushButton:pressed{image: url(:/登录界面/close_24px_black.png);}""")
        self.gb.setObjectName("gb")
        self.gb.clicked.connect(self.close)

        # zxh
        self.zxh = QtWidgets.QPushButton(Form)
        self.zxh.setGeometry(QtCore.QRect(645*a, 2*a, 24*a, 24*a))
        self.zxh.setMinimumSize(QtCore.QSize(24*a, 24*a))
        self.zxh.clicked.connect(self.showMinimized)
        self.zxh.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/mize_24px.png);}
                                      QPushButton:hover{image: url(:/登录界面/mize_24px_h.png);}
                                      QPushButton:pressed{image: url(:/登录界面/mize_24px.png);}""")
        self.zxh.setObjectName("zxh")
        #
        # # sz
        # self.sz = QtWidgets.QPushButton(Form)
        # self.sz.setGeometry(QtCore.QRect(620, 2, 24, 24))
        # self.sz.setMinimumSize(QtCore.QSize(24, 24))
        # self.sz.setStyleSheet("""QPushButton{background-color:rgb(0, 0, 0, 0);image: url(:/登录界面/settings_24px_h.png);}
        #                               QPushButton:hover{image: url(:/登录界面/settings_24px.png);}
        #                               QPushButton:pressed{image: url(:/登录界面/settings_24px_b.png);}""")
        # self.sz.setObjectName("sz")

        # # logo
        # self.logo = QtWidgets.QLabel(Form)
        # self.logo.setGeometry(QtCore.QRect(10, 350, 200, 200))
        # self.logo.setStyleSheet("background-color: rgb(0, 0, 0, 0);""border-image: url(:/登录界面/wm.png);")
        # self.logo.setText("")
        # self.logo.setObjectName("beijing")

        self.yanzhengma_shuru.raise_()
        self.yanzhengma_xianshi.raise_()
        self.widget.raise_()
        self.username.raise_()
        self.zhuce_bqian.raise_()
        self.password.raise_()
        self.zc_zhanghao.raise_()
        self.mima_bq.raise_()
        self.Jilu_Zhanghao.raise_()
        self.jilu_mima.raise_()
        self.denglu_bt.raise_()
        self.yanzhengma_shuru.raise_()
        self.yanzhengma_xianshi.raise_()
        self.wangji_mima.raise_()
        self.Jilu_Zhanghao.raise_()
        self.yzm_qh.raise_()
        self.touxiang.raise_()
        self.qq.raise_()
        self.wx.raise_()
        self.wb.raise_()

        #$找回密码，重置密码
        self.zhaohuimima = QtWidgets.QWidget(Form)
        self.zhaohuimima.setGeometry(QtCore.QRect(160*a, 110*a, 400*a, 350*a))
        self.zhaohuimima.setStyleSheet("background-color: #407d94;""border-radius: 15px;")
        self.zhaohuimima.close()
        # self.wangji_mima.clicked.connect(self.zhaohuimima.show) #@
        self.zhaohuimima.setObjectName("zhaohuimima")

        self.hudun = QtWidgets.QLabel(self.zhaohuimima)
        self.hudun.setGeometry(QtCore.QRect(140*a, 0, 120*a, 120*a))
        self.hudun.setPixmap(QtGui.QPixmap("登录界面图片/wmlog.png"))
        self.hudun.setScaledContents(True)
        self.hudun.setObjectName("hudun")

        #$新密码输入栏
        self.xinmima = QtWidgets.QLineEdit(self.zhaohuimima)
        self.xinmima.setGeometry(QtCore.QRect(110*a, 130*a, 181*a, 35*a))
        self.xinmima.setMinimumSize(QtCore.QSize(181*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(6*a)
        self.xinmima.setFont(font)
        self.xinmima.setMaxLength(12*a)
        self.xinmima.setObjectName("password")
        self.xinmima.setStyleSheet("background-color: rgb(255, 255, 255);""border-radius: 5px;")
        self.xinmima.setEchoMode(QtWidgets.QLineEdit.Password)

        #$新密码标签
        self.xinmima_bq = QtWidgets.QLabel(self.zhaohuimima)
        self.xinmima_bq.setGeometry(QtCore.QRect(50*a, 130*a, 60*a, 35*a))
        self.xinmima_bq.setMinimumSize(QtCore.QSize(41*a, 35*a))
        self.xinmima_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        # font = QtGui.QFont()
        # font.setFamily("ADMUI3Lg")
        # font.setPointSize(8)
        # self.xinmima_bq.setFont(font)
        self.xinmima_bq.setObjectName("xinmima_bq")

        #$确认密码输入栏
        self.queren_xinmima = QtWidgets.QLineEdit(self.zhaohuimima)
        self.queren_xinmima.setGeometry(QtCore.QRect(110*a, 180*a, 181*a, 35*a))
        self.queren_xinmima.setMinimumSize(QtCore.QSize(181*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(6*a)
        self.queren_xinmima.setFont(font)
        self.queren_xinmima.setMaxLength(12*a)
        self.queren_xinmima.setObjectName("password")
        self.queren_xinmima.setStyleSheet("background-color: rgb(255, 255, 255);""border-radius: 5px;")
        self.queren_xinmima.setEchoMode(QtWidgets.QLineEdit.Password)

        #$确认密码标签
        self.queren_xinmima_bq = QtWidgets.QLabel(self.zhaohuimima)
        self.queren_xinmima_bq.setGeometry(QtCore.QRect(10*a, 180*a, 100*a, 35*a))
        self.queren_xinmima_bq.setMinimumSize(QtCore.QSize(41*a, 35*a))
        self.queren_xinmima_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        # font = QtGui.QFont()
        # font.setFamily("ADMUI3Lg")
        # font.setPointSize(8)
        # self.queren_xinmima_bq.setFont(font)
        self.queren_xinmima_bq.setObjectName("queren_xinmima_bq")

        # # $验证邮箱
        # self.yanzhengyouxiang_bq = QtWidgets.QLabel(self.zhaohuimima)
        # self.yanzhengyouxiang_bq.setGeometry(QtCore.QRect(51, 210, 65, 35))
        # self.yanzhengyouxiang_bq.setMinimumSize(QtCore.QSize(41, 35))
        # self.yanzhengyouxiang_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        # font = QtGui.QFont()
        # font.setFamily("ADMUI3Lg")
        # font.setPointSize(15)
        # self.yanzhengyouxiang_bq.setFont(font)
        # self.yanzhengyouxiang_bq.setObjectName("youxiangyanzheng_srl_bq")
        #
        # #$验证邮箱输入栏
        # self.yanzhengyouxiang_srl = QtWidgets.QLineEdit(self.zhaohuimima)
        # self.yanzhengyouxiang_srl.setGeometry(QtCore.QRect(110, 210, 181, 35))
        # self.yanzhengyouxiang_srl.setMinimumSize(QtCore.QSize(181, 35))
        # font = QtGui.QFont()
        # font.setFamily("宋体")
        # font.setPointSize(12)
        # self.yanzhengyouxiang_srl.setFont(font)
        # self.yanzhengyouxiang_srl.setMaxLength(12)
        # self.yanzhengyouxiang_srl.setObjectName("xinmima")
        # self.yanzhengyouxiang_srl.setStyleSheet("background-color: rgb(255, 255, 255);""border-radius: 5px;")

        #$邮箱验证标签
        self.youxiangyanzhengma_srl_bq = QtWidgets.QLabel(self.zhaohuimima)
        self.youxiangyanzhengma_srl_bq.setGeometry(QtCore.QRect(10*a, 230*a, 100*a, 35*a))
        self.youxiangyanzhengma_srl_bq.setMinimumSize(QtCore.QSize(41*a, 35*a))
        self.youxiangyanzhengma_srl_bq.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        # font = QtGui.QFont()
        # font.setFamily("ADMUI3Lg")
        # font.setPointSize(8)
        # self.youxiangyanzhengma_srl_bq.setFont(font)
        self.youxiangyanzhengma_srl_bq.setObjectName("youxiangyanzheng_srl_bq")

        #$邮箱验证码输入栏
        self.youxiangyanzhengma_srl = QtWidgets.QLineEdit(self.zhaohuimima)
        self.youxiangyanzhengma_srl.setGeometry(QtCore.QRect(110*a, 230*a, 90*a, 35*a))
        self.youxiangyanzhengma_srl.setMinimumSize(QtCore.QSize(90*a, 35*a))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12*a)
        self.youxiangyanzhengma_srl.setFont(font)
        self.youxiangyanzhengma_srl.setMaxLength(4*a)
        self.youxiangyanzhengma_srl.setObjectName("xinmima")
        self.youxiangyanzhengma_srl.setStyleSheet("background-color: rgb(255, 255, 255);""border-radius: 5px;")
        # $确认修改按钮
        self.querenxiugai_bt = QtWidgets.QPushButton(self.zhaohuimima)
        self.querenxiugai_bt.setGeometry(QtCore.QRect(110*a, 290*a, 90*a, 35*a))
        self.querenxiugai_bt.setObjectName("denglu_bt")
        self.querenxiugai_bt.setStyleSheet("QPushButton{background-color: LightCyan ;border-radius: 3px;}"
                                           "QPushButton:hover{background-color:#54FF9F;}"
                                           "QPushButton:pressed{background-color:#43CD80}"
                                           )

        # $取消修改按钮
        self.quxiaoxiugai_bt = QtWidgets.QPushButton(self.zhaohuimima)
        self.quxiaoxiugai_bt.setGeometry(QtCore.QRect(210*a, 290*a, 80*a, 35*a))
        self.quxiaoxiugai_bt.setObjectName("denglu_bt")
        self.quxiaoxiugai_bt.setStyleSheet("QPushButton{background-color: LightCyan ;border-radius: 3px;}"
                                           "QPushButton:hover{background-color:#54FF9F;}"
                                           "QPushButton:pressed{background-color:#43CD80}"
                                           )
        self.quxiaoxiugai_bt.clicked.connect(self.zhaohuimima.close)

        # # $密码不一致提示标签
        # self.mimabuyizhi = QtWidgets.QLabel(self.zhaohuimima)
        # self.mimabuyizhi.setGeometry(QtCore.QRect(300, 180, 140, 35))
        # font = QtGui.QFont()
        # font.setFamily("宋体")
        # font.setPointSize(10)
        # self.mimabuyizhi.setFont(font)
        # self.mimabuyizhi.setStyleSheet("background-color: rgb(0, 0, 0, 0);""color:red")
        # self.mimabuyizhi.close()
        # self.mimabuyizhi.setObjectName("mimabuyizhi")

        # $获取验证码按钮
        self.huoquyanzhengma_bt = QtWidgets.QPushButton(self.zhaohuimima)
        self.huoquyanzhengma_bt.setGeometry(QtCore.QRect(210*a, 230*a, 81*a, 35*a))
        self.huoquyanzhengma_bt.setObjectName("denglu_bt")
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(6*a)
        self.huoquyanzhengma_bt.setFont(font)
        self.huoquyanzhengma_bt.setStyleSheet("QPushButton{background-color: LightCyan ;border-radius: 3px;}"
                                           "QPushButton:hover{background-color:#54FF9F;}"
                                           "QPushButton:pressed{background-color:#43CD80}"
                                           )
        # $邮箱验证码错误
        # self.youxiangyanzhengmacuowu = QtWidgets.QLabel(self.zhaohuimima)
        # self.youxiangyanzhengmacuowu.setGeometry(QtCore.QRect(110, 260, 200, 35))
        # self.youxiangyanzhengmacuowu.setMinimumSize(QtCore.QSize(41, 35))
        # self.youxiangyanzhengmacuowu.setStyleSheet("background-color: rgb(0, 0, 0, 0);""color:red;")
        # self.youxiangyanzhengmacuowu.close()  # $验证码错误提示标签默认关闭状态
        # font_zh = QtGui.QFont()
        # font_zh.setFamily("ADMUI3Lg")
        # font_zh.setPointSize(15)
        # self.youxiangyanzhengmacuowu.setFont(font_zh)
        # self.youxiangyanzhengmacuowu.setObjectName("youxiangyanzhengmacuowu")

        self.yx.raise_()
        self.px.raise_()
        self.gb.raise_()
        self.zxh.raise_()
        self.mimacuowu.raise_()
        # self.sz.raise_()
        # self.logo.raise_()
        self.yanzhengmacuowu.raise_()
        self.zhaohuimima.raise_()
        self.xinmima.raise_()
        self.queren_xinmima.raise_()
        self.xinmima_bq.raise_()
        self.queren_xinmima_bq.raise_()
        # self.zhaohuimima_gb.raise_()
        self.querenxiugai_bt.raise_()
        # self.yanzhengyouxiang_bq.raise_()
        # self.yanzhengyouxiang_srl.raise_()
        self.hudun.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # $

    def initDrag(self):
        # 设置鼠标跟踪判断扳机默认值
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

        # $

    def initTitleLabel(self):
        # 安放标题栏标签
        self._TitleLabel = QTitleLabel(self)
        self._TitleLabel.setGeometry(QtCore.QRect(0*a, 0, 401*a, 31*a))
        self._TitleLabel.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self._TitleLabel.setMouseTracking(True)  # 设置标题栏标签鼠标跟踪（如不设，则标题栏内在widget上层，无法实现跟踪）
        self._TitleLabel.setIndent(10*a)  # 设置标题栏文本缩进
        self._TitleLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self._TitleLabel.move(0, 0)  # 标题栏安放到左上角

        # $

    def mousePressEvent(self, event):
        self._move_drag = True
        self.move_DragPosition = event.globalPos() - self.pos()
        event.accept()

    # $

    def mouseMoveEvent(self, QMouseEvent):
        self.setCursor(Qt.ArrowCursor)
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        # 没有定义左方和上方相关的5个方向，主要是因为实现起来不难，但是效果很差，拖放的时候窗口闪烁，再研究研究是否有更好的实现
        if Qt.LeftButton and self._right_drag:
            # 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._corner_drag:
            # 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._move_drag:
            # 标题栏拖放窗口位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()
        # $

    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放后，各扳机复位
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

    def shuaxin(self):
        img, self.content = yanzhengma.get_code()
        tp_path = 'hupian.jpg'
        img.save(tp_path)
        self.yanzhengma_xianshi.setPixmap(QtGui.QPixmap(tp_path))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.zhuce_bqian.setText(_translate("Form", "账 号"))
        self.zc_zhanghao.setText(_translate("Form", "注册账号"))
        self.mima_bq.setText(_translate("Form", "密 码"))
        self.Jilu_Zhanghao.setText(_translate("Form", "记住密码"))
        self.jilu_mima.setText(_translate("Form", "自动登陆"))
        self.denglu_bt.setText(_translate("Form", "登 录"))
        self.wangji_mima.setText(_translate("Form", "忘记密码?"))
        self.yzm_qh.setText(_translate("Form", "看不清换一张"))
        # self.yanzhengmacuowu.setText(_translate("Form", "验证码错误！"))
        self.mimacuowu.setText(_translate("Form", "密码错误！"))
        self.xinmima_bq.setText(_translate("Form", "新密码"))
        self.queren_xinmima_bq.setText(_translate("Form", "确认新密码"))
        self.youxiangyanzhengma_srl_bq.setText(_translate("Form", "邮箱验证码"))
        self.querenxiugai_bt.setText(_translate("Form", "确认修改"))
        self.quxiaoxiugai_bt.setText(_translate("Form", "取消修改"))
        # self.yanzhengyouxiang_bq.setText(_translate("Form", "验证邮箱"))
        # self.mimabuyizhi.setText(_translate("Form", "密码不一致！"))
        self.huoquyanzhengma_bt.setText(_translate("Form", "获取验证码"))
        # self.youxiangyanzhengmacuowu.setText(_translate("Form", "邮箱验证码错误，请重新输入！"))

class WanMaDicot(QtWidgets.QWidget, Ui_Form_dljm):

	def __init__(self):
		super().__init__() # 初始化父类构造方法
		self.setupUi(self) # 调用父类属性设置方法

if __name__ == "__main__":
    import dljm_sc
    import tp
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = WanMaDicot()   #MyForm是自己的窗体类名
    # t=myapp.sousuo_shurulan.text()
    # print(len(t))

    myapp.show()
    # myapp.fanyi_button.clicked.connect(shurulan.slot_method)
    sys.exit(app.exec_())

