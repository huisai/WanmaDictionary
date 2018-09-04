import sys
from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui  import QPixmap
from PyQt5.QtCore import pyqtSignal,Qt,QObject,QByteArray,QBuffer
import time
import re
import hashlib
from threading import Thread,Event
import os
from .zhujiemian import Ui_Form_zhujiemian
from .dljiemian import Ui_Form_dljm, yanzhengma
from .gerenziliao import Ui_Form_gerenziliao
from .danciben import Ui_Form_danciben
from .zc_jm import  Ui_Form_zc_jm
from .tanchuang import Ui_Form
from .clientRecv import *   #RecvThread,commuite,load_hist,read_pw,write_pw
from .yunyin import *
from .tool import *


HIST = {}
FONT_SIZE =17
log_state = False  # 登录状态false为未登录，true为已登录
ATUOLOG = False    #是否自动登陆默认未false
SENDED_AUTOLOG = False
# ip = '176.122.15.110'
ip = '172.28.34.4'
# ip = '176.122.15.74'
path_yuyin = os.path.join('temp','mp3')
sockfd = 0

#主窗口
class Z_class(QWidget, Ui_Form_zhujiemian):
    signal_xsl = pyqtSignal(tuple)    #改变显示局域栏的值
    # signal_liju = pyqtSignal(list)    #接收例句的信号

    def __init__(self,dl):
        super().__init__()
        self.setupUi(self)
        self.word_fanhui = ''
        self.dl = dl            #将登陆用户名和密码传进来@
        self.user = ''
        self.passw = ''
        self.show()
        self.sousuo_shurulan_01.setFocus()
        self.signal_xsl.connect(self.slot_method)  # 自定义信号和槽函数绑定@
        self.fanyi_button.clicked.connect(self.fanyi_click) # 翻译图标点击信号连接@，放到子类下
        # self.sousuo_shurulan.enterPressed.connect(self.fanyi_click)
        self.jrdcb_button.clicked.connect(self.jrdc_click)  #加入单词本点击信号连接 @
        self.gb.clicked.connect(self.close)   #关闭
        self.sousuo_shurulan_01.returnPressed.connect( self.fanyi_click)  # 回车信号绑定到槽。
        self.zhuxiaodenglu_button.clicked.connect(self.slot_zhuxiaodl)  #注销登陆按钮点击连接
        self.yuyinshuru_button.clicked.connect(self.yunyinshuru_clicked)  # @语音输入按钮连接
        self.jiesushuru.clicked.connect(self.jieshuly_clicked)  # @开始录音
        self.yuyin_button.clicked.connect(self.yuyinbf_clicked)
        self.jiepingfanyi_button.clicked.connect(self.jiepingbf_clicked)
        self.szl_ok.clicked.connect(self.szok_clicked)
        self.meiricihui_button.clicked.connect(self.qchuancun)

    def init_zjm(self):  # 显示窗体2
        # 检查是否可以自动登陆
        self.user,self.passw = read_pw(filename="al")    #先注释，方便测试
        if self.passw:
            data = "L " + self.user + ' ' + self.passw
            sockfd_send(data.encode())
            print("自动登陆请求")
            set_quanju('SENDED_AUTOLOG',True)
        print('执行init_zjm')
        self.token = get_token()  #在窗口初始化时获取百度token
        # self.show()

    # def zhujiemian_close(self):
    def close(self):
        if ATUOLOG and log_state:
            write_pw(self.dl.user,self.dl.passw,filename="al")
        else:
            if not SENDED_AUTOLOG:
                write_pw(self.dl.user, filename="al")
        # self.close()
        super(Z_class,self).close()

    # def keyPressEvent(self, e):    #可使用该方法捕获回车
    #     print(e.key())
    #     # if e.key() == Qt.Key_Enter:
    #     if e.key() == 16777220:
    #         self.fanyi_click()

    def fanyi_click(self):      #翻译图标点击信号槽函数@
        txt = self.sousuo_shurulan_01.text().strip().replace('\n',' ') # 获取输入框信息,后需添加中英文判段，句子判断
        if txt == '$%^456':
            print(s)
        if not txt:
            return
        self.word_shuru = txt
        if ' ' in txt or is_cn(txt):
            sockfd_send(b'U ' + txt.encode())
            return
        if log_state:
            sockfd_send(b'Q ' + txt.encode())
        else:
            sockfd_send(b'G ' + txt.encode())
        self.xianshilan.clear()

    def slot_method(self,t):   #添加参数t，为要显示的数据@
         # 输出信息
        # text = self.sousuo_shurulan.text() #获取输入框信息
        print('slot_method:',t[0],self.word_shuru)
        if t[0].lower() == self.word_shuru.lower():    #当返回的单词 和 输入并点查询的单词 是一致时才显示，否则不显示
            if ' ' in t[0] or is_cn(t[0]):    #判断是否标准单个英文单词返回
                trans = "\n\n"
                for x in t[1:]:
                    trans += x + '\n'
            else:
                trans = "%s\n音标:%s\n单词释义:%s\n是否牛津三千核心词汇:%s\n标签:%s\n英国国家语料库词频顺序:%s\n当代语料库词频顺序:%s" % t
            print('trans=', trans)
            self.xianshilan.clear()
            self.xianshilan.insertPlainText(trans+'\n')
            self.word_fanhui = t[0]  #保证点收藏时，收藏的单词时详细翻译框中的单词

            # if self.word_fanhui in HIST:
            #     HIST[self.word_fanhui][1] += 1
            # else:
            #     HIST[self.word_fanhui] = [t[2],1,0]
            # print('我准备执行toPlainText()')
            # a= self.sousuo_shurulan.toPlainText()
            # a = self.sousuo_shurulan.text()   #有道注释掉@
            # print(a)
            # x=youfy.fanyi_youdao(a)       #有道注释掉@
        # x = 'hello'
        # print('显示方法',x)

        #         #显示框自动跳到底部
        #         # self.shuchu_edit.moveCursor(+End)

    def jrdc_click(self):
        if self.word_fanhui:
            if log_state:
                sockfd_send(('W '+self.word_fanhui).encode())
            else:
                tc.show_tc('您尚未登陆\n请登陆后收藏单词')

    def slot_zhuxiaodl(self):
        sockfd_send(b'O')          #向服务端发送注销登陆请求
        self.xiaxian()
        tc.show_tc("你已注销登陆")

    def yunyinshuru_clicked(self):
        self.__e = Event()
        self.__e.set()
        ps = Thread(target=my_record,args=(self.__e,))
        self.yuyinshuruxx.show()
        ps.start()

        # ps.join()

    def jieshuly_clicked(self):
        self.__e.clear()
        self.__e.wait(4)
        word = get_word(self.token)
        if word == "!@#":
            tc.show_tc('识别失败，\n请提高录音质量')
            self.yuyinshuruxx.close()
        else:
            self.sousuo_shurulan_01.setText(word)
            self.fanyi_click()
            self.yuyinshuruxx.close()

    def yuyinbf_clicked(self):
        filename = self.word_fanhui +".mp3"
        filename =os.path.join(path_yuyin, filename)
        try:
            play_mp3(filename,4.5)
        except Exception:
            tc.show_tc("找不到语音")

    def jiepingbf_clicked(self):
        import win32api
        import baiduImg
        def on_clipboard_change():
            img = clipboard.image()
            if img:
                data = QByteArray()
                buf = QBuffer(data)
                img.save(buf, 'PNG')
                s = data.toBase64()
                # print(type(s))     #<class 'PyQt5.QtCore.QByteArray'>，但打印出来就是一个字节串的格式
                # print(type(bytes(s)))   #百度接口需要bytes 的对象
                content = baiduImg.get_word_img(bytes(s),self.token)   #调用百度接口获取识别内容
                if content:
                    self.sousuo_shurulan_01.setText(content)
                    self.fanyi_click()
                else:
                    tc.show_tc("识别失败")
                clipboard.dataChanged.disconnect(on_clipboard_change)  # 解除连接
                os.system("taskkill /IM SnippingTool.exe")  # 强制关闭截图工具

        win32api.ShellExecute(0, 'open', 'SnippingTool.exe', 'new', '', 1)    #打开自带截图工具
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(on_clipboard_change)

    def szok_clicked(self):
        # ip地址正则
        pattern = r"(?=(\b|\D))(((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))(?=(\b|\D))"
        ip = self.shezhi_shurulan.text().strip()
        r = re.match(pattern, ip)
        if not r:
            tc.show_tc('请输入正确的\nip地址')
            self.szl_ok.close()
            self.shezhi_shurulan.close()
            return
        if not sockfd:
            set_quanju('sockfd',ip)
            if sockfd:
                creat_thread()
                tc.show_tc('已连接服务器')
                self.shezhi_shurulan.close()
                self.szl_ok.close()
            else:
                tc.show_tc('请输入正确的\n服务器地址')
                self.szl_ok.close()
                self.shezhi_shurulan.close()
        else:
            print(1)
            self.szl_ok.clear()
            print(2)
            self.szl_ok.close()

    def shangxian(self):
        if self.dl.user:
            print('shangxian1')
            set_quanju('log_state', self.dl.user + ' ' + self.dl.passw)
        elif self.user:
            print('shangxian2')
            set_quanju('log_state', self.user + ' ' + self.passw)
        print('shangxian3')
        self.denglu_button.close()
        self.zhuxiaodenglu_button.show()

    def xiaxian(self):
        set_quanju('log_state', False)
        self.denglu_button.show()
        self.zhuxiaodenglu_button.close()  #

    def qchuancun(self):
        pth =get_path('mp3','')
        filist = os.listdir(pth)
        print(filist)
        for x in filist:
            os.remove(os.path.join(pth,x))

