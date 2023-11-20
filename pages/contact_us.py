import streamlit as st
import send_mail as sm

st.header("Contact me")

with st.form(key="Email_form"):
    usr_email = st.text_input("Your Email address:")
    raw_message = st.text_area("Your message:")
    submit_button = st.form_submit_button()
    message = f"""\
Subject: You have a new message From {usr_email}

From: {usr_email}
{raw_message}
    """
if submit_button:
    sm.send_mail(message)
    st.info("Your message has been submitted.I will contact you soon.Thank you!")
