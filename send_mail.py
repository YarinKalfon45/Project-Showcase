import smtplib as smtp
import ssl
import os


def send_mail(message, reciver='Yarinkalfon45@gmail.com'):
    host = 'smtp.gmail.com'
    port = 465
    uname = 'contactyarin@gmail.com'
    password = os.getenv("Password")
    context = ssl.create_default_context()
    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.login(uname, password)
        server.sendmail(uname, reciver, message)


"""
enlmypwchxzcjwrw
"""
"""
mcowebdzgevwbqqj
"""