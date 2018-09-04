

# mail1 = '949220505@qq.com'   # 收件人邮箱账号，我这边发送给自己r
 
# kkvguipwmqngdhje
def mail(mail1):
    ret = True

    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
     
    my_sender = '2504072604@qq.com'  # 发件人邮箱账号
    my_pass = 'kkvguipwmqngdhje'       # 发件人邮箱密码(当时申请smtp给的口令)

    try:
        mail_msg = """ 您好! xxx  欢迎加入内达科技! 请用以下链接来激活您的帐号:\
        <p><a href="http://176.122.15.128:9955/login/logincheck/%s" \
        rel="external nofollow" >这是一个链接</a></p>"""%mail1

        msg=MIMEText(mail_msg, 'html', 'utf-8')
        # msg=MIMEText('<邮件内容>','plain','utf-8')
        print("11")
        msg['From']=formataddr(["内达科技", my_sender]) 
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        print("22")
        msg['To']=formataddr(["", mail1])       
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        print("33")
        msg['Subject']= '内达科技 xxx 用户帐号激活!'     
        # 邮件的主题，也可以说是标题
        print("44")

        server=smtplib.SMTP_SSL("smtp.qq.com", 465) 
        # 发件人邮箱中的SMTP服务器，端口是465
        print("55")
        server.login(my_sender, my_pass) 
        # 括号中对应的是发件人邮箱账号、邮箱密码
        print("66")
        server.sendmail(my_sender, [mail1,], msg.as_string()) 
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        print("77")
        server.quit() # 关闭连接
    except Exception: # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
        print("邮件发生失败")
    return ret
    print("邮件发送成功")
     
# ret = mail(mail1)

# if ret:
#   print("邮件发送成功")
# else:
#   print("邮件发送失败")
