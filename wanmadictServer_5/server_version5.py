#!/usr/bin/env python3
# coding=utf-8


from socket import *
import os
import signal
import time
import sys
import pymysql
import re
from checknumber import *
from youjian import *
from spider import *

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

# 主控制流程


def main():

    db = pymysql.connect(host="localhost", user="root",
                         passwd='123456', db='dict', charset="utf8")
    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    # 设置父进程接收到子进程退出信号时的处理方式-->>忽略子进程退出
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit("Server's out")  # 服务器进程退出
        except Exception:
            continue

        # 创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()   # 子进程中，父进程的监听套接字无意义，故关闭
            do_child(c, db)
        else:
            c.close()   # 无论创建失败还是父进程，都是关闭客户端套接字
            continue


def do_child(c, db):
    # 每一个独立的子进程单独处理一个客户端
    print("Enter child process")
    # 循环接收客户端请求
    while True:
        # 要求客户端的数据格式：
        data = c.recv(128).decode()
        print("Reuquest:", data)
        if data[0] == 'R':
            # 注册
            do_register(c, db, data)
        elif data[0] == 'L':
            # 登录
            name = do_login(c, db, data)
        elif data[0] == 'E':
            # 客户端退出，发送过来指令，
            c.close()   # 关闭套接字及退出子进程
            sys.exit(0)
        elif data[0] == 'Q':
            # 接收到查词请求的信号
            do_query(c, db, name, data)
        elif data[0] == 'H':
            # 接收到查询历史的请求信号
            do_history(c, db, name)
        elif data[0] == 'O':
            # 用户执行注销操作，客户端发送数据格式：'O'
            do_logout(c, db, name)
        elif data[0] == 'G':
            guest_query(c, db, data)
        elif data[0] == 'T':
            # 首字母Ｔ表示用户请求发送验证码给邮箱
            # 要求客户端发送的消息格式如"T username"
            # 生成的验证码是一串字符串
            number = send_verification(c, db, data)
        elif data[0] == 'V':
            # 接收用户修改密码的详细信息，如'X username pwd checknumber'
            modify_pwd(c, db, data, number)
        elif data[0] == 'U':
            # 请求非英文单词查询
            # 要求客户端发送格式"U XXX"
            cn_query(c, data)


def cn_query(c, data):
    # 中文查词
    print('进入爬虫模块')
    print('data:', data)
    dataInfo = data.split(' ')
    if dataInfo.length>2:
        sentence = 0
    word = dataInfo[1]
    youdao_zh_en = Youdao_zh_en(word)
    query_result = youdao_zh_en.start()
    if query_result:
        # 取出查询结果的'translation'键的列表
        result = query_result['translation']
        print('result:', result)
        result.append(word)
        send_result = repr(result)
        # 返回如："U ['hello', 'hi', '你好']^*"
        print('send_result:', send_result)
        msg = "U " + send_result + '^*'
        print(msg)
        c.send(msg.encode())
    else:
        msg = "H "+word+"^*"
        c.send(msg.encode())
    return


def modify_pwd(c, db, data, number):
    # 修改密码
    dataInfo = data.split(' ')
    # 接收到的修改密码的消息格式为如：'V user pwd verfivicationCode'
    name = dataInfo[1]
    pwd = dataInfo[2]
    # userNUm即为客户端的用户发送过来的验证码
    userNum = data[3]
    # flag = updatepassword(name, number, userNum, pwd)
    if number == userNum:
        # 当客户发送的验证码与系统验证码(即服务端发送给用户邮箱的验证码)相同的时候，允许修改密码
        cursor1 = db.cursor()
        sql_update = "update index_user set passwd='%s' where name='%s';" % (
            pwd, name)
        try:
            cursor1.execute(sql_update)  # 修改记录
            db.commit()
            print("修改成功")
            c.send(b'J S^*')
            cursor1.close()
        except:
            db.rollback()
            print("出现错误,已回滚")
            cursor1.close()
            c.send(b'J F^*')
    else:
        #　用户输入的验证码与服务端发送的验证码不一致，直接告知客户端修改失败
        c.send(b'J F^*')
    return


def send_verification(c, db, data):
    # send_verification 只负责发送验证码到用户邮箱
    print(data)
    dataInfo = data.split(' ')
    print(dataInfo)
    username = dataInfo[1]
    print('username:', username)
    # 从数据库获取用户名对应的邮箱帐号
    cursor = db.cursor()
    sql = "select email from user where name ='%s';" % username
    print('查email:', sql)
    try:
        cursor.execute(sql)
        r = cursor.fetchone()
        print('r:', r)
        # 若能查到，cursor.fetchone()返回的是元组('xxx@yyy.com',)
        if r:
            email = r[0]
            print('获取到的email:', email)
            number = checknumber(email)
            print('验证码number:', number)
            c.send(b'I S^*')
            cursor.close()
            return number
        else:
            # 若r为空，则不存在该用户，告知客户端发送失败
            c.send(b'I F^*')
            return
    except:
        pass