# 登陆界面
class Dl_class(QWidget, Ui_Form_dljm):
    signal_dl = pyqtSignal(str)
    signal_gbxgmm = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user = ''
        self.passw = ''
        # self.signal_dl.connect(self.recv_dl)   #接收登陆信息的自定义信号与槽函数连接@
        self.denglu_bt.clicked.connect(self.slot_dl_btn)  #登陆按钮的点击与槽函数链接@
        self.Jilu_Zhanghao.stateChanged.connect(self.jlmima_change)   #记录密码连接@
        self.jilu_mima.stateChanged.connect(self.zddenglu_change)      #自动登陆连接@
        # 点击登录界面右上角关闭按键，关闭登录界面退出程序
        self.gb.clicked.connect(self.close_dljm)
        self.wangji_mima.clicked.connect(self.wjmm_clicked)
        self.querenxiugai_bt.clicked.connect(self.xiugaimm_clicked)
        # self.yanzhengma_shuru.textChanged.connect(self.qingchutishi)
        self.huoquyanzhengma_bt.clicked.connect(self.sendyzm)
        self.signal_gbxgmm.connect(self.closs)

    def closs(self):
        print('self.zhaohuimima.close()')
        self.zhaohuimima.close()

    def close_dljm(self):  # 点击按钮将窗体1关掉
        self.yanzhengma_shuru.clear()
        self.password.clear()
        self.username.clear()
        self.close()

    def show_dljm(self):
        if not log_state:
            self.list_u = read_pw()  # 读取密码列表
            print('登陆界面读取了read_pw', self.list_u)
            set_quanju('SENDED_AUTOLOG', False)
            self.show()
        else:
            print('不可能出现')
            Z_Jm.xiaxian()
            sockfd_send(b'O ')

    def jlmima_change(self,state):
        # print('1bian')
        if state == Qt.Checked:
            pass
        else:
            if self.jilu_mima.isChecked():
                self.jilu_mima.toggle()

    def zddenglu_change(self,state):
        if state == Qt.Checked:
            if not self.Jilu_Zhanghao.isChecked():
                self.Jilu_Zhanghao.toggle()
            set_quanju('ATUOLOG',True)
        else:
            set_quanju('ATUOLOG',False)

    def slot_dl_btn(self):          #登陆按钮的点击相连接的槽函数@
        try:
            username = self.username.text()
            psw = self.password.text()
            psw = hashlib.md5(psw.encode('utf-8')).hexdigest()
            yanzhengma = self.yanzhengma_shuru.text()
            if (not username) or (not psw) or (not yanzhengma):
                # tc = TC("请输入完整信息")
                tc.show_tc("请输入完整信息")
                return
            if ' ' in username or ' ' in psw:
                tc.show_tc("密码和用户名不能含有空格")
                return
            yanzhengma = yanzhengma.lower()
            if yanzhengma != self.content.lower():
                self.yanzhengmacuowu.show()
                print("提示验证码不正确",self.content.lower())
                tc.show_tc("验证码不正确"+self.content.lower())
                self.yanzhengma_shuru.clear()
                self.yanzhengma_shuru.setFocus()
                # self.password.clear()
                return
            print(username, psw, yanzhengma, self.content.lower())
            data = "L "+username+' '+psw
            self.user = username
            self.passw = psw
            sockfd_send(data.encode())
        except Exception as e:
            print(e)
            tc.show_tc("登陆失败")

    def wjmm_clicked(self):
        self.__username_xg = self.username.text()
        if not self.__username_xg:
            tc.show_tc('请先输入用户名')
            self.username.setFocus()
            return
        print('self.__username_xg',self.__username_xg)
        self.xinmima.clear()
        self.queren_xinmima.clear()
        self.youxiangyanzhengma_srl.clear()
        self.zhaohuimima.show()

    def sendyzm(self):
        sockfd_send(('T '+ self.__username_xg).encode())

    def xiugaimm_clicked(self):
        psw = self.xinmima.text()
        psw2 = self.queren_xinmima.text()
        yzm = self.youxiangyanzhengma_srl.text()
        if not psw or not psw2 or not yzm:
            tc.show_tc('不能为空')
            return
        if  ' ' in psw or ' ' in yzm or ' ' in self.__username_xg:
            tc.show_tc('用户名或密码不能\n含有空格')
            return
        if psw != psw2:
            tc.show_tc('两次密码必须一致')
            self.queren_xinmima.clear()
            self.queren_xinmima.setFocus()
            return
        psw = hashlib.md5(psw.encode('utf-8')).hexdigest()
        data = "V " + self.__username_xg + " " + psw + " " + yzm
        sockfd_send(data.encode())

    def qingchutishi(self):
        self.mimacuowu.close()
        self.yanzhengmacuowu.close()
    # def recv_dl(self,t):
    #     # 接收B，调用登录方法
    #     if t == 'S':
    #         print('登录成功')
    #         # 界面－登录成功提示
    #         # 设置登录标志位
    #         set_quanju('log_state',True)
    #         print("进入4")
    #         # 保存账号密码
    #         if self.Jilu_Zhanghao.isChecked():
    #             print(self.user, self.passw)
    #             write_pw(self.user,self.passw,self.list_u)
    #             print("已记录密码")
    #         else:
    #             write_pw(self.user, list_u=self.list_u)
    #         self.close_dljm()
    #     elif t == 'F':
    #         print('登录失败')
    #         # 界面－登录成功提示
    #         # 设置登录标志位
    #     elif t == "Z":
    #         print('被挤下线')
    #     elif t == "N":
    #         print('邮箱未验证')

