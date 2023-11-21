import smtplib as smtp
import ssl
import os

import streamlit


def send_mail(message, reciver='Yarinkalfon45@gmail.com'):
    host = 'smtp.gmail.com'
    port = 465
    uname = streamlit.secrets("uname")
    password = streamlit.secrets("password")
    context = ssl.create_default_context()
    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.ehlo_or_helo_if_needed()
        server.login(uname, password)
        server.sendmail(uname, reciver, message)


"""
enlmypwchxzcjwrw
"""
"""
mcowebdzgevwbqqj
"""