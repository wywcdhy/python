import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from time import strftime, localtime, sleep


def send_email(dest_email, file_path, report_name, text_content):  # 目标邮箱、附件路径、附件名称、正文内容。如需要添加图片，代码已包含
    # 设置smtplib所需的参数
    # 下面的发件人，收件人是用于邮件传输的。
    smtpserver = 'smtp.163.com'
    username = 'XXXXXXXX@163.com'
    password = 'XXXXXXXXX'
    sender = 'XXXXXXXXX@163.com'
    # receiver='XXX@126.com'
    receiver = dest_email
    # 收件人为多个收件人
    # receiver = ['XXX@126.com', 'XXX@126.com']

    subject = '测试报告'
    # 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
    # subject = '中文标题'
    # subject=Header(subject, 'utf-8').encode()

    # 构造邮件对象MIMEMultipart对象
    # 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = 'XXX'
    # msg['From'] = sender
    # msg['To'] = 'XXX@126.com'
    # 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
    msg['To'] = receiver  # 这个地方必须要写可用的email
    # msg['To'] = ";".join(receiver)
    # msg['Date']='2012-3-16'

    # 构造文字内容
    text = text_content
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    # 构造附件
    # sendfile = open(r'C:\Users\frank\PycharmProjects\postgreSQL\test.html', 'rb').read()
    sendfile = open(file_path, 'rb').read()

    text_att = MIMEText(sendfile, 'base64', 'utf-8')
    text_att["Content-Type"] = 'application/octet-stream'
    # 以下附件可以重命名成aaa.txt
    # text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
    # 另一种实现方式
    text_att.add_header('Content-Disposition', 'attachment', filename=report_name)
    # 以下中文测试不ok
    # text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
    msg.attach(text_att)

    # 构造图片链接
    '''
    sendimagefile = open(r'D:\pythontest\testimage.png', 'rb').read()
    image = MIMEImage(sendimagefile)
    image.add_header('Content-ID', '<image1>')
    image["Content-Disposition"] = 'attachment; filename="testimage.png"'
    msg.attach(image)
    '''

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    # smtp.set_debuglevel(1)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
