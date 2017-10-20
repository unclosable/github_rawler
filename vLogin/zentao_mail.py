import smtplib
import poplib
from email.mime.text import MIMEText
from email.header import Header

__sender = "冯涛 <fengtao@itiaoling.com>"
__receiver = ["zhengwei@itiaoling.com", "fengtao@itiaoling.com",
              "liuhaibao@itiaoling.com", "songkai@itiaoling.com",
              "gaotong@itiaoling.com", "wujianwei@itiaoling.com"]
__subject = '涛涛你好二你皂么'
__smtpserver = 'smtp.wltest.com'
__port = 25
__username = 'rocket@wltest.com'
__password = 'Rfd.com@123'


def _smtp():
    msg = MIMEText('如题', 'html', 'utf-8')
    msg['Subject'] = Header(__subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(__smtpserver)
    smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.login(__username, __password)
    smtp.sendmail(__sender, __receiver, msg.as_string())
    smtp.quit()


def _smtp_msg(title, msg):
    msg = MIMEText(msg, 'html', 'utf-8')
    msg['Subject'] = Header(title, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(__smtpserver)
    smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.login(__username, __password)
    smtp.sendmail(__sender, __receiver, msg.as_string())
    smtp.quit()


def __pop3():
    s = poplib.POP3(__smtpserver)
    s.port(__port)
    s.user(__username)
    s.pass_(__password)


if __name__ == "__main__":
    _smtp()