# 数据接收处理方法封装在此类
class DoRecv(QObject):
    signal_liju = pyqtSignal(list)  # 接收例句的信号
    signal_showtc = pyqtSignal(str)  #弹窗提示
    sig_zhaobudao = pyqtSignal(str)


    def __init__(self, Dl_jm, zhujm, Dcb_Jm):
        self.dl_jm = Dl_jm
        self.zhujm = zhujm
        self.dcb_jm = Dcb_Jm
        super().__init__()
        self.sig_zhaobudao.connect(self.zhaobudao)
        self.signal_liju.connect(self.recv_liju)


    def recv_dl(self, t):
        # 接收B，调用登录方法
        if t == 'S':
            print('登录成功','SENDED_AUTOLOG',SENDED_AUTOLOG)
            # 界面－登录成功提示
            # 设置登录标志位
            # 保存账号密码
            if not SENDED_AUTOLOG:
                if self.dl_jm.Jilu_Zhanghao.isChecked():
                    print('not SENDED_AUTOLOG',self.dl_jm.user, self.dl_jm.passw)
                    write_pw(self.dl_jm.user, self.dl_jm.passw, self.dl_jm.list_u)
                else:
                    write_pw(self.dl_jm.user, list_u=self.dl_jm.list_u)
                self.dl_jm.close_dljm()
            self.zhujm.shangxian()
        elif t == 'F':
            print('登录失败用户名或密码有误')
            tc.show_tc('登录失败\n用户名或密码有误')
            self.dl_jm.password.clear()
            # 界面－登录成功提示
            # 设置登录标志位
        elif t == "Z":
            if not log_state:
                tc.show_tc("你的账号已在别处\n登陆")
        elif t == "N":
            tc.show_tc('你的邮箱未验证\n请先验证邮箱')

    def recv_liju(self,t):
        if t[0] == self.zhujm.word_shuru:
            self.zhujm.xianshilan.insertPlainText('例句：\n')
            for i in t[1:]:
                for j in i:
                    self.zhujm.xianshilan.insertPlainText(j+'\n')

    def zhaobudao(self,t):
        if Z_Jm.word_shuru == t:
            Z_Jm.xianshilan.clear()
            Z_Jm.xianshilan.setText("找不到该单词")

