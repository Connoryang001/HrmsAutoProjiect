# coding=utf-8
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import os


def send_mail():

    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    sender = '593383513@qq.com'
    mail_pwd = 'cmgidlsyoyrsbahh'
    tolist = ['593383513@qq.com', 'yangli_revee@163.com']

    # 创建邮件对象
    message = MIMEMultipart()
    # 邮件主题
    message['Subject'] = Header('HRMS自动化测试报告', 'utf-8')
    # 发送方信息
    message['From'] = Header(sender, 'utf-8')
    # 接受方信息
    message['To'] = Header(','.join(tolist), 'utf-8')
    # 邮件正文内容
    message.attach(MIMEText('''老师们好，以上为自动化测试报告，请查收！！''', 'plain', 'utf-8'))

    # 获取report中最新的测试报告
    test_report = 'D:/pythonProject/HrmsAutoProject/report/' #报告存放目录
    lists = os.listdir(test_report) # 列出目录下所有文件名存放到lists
    print(lists)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn)) # 按时间排序
    print(lists)
    file_new = os.path.join(test_report, lists[-2]) #获取最新的文件保存到file_new
    print(file_new)

    # 构造附件
    fujian = open(file_new, 'rb').read()
    att1 = MIMEText(fujian, 'base64', 'utf-8')
    att1['Content-type'] = 'application/octet-stream'
    att1.add_header("Content-Disposition", "attachment", filename="自动化测试报告 %s.html" %now_time)
    message.attach(att1)


    # 创建邮箱服务器对象
    smtp = smtplib.SMTP()
    # 连接邮箱服务器
    smtp.connect('smtp.qq.com')
    # 登录邮箱账号
    smtp.login(sender, mail_pwd)
    # 发送邮件：from_addr:发件人;send_addrs:收件人，可以多人;msg:消息内容
    smtp.sendmail(sender, tolist, message.as_string())
    smtp.quit()

    print('email has send out')




if __name__ == '__main__':

    send_mail()