def do_register(c, db, data):
    # 注册操作
    # 注册时收到的数据格式："R name pwd email"
    print('----do_register----')
    print(data)
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    email = l[3]
    print('name:', name, ' passwd:', passwd, ' email:', email)
    cursor = db.cursor()

    # 判断用户名是否存在
    sql = "select name from user where name ='%s';" % name
    cursor.execute(sql)
    r = cursor.fetchone()
    print("SQL of Register test:", r)
    if r:   # 查询有结果，则说明用户已存在
        c.send(b'A F^*')
        return

    # 判断邮箱是否存在
    sql = "select name from user where email ='%s';" % email
    cursor.execute(sql)
    r = cursor.fetchone()
    print("SQL of Register test:", r)
    if r:   # 查询有结果，则说明用户已存在
        c.send(b'A N^*')
        return

    # r为空，则说明用户不存在，执行插入用户数据的操作
    sql = "insert into user (name,passwd,email) values ('%s','%s','%s');" % (
        name, passwd, email)
    print("----insert user into db")
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print('db.commit() succeed')
        # c.send(b'OK')
        # 通知客户端注册结果，Ａ表示该信息属于'注册'相关的信息，Ｓ表示注册成功
        regist_info = "A S^*"
        c.send(regist_info.encode())
        print('register succeed')
    except:
        print('cursor exception')
        c.send(b"A F^*")
        db.rollback()
    else:
        # 调用youjian模块中发送验证邮件给用户邮箱的方法
        mail(email)
        print('注册成功')
    cursor.close()
    return


def do_login(c, db, data):
    print("用户正在执行登录操作")
    print('-------do_login test---------')
    print('receive data:', data)
    l = data.split(' ')
    print('l:', l)
    passwd = l[2]
    print('passwd:', passwd)
    # 先判断是通过邮箱登录还是用户名登录
    pattern = '(\w+@\w+(\.(cn|com)){1,2})'
    regex = re.compile(pattern)
    m = regex.findall(l[1])
    if m:
        # 若正则表达式能匹配出是邮箱，则用邮箱登录
        findKey = 'email'
        # m返回一个列表，形如[('sussan@126.com', '.com', 'com')]
        # 邮箱地址为正则表达式对象匹配出的结果返回的元组的第０个元素
        keyVal = m[0][0]
    else:
        # 正则表达式匹配不出邮箱，则说明是账户登录
        findKey = 'name'
        keyVal = l[1]

    cursor = db.cursor()

    # sql语句的wehre字句的关键字段根据匹配到的是用户名还是邮箱而定
    sql = "select * from user where %s ='%s' and passwd ='%s';" % (findKey,
                                                                   keyVal, passwd)
    print(sql)
    cursor.execute(sql)
    r = cursor.fetchone()
    print(r)
    # r=(1, username, passwd, status, email, loginCheck)或r=()
    if not r:
        c.send(b'B F^*')  # 登录失败
        print('到此处发送了登录失败的消息')
        return
    elif r and r[3] == 0 and r[5] == True:
        # 查询结果不为空，且登录状态r[3]为未登录且邮箱已激活(r[5]为真)，则允许登录
        name = r[1]
        sql_status = "update user set status=1 where name='%s';" % name
        cursor.execute(sql_status)
        db.commit()
        c.send(b'B S^*')
        return name
        # 此处考虑return一个值用于标记用户的登录状态，方便后续做其他操作
        # 例如返回用户的姓名
    elif r[3] == 1:
        c.send(b'B Z^*')  # 该用户已登录
        return
    elif r[5] == False:
        # 邮箱未验证
        c.send(b'B N^*')
        return
    # else:
    #     # c.send(b"Fail")
    #     c.send(b'B F^*')  # 登录失败
    #     print('到此处发送了登录失败的消息')


def do_query(c, db, name, data):
    # 查询操作
    word = data.split(' ')[1]
    print('查询单词：', word)
    cursor = db.cursor()

    def insert_history():
        # 用内部函数的方式实现插入历史记录的功能，可以无条件使用外部函数的变量，不需要形参
        # cursor = db.cursor()  # 若外部是使用文本查询，则此处需要创建游标对象
        tm = time.ctime()
        sql1 = "select * from hist where name='%s' and word='%s';" % (
            name, word)
        cursor.execute(sql1)
        r = cursor.fetchall()
        if r:
            # 若历史记录中对应的用户已经存在该单词，则原有的该词查词频数+1
            sql2 = "update hist set frequency=frequency+1 where name='%s' and word='%s';" % (
                name, word)
            try:
                cursor.execute(sql2)
                db.commit()
            except:
                db.rollback()
                return
        else:
            # 查不到该词，则对应用户增加该词的查词记录
            sql3 = "insert into hist (name,word,frequency,time) values ('%s','%s','%d','%s')" % (
                name, word, 1, tm)
            try:
                cursor.execute(sql3)
                db.commit()
            except:
                db.rollback()
                return

    sql = "select * from dict2 where word = '%s';" % word
    try:
        cursor.execute(sql)
        r = cursor.fetchone()
    except:
        pass
    if not r:
        c.send(('H '+word+'^*').encode())
    else:
        # c.send(b'OK')
        time.sleep(0.1)
        # msg = "{} : {}".format(r[1], r[2:])   # msg是一个字符串！
        # msg = r[2:]
        msg = ""
        # print(r[2:])
        # for i in r[2:]:
        #     msg += str(i)
        #     msg += "#"
        # r = [id, word, phonetic, translation,...],故从下标１开始取到最后作为查询结果返回
        query_result = repr(r[1:])
        msg = "C "+query_result+'^*'  # 返回的查询结果是Ｃ＋１个列表字符串
        print(msg)
        c.send(msg.encode())    # send的是一个字符串转化为二进制编码
        insert_history()
        cursor.close()
        # get voice and examply by spider module
        # youdao_zh_en = Youdao_zh_en(word)
        # query_result = youdao_zh_en.start()
        # example = query_result['example']
        # example_word = example.insert(0,word)
        # print('example:',example_word)
        # voice = query_result['voice'][0]
        # print('voice:',query_result['voice'][0])
        # send_example = 'E '+repr(example_word)+'^*'
        # # send_voice = 'F ' + word +  + "^*"
        # voice_head = 'F '+word+' '
        # c.send(send_example.encode())
        # c.send(voice_head.encode()+voice+b'^*')
        query_voice_example(c, word)



