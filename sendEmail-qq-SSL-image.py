#!/usr/bin/python
#  coding:utf-8
#  lichanglai

import smtplib
from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart
from email.Utils import formatdate
from email.Header import Header
import sys
from email.mime.image import MIMEImage

#设置默认字符集为UTF8 不然有些时候转码会出问题
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#发送邮件的相关信息，根据你实际情况填写
smtpHost = 'smtp.qq.com'
smtpPort = '25'
sslPort  = '465'
fromMail = ''
toMail   = ''
username = fromMail
password = ''

#创建一个带附件的实例
message = MIMEMultipart('related')
message['From'] = fromMail
message['To'] =  toMail
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
message.attach(msgAlternative)


mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="https://www.baidu.com">baidu</a></p>
    <p>图片演示：</p>
    <p><img src="cid:image1"></p>
    """
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('test.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)


try:
    #连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种
    
    
    #普通方式，通信过程不加密
#    smtp = smtplib.SMTP(smtpHost,smtpPort)
#    smtp.ehlo()
#    smtp.login(username,password)

    #tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
#    smtp = smtplib.SMTP(smtpHost,smtpPort)
#    smtp.set_debuglevel(True)
#    smtp.ehlo()
#    smtp.starttls()
#    smtp.ehlo()
#    smtp.login(username,password)

    #纯粹的ssl加密方式，通信过程加密，邮件数据安全
    smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
    smtp.ehlo()
    smtp.login(username,password)
    
    #发送邮件
    smtp.sendmail(fromMail,toMail,message.as_string())
    smtp.close()
    print 'OK'
except Exception as e:
    print e




