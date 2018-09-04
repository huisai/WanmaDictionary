import  random 





def checknumber(email):
    number = "" 
    for x in range(0,4):
        num = int(random.uniform(0,9))
        number += str(num)
    mail(email,number) 
    return number
 


def mail(email,number):
    ret = True

    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    
    my_sender = '2504072604@qq.com'  # 发件人邮箱账号
    my_pass = 'kkvguipwmqngdhje'       # 发件人邮箱密码(当时申请smtp给的口令)

        
    try:

        mail_msg = """<h1>|-万码词典-|<h1>
         <p>您好! 您的验证码是 %s 请勿泄露给任何人<p>"""%number

        msg=MIMEText( mail_msg , 'html', 'utf-8')
        # msg=MIMEText('<邮件内容>','plain','utf-8')
        print("11")
        msg['From']=formataddr(["万码科技", my_sender]) 
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        print("22")
        msg['To']=formataddr(["", email])       
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        print("33")
        msg['Subject']= ' 您正在进行修改密码操作 !'     
        # 邮件的主题，也可以说是标题
        print("44")

        server=smtplib.SMTP_SSL("smtp.qq.com", 465) 
        # 发件人邮箱中的SMTP服务器，端口是465
        print("55")
        server.login(my_sender, my_pass) 
        # 括号中对应的是发件人邮箱账号、邮箱密码
        print("66")
        server.sendmail(my_sender, [email,], msg.as_string()) 
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件

        server.quit() # 关闭连接
    except Exception: # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
        print("邮件发生失败")
    return ret
    print("邮件发送成功")



def updatepassword(name,number,usernumber,password):
    #1.导入数据库模块
    import pymysql

    #2. 判断验证码是否相等
    if number == usernumber:
        print("111")
        # 1,创建数据库链接对象
        conn = pymysql.connect(host='localhost',user='root',passwd='123456',db='dict',charset='utf8')

        # 2, 创建游标对象
        cursor1 = conn.cursor()
        # 3, 利用execute方法实行sql命令
        # try:
        try:
            sql_update = "update index_user set passwd=%s where name=%s;"
            cursor1.execute(sql_update,[password,name]) #修改记录
            print("222")
            conn.commit()
            print("修改成功")
            return True

        except Exception as e:
            conn.rollback()
            print("出现错误,已回滚")
            cursor1.close()
            conn.close()
            return False

    else:
        print("xxx")