# 注册界面
class Zc_class(QWidget, Ui_Form_zc_jm):
    signal_zc = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.zhuce_button.clicked.connect(self.zhuce_btn_click)
        self.signal_zc.connect(self.recv_zc)
        self.gb.clicked.connect(self.zcjm_close)

    def zcjm_close(self):  # 窗体2
        self.qingchusrl()
        self.close()

    def zhuce_btn_click(self):
        username = self.nc_shuru.text()
        psw = self.denglumimashuru.text()
        psw2 = self.querenmima_shuru.text()
        if not username or not psw or not psw2:
            tc.show_tc('用户名或密码\n不能为空')
            return
        if ' ' in username or ' ' in psw:
            tc.show_tc('密码和用户名\n不能含有空格')
            return
        if psw != psw2:
            tc.show_tc('两次密码必须一致')
            self.querenmima_shuru.clear()
            self.querenmima_shuru.setFocus()
            return
        email = self.youxiang_shuru.text()
        pattern = '^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}'
        r = re.match(pattern,email)
        if not r:
            tc.show_tc('邮箱格式不正确')
            self.youxiang_shuru.setFocus()
            return
        psw = hashlib.md5(psw.encode('utf-8')).hexdigest()
        print('发送登陆信息')
        data = "R "+username+' '+psw+" "+email
        sockfd_send(data.encode())

    def qingchusrl(self):
        self.nc_shuru.clear()
        self.denglumimashuru.clear()
        self.querenmima_shuru.clear()
        self.youxiang_shuru.clear()

    def recv_zc(self,t):
        if t == 'S':
            tc.show_tc('注册成功')
            self.qingchusrl()
            self.close()
            # 界面－注册成功提示
        elif t == 'F':
            tc.show_tc('注册失败\n用户名已存在')
            # 界面－注册成功提示
        elif t == 'N':
            tc.show_tc('该邮箱已注册\n可使用邮箱登陆')
        else:
            print('???')