def guest_query(c, db, data):
    word = data.split(' ')[1]
    cursor = db.cursor()
    sql = "select * from dict2 where word = '%s';" % word
    try:
        cursor.execute(sql)
        r = cursor.fetchone()
    except:
        pass

    if not r:
        c.send(('H '+word+'^*').encode())
    else:
        # c.send(b'OK')
        time.sleep(0.1)
        # msg = "{} : {}".format(r[1], r[2:])   # msg是一个字符串！
        # msg = r[2:]
        msg = ""
        # print(r[2:])
        # for i in r[2:]:
        #     msg += str(i)
        #     msg += "#"
        query_result = repr(r[1:])
        msg = "C " + query_result + '^*'
        print(msg)
        c.send(msg.encode())
        cursor.close()

        # youdao_zh_en = Youdao_zh_en(word)
        # query_result = youdao_zh_en.start()

        # # send voice
        # voice = query_result['voice'][0]
        # voice_head = 'F ' + word + ' '
        # c.send(voice_head.encode() + voice + b'^*')

        # # send example
        # example = query_result['example']
        # print('example:', example)
        # example.insert(0, word)
        # print('example_word:', example)
        # send_example = 'E ' + repr(example) + '^*'
        # c.send(send_example.encode())
        query_voice_example(c, word)
        return


def query_voice_example(c, word):
    youdao_zh_en = Youdao_zh_en(word)
    query_result = youdao_zh_en.start()
    # send voice
    try:
        print('voice:', query_result['voice'][0])
    except:
        pass
    if query_result['voice']:
        voice = query_result['voice'][0]
        voice_head = 'F ' + word + ' '
        c.send(voice_head.encode() + voice + b'^*')
    else:
        pass

    # send example
    if query_result['example']:
        example = query_result['example']
        print('example:', example)
        example.insert(0, word)
        print('example_word:', example)
        send_example = 'E ' + repr(example) + '^*'
        c.send(send_example.encode())
    else:
        # msg = 'H ' + word + '^*'
        # c.send(msg.encode())
        pass
    return


def do_history(c, db, name):
    print("历史记录")
    cursor = db.cursor()
    # sql = "select * from hist where name = '%s';" % name
    sql = "select name,word,frequency from hist where name = '%s';" % name
    try:
        cursor.execute(sql)
        r = cursor.fetchall()
        print('fetch done')
    except:
        pass

    if not r:
        # 如果没有找到，r就是null，此时返回给客户端一个fail的信号
        c.send(b'Fail')
    else:
        # c.send(b'OK')
        # time.sleep(0.1)  # 后面仍是发送消息，连续发送要防止粘包，此处用延迟方式防粘包
        # for i in r:
        #     # time.sleep(0.1) # 连续发送，要防止粘包，延迟方式，＃或者每次发送最后加\n，是客户端接收后\n换行
        #     # 最后+'\n'使客户端每次打印换行即可，使粘包影响转换为换行
        #     msg = "{} {} {}\n".format(i[1], i[2], i[3])
        #     c.send(msg.encode())
        # time.sleep(0.1)  # 迭代完成后再阻塞0.1秒，同样是为了防止粘包
        # c.send(b'##')   # 迭代完成后

        # 直接将查询结果的列表通过repr()转换为字符串形式发送给客户端
        hist_result = repr(r)
        msg = 'D ' + hist_result + '^*'
        c.send(msg.encode())
        # 客户端把msg decode，将列表字符串提取后需要通过eval()转换回列表，列表内是元组


def do_logout(c, db, name):
    print("%s 正在执行注销操作" % name)
    cursor = db.cursor()
    sql = "update user set status=0 where name = '%s';" % name
    try:
        cursor.execute(sql)
        db.commit()
        print("%s　注销成功" % name)
        print(sql)
    except:
        db.rollback()
        print("注销失败")


if __name__ == '__main__':
    main()
