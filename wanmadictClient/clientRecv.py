#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os


class RecvThread():
    # 接收模块初始化
    def __init__(self, sockfd, Dl_Jm, zc, Z_Jm,dorecv_main,dcb_jm):
        # 将窗口对象传入，用于接收数据后向各个对象发送信号
        self.sockfd = sockfd
        self.dl_jm = Dl_Jm
        self.z_jm = Z_Jm
        self.zc = zc
        self.dcb_jm = dcb_jm
        self.dorecv_main = dorecv_main
        self.do_recv()    #初始化完成进入接收等待监听

     # 接收Ａ，调用注册方法  已测试ok
    def rec_zhuce(self,t):
        self.zc.signal_zc.emit(t)

    # 接收B，调用登录方法  已测试ok
    def rec_denglu(self,t):
        self.dl_jm.signal_dl.emit(t)
        print('发送了登陆信号',t)
        # if t == 'S':
        #     print('登录成功')
        #     self.app.set_shangxian()
        #     self.app.second()
        #     # 界面－登录成功提示
        #     # 设置登录标志位
        # elif t == 'F':
        #     print('登录失败')
        #     # 界面－登录成功提示
        #     # 设置登录标志位
        # elif t == "Z":
        #     print('被挤下线')
        #     # self.app.set_xiaxian()
        # elif t == "N":
        #     print('邮箱未验证')

    # 接收Ｃ，t是元组（单词，音标，翻译．．．）  已测试ok
    def rec_fanyi(self,t):
        # 获取单前单词word
        # if t[0] == word:
        d = {'zk':"中考",'gk':'高考','cet4':'四级','cet6':'六级','ky':'考研','toefl':'托福','ielts':'雅思','gre':'GRE'}
        t = eval(t)
        t = list(t)
        if t[3]:
            t[3] = t[3].replace('1', '是')
        else:
            t[3] = t[3].replace('', '否')
        if t[4]:
            for i in t[4].split(' '):
                t[4] = t[4].replace(i,d[i])
        t = tuple(t)
        self.z_jm.signal_xsl.emit(t)
        print('z_jm.signal_xsl:',t)
        # for x in t[1:]:
        #     pass

    # 接收D  已测试ok
    def rec_lishi(self,t):
        t = eval(t)
        lishi = [(x[0],x[1],x[2]) for x in t]
        shoucang = [(x[0],x[1]) for x in t if x[3] == 1]
        print('shoucang=',shoucang)
        self.dcb_jm.signal_dcb.emit(lishi,shoucang)

    # 接收E  已测试ok
    def rec_liju(self,t):
        t = eval(t)
        self.dorecv_main.signal_liju.emit(t)

    # 接收F 发音  已测试ok
    def rec_fayin(self,t):
        word = t[0].decode()
        path0 = os.path.split(os.path.realpath(__file__))[0]
        path1 = os.path.join(path0,'temp','mp3')
        filename = os.path.join(path1,word+'.mp3')
        print(filename)
        if not os.path.exists(path0):
            os.mkdir(path0)
        with open(filename,'wb') as f:
            f.write(t[1])

    # 接收G
    def rec_xiugaimm(self,t):
        if t == 'S':
            self.dorecv_main.signal_showtc.emit("密码修改成功！")
            self.dl_jm.signal_gbxgmm.emit()
        elif t == 'F':
            self.dorecv_main.signal_showtc.emit("验证码不正确！")
        elif t == 'N':
            self.dorecv_main.signal_showtc.emit("用户名不存在！")

    # 接收H 找不到单词  已测试ok
    def rec_zhaobudao(self,t):
        self.dorecv_main.sig_zhaobudao.emit(t)

    # I 服务端发送邮箱验证码返回信息
    def rec_yzmhou(self,t):
        if t == 'S':
            self.dorecv_main.signal_showtc.emit("已向用户邮箱\n发送验证码！")
        elif t == 'F':
            self.dorecv_main.signal_showtc.emit("该用户不存在！")

    #J 修改密码返回信息
    def rec_xgmmhou(self,t):
        if t == 'S':
            self.dorecv_main.signal_showtc.emit("密码已修改！")
            self.dl_jm.signal_gbxgmm.emit()
        elif t == 'F':
            self.dorecv_main.signal_showtc.emit("邮箱验证码不正确\n密码修改失败！")

    #U 非英文单词查询返回
    def rec_nonword(self,t):
        t = eval(t)
        t.reverse()
        t = tuple(t)
        print(t)
        self.z_jm.signal_xsl.emit(t)



    def do_recv(self):
        # 根据通信协议，解析报文后将接收到的内容分发各个处理函数进行处理，建立报文指令与处理函数的映射
        self.fun_map = {'A':self.rec_zhuce,'B':self.rec_denglu,\
        'C':self.rec_fanyi,'D':self.rec_lishi, 'E':self.rec_liju, 'F':self.rec_fayin,\
                        'G':self.rec_xiugaimm, 'H':self.rec_zhaobudao,'I':self.rec_yzmhou,\
                        'J':self.rec_xgmmhou, 'U':self.rec_nonword}
        print('dothread')
        data0 =b''
        while True:
            data0 += self.sockfd.recv(2048)  #监听接收
            if not data0:
                print("服务器断开连接")
                break
            print('data0',data0)
            if data0[-2:] != b'^*':         #接收语音时，数据过大，可能一次接收不完，需要再次接收，已获取完整数据
                continue
            data_recv = data0.split(b'^*')
            print('data_recv:',data_recv)
            for i in data_recv[:-1]:
                try:
                    key,value = i[:1].decode(),i[2:]
                    if key in ("F",):
                        value = tuple(value.split(maxsplit=1))
                    else:
                        value = value.decode().strip()
                    print(key,value)
                    self.fun_map[key](value)        #解析报文后将接收到的内容分发各个处理函数进行处理
                    print('执行了',key,self.fun_map[key])
                except Exception as e:
                    print('接收消息后，解析报文过程中报错：',e)
            data0 =b''



