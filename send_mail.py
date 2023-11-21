import smtplib as smtp
import ssl
import os

import streamlit


def send_mail(message, reciver='Yarinkalfon45@gmail.com'):
    host = 'smtp.gmail.com'
    port_git = 465
    port_st = 587
    uname = streamlit.secrets("uname")
    password = streamlit.secrets("password")

    server = smtp.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(uname, password)
    server.sendmail(uname, reciver,message)
    server.quit()


    # server = smtp.SMTP(host,port_st)
    # with smtp.SMTP(host,port_st) as server:
    #     server.login(uname,password)
    #     server.sendmail(uname,reciver,message)

    # context = ssl.create_default_context()
    # with smtp.SMTP_SSL(host, port, context=context) as server:
    #     server.login(uname, password)
    #     server.sendmail(uname, reciver, message)


"""
enlmypwchxzcjwrw
"""
"""
mcowebdzgevwbqqj
"""