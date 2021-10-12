# 生产测试报告
from HTMLTestRunner import HTMLTestRunner  # 界面报告运行，给用户，返回报告
import unittest
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"E:\pythonProject\自动化", pattern="Test*.py")

# 2.创建 运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",
    description="计算器的加法报告",
    verbosity=1,
    stream=open(file="计算器.html", mode="w+", encoding="utf-8")
)

# 3.运行用例
runner.run(tests)


# 4.邮件发送
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "2291494711@qq.com"  # 用户名
mail_pass = "easokwbixrxldiai"  # 口令

sender = '2291494711@qq.com'
receivers = ['2291494711@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("蔚超慧", 'utf-8')  # 发件人
message['To'] = Header("蔚大白", 'utf-8')   # 收件人

subject = 'Python发送带附件的邮件示例'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
send_content = 'hi man，你收到附件了吗？'
content_obj = MIMEText(send_content, 'plain', 'utf-8')  # 第一个参数为邮件内容
message.attach(content_obj)

# 构造附件1，发送当前目录下的 t1.txt 文件
att1 = MIMEText(open('计算器.html', 'rb').read(), _subtype='html', _charset='utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件附件中显示什么名字
att1.add_header("Content-Disposition" , 'attachment', filename="计算器.html")
message.attach(att1)

try:
    smtpObj = smtplib.SMTP('smtp.qq.com')
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException:
    print("Error: 无法发送邮件")