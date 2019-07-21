import sys
import json
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
 
# 第三方 SMTP 服务
with open('config', 'r') as f:
    config = json.loads(f.read())

mail_host = config['mail_host']
mail_port = config['mail_port']
mail_user = config['user']    #用户名
mail_pass = config['password']   #口令 
 
 
sender = mail_user
receivers = sys.argv[1] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEMultipart()
message['From'] = Header("ZRJ's_python_email_sender", 'utf-8')
# message['To'] = Header("帅哥美女", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

message.attach(MIMEText(' '.join(sys.argv[2:-1]), 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
mime = MIMEBase(zip, zip, filename=sys.argv[-1])
mime.add_header('Content-Disposition','attachment',filename=('gb2312', '', sys.argv[-1]))
mime.add_header('Content-ID','<0>')
mime.add_header('X-Attachment-Id','0')
#把附件的内容读进来
mime.set_payload(open(sys.argv[-1], 'rb').read())
#用Base64编码
encoders.encode_base64(mime)
message.attach(mime)
 
try:
    smtpObj = smtplib.SMTP(host=mail_host)
    smtpObj.connect(mail_host, mail_port)
    print('服务器连接成功')
    smtpObj.set_debuglevel(True)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(mail_user,mail_pass)  
    print('登陆成功')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")