# 个人资料界面
class Grzl_class(QWidget, Ui_Form_gerenziliao):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def show_gerenziliao(self):
        self.show()

    def close_gerenziliao(self):
        self.close()

# 单词本界面
class Dcb_class(QWidget, Ui_Form_danciben):
    signal_dcb = pyqtSignal(list, list)  # 接收单词本的信号

    def __init__(self,zjm):
        super().__init__()
        self.zjm = zjm
        self.setupUi(self)
        self.page = 0
        self.dcb = []
        self.row = [self.shoucang_01, self.shoucang_02, self.shoucang_03, self.shoucang_04, self.shoucang_05, \
                    self.shoucang_06, self.shoucang_07, self.shoucang_08, self.shoucang_09, self.shoucang_10, ]
        self.fanyi = (self.fanyi_button, self.fanyi_button_02, self.fanyi_button_03, self.fanyi_button_04, self.fanyi_button_05, \
               self.fanyi_button_06, self.fanyi_button_07, self.fanyi_button_08, self.fanyi_button_09, self.fanyi_button_10)
        for x in self.fanyi:
            x.clicked.connect(self.slot_fanyi)
        self.shanchu = (self.sc_srl_button, self.sc_srl_button_02, self.sc_srl_button_03, self.sc_srl_button_04, self.sc_srl_button_05, \
                   self.sc_srl_button_06, self.sc_srl_button_07, self.sc_srl_button_08, self.sc_srl_button_09, self.sc_srl_button_10)
        for x in self.shanchu:
            x.clicked.connect(self.slot_shanchu)
        self.shangyiye_bt.clicked.connect(self.slot_shangyiye)
        self.xiayiye_bt.clicked.connect(self.slot_xiayiye)

        self.signal_dcb.connect(self.recv_dcb)

    def show_danciben(self):
        if log_state:
            if not self.dcb or True:
                sockfd_send(b'H ')
            self.show()
        else:
            tc.show_tc("请先登陆")


    def close_danciben(self):
        self.close()


    def recv_dcb(self,lishi,dcb):
        for x in dcb:
            item = x[0]+':  '+str(x[1].replace('\n',';'))
            if len(item) > 30:
                item = item[:30]+'...'
            self.dcb.append(item)
        # self.dcb = [x[0]+':  '+str(x[1].replace('\n',';')) for x in dcb]
        print('self.dcb=',len(self.dcb))
        self.get_dcb()

    def get_dcb(self):
        if len((self.dcb)) < 10+self.page:
            end = (len(self.dcb)) % 10
            for x in range(10):
                self.shanchu[x].close()  # 隐藏删除和翻译按钮
                self.fanyi[x].close()
                self.row[x].clear()
            # if self.get_dcb() <=10:
            #     self.xiayiye_bt.close()
            #     self.shangyiye_bt.close()
        else:
            end = 10
            # self.xiayiye_bt.show()
            # self.shangyiye_bt.show()
        for i in range(end):
            txt = self.dcb[i+self.page]
            self.row[i].setText(txt)
            self.fanyi[i].show()
            self.shanchu[i].show()


    def slot_fanyi(self):
        sender = self.sender()
        i = self.fanyi.index(sender)
        txt = self.row[i].toPlainText().split(':  ')[0]
        self.close()
        self.zjm.sousuo_shurulan_01.setText(txt)
        self.zjm.fanyi_click()

    def slot_shanchu(self):
        sender = self.sender()
        i = self.shanchu.index(sender)
        txt = self.row[i].toPlainText()
        print('txt=', txt)
        self.dcb.remove(txt)
        print('self.dcb=',self.dcb)
        word = txt.split(':  ')[0]
        print('word=', word)
        sockfd_send(('X '+ word).encode())
        self.get_dcb()

    def slot_shangyiye(self):
        if self.page - 10 >= 0:
            self.page -= 10
            self.get_dcb()

    def slot_xiayiye(self):
        if self.page +10 <= len(self.dcb):
            self.page += 10
            self.get_dcb()

#消息提示窗口
class TC(QWidget,Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def show_tc(self,s):
        self.tishilan.setText(s)
        self.show()


def do_thread(tc,Dl_Jm,Zczh_Jm,z_jm,do_recv,dcb_jm):              #创建子线程@
    while True:
    #读取登陆状态
        if sockfd:
            rt = RecvThread(sockfd,Dl_Jm,Zczh_Jm,z_jm,do_recv,dcb_jm)
        set_quanju('sockfd')  #断开连接后马上检测是否能重连
        if not sockfd:
            do_recv.signal_showtc.emit("服务器断开连接")
            print('子线程结束')
            break
        else:
            if log_state:
                sockfd.send(('L ' + log_state).encode())    #断线重连后重新登陆,并继续进入监听
                print('短线重连后重新登陆')



def set_quanju(name,b=True):      #设置全局变量
    global log_state, ATUOLOG, SENDED_AUTOLOG,sockfd,ip
    if name == 'log_state':
        log_state = b
    elif name == 'ATUOLOG':
        ATUOLOG = b
    elif name == 'SENDED_AUTOLOG':
        SENDED_AUTOLOG = b
        print('已设置SENDED_AUTOLOG为：',b)
    elif name == "sockfd":
        if b == True:
            b = ip
        else:
            ip = b
        sockfd = communite(b)



# 定义数据发送函数，若创建套接字成功则直接发送，否则创建套接字，并检查是否已登陆（能在意外断开连接后继续自动重连，登陆）
def sockfd_send(s):
    if not sockfd:
        set_quanju('sockfd')
        if not sockfd:
            tc.show_tc("服务器未连接，\n请检查网络")
            return
        else:
            creat_thread()      #断开连接后监听子线程会结束，重连成功后应再次启动子线程
            if log_state:
                sockfd.send(('L ' + log_state).encode())    #短线重连后重新登陆
                time.sleep(0.1)    #防止毡包
                print('短线重连后重新登陆',log_state)
            print('短线重连后发送消息')
    sockfd.send(s)
    print('发送了',s)

# 创建接收监听子线程
def creat_thread():
    tp = Thread(target=do_thread, args=(tc,Dl_Jm,Zczh_Jm, Z_Jm,do_recv,Dcb_Jm))  # 创建接收监听线程@
    tp.daemon = True
    tp.start()

set_quanju('sockfd')
app = QApplication(sys.argv)
Dl_Jm = Dl_class()
Z_Jm = Z_class(Dl_Jm)
Zczh_Jm = Zc_class()
Grzl_Jm = Grzl_class()
Dcb_Jm = Dcb_class(Z_Jm)
do_recv = DoRecv(Dl_Jm, Z_Jm, Dcb_Jm)
tc = TC()
creat_thread()

# 弹窗提示
do_recv.signal_showtc.connect(tc.show_tc)
# 接收登陆信息的自定义信号与槽函数连接@
Dl_Jm.signal_dl.connect(do_recv.recv_dl)
#点击登录按钮关闭登录界面
# Dl_Jm.denglu_bt.clicked.connect(Dl_Jm.close_dljm)
#点击注册账号，跳转注册界面
Dl_Jm.zc_zhanghao.clicked.connect(Zczh_Jm.show)
#主界面登录按键跳转登录界面
Z_Jm.denglu_button.clicked.connect(Dl_Jm.show_dljm)
#主界面注册账号按键跳转注册界面
Z_Jm.zhucezhanghao_button.clicked.connect(Zczh_Jm.show)
#主界面个人资料按键跳转个人资料界面
Z_Jm.gerenziliao_button.clicked.connect(Grzl_Jm.show_gerenziliao)
# 个人资料界面返回主界面按键跳转主界面并关闭个人资料界面
Grzl_Jm.fanhuizhujiemian_button.clicked.connect(Grzl_Jm.close_gerenziliao)
# 主界面单词本按键跳转单词本界面
Z_Jm.danciben_button.clicked.connect(Dcb_Jm.show_danciben)
# 单词本界面返回主界面按键跳转主界面并关闭单词本界面
Dcb_Jm.fanhuizhujiemian_button.clicked.connect(Dcb_Jm.close_danciben)

Z_Jm.init_zjm()
sockfd_send('通信测试，无需理会'.encode())
app.exec_()

