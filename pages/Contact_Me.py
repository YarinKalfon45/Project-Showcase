import streamlit as st
import send_mail as sm

st.header("Contact me")
options = ["Teach me how to live like you", "Tell me more about your program","Other"]

with st.form(key="Email_form"):
    usr_email = st.text_input("Your Email address:",key="usr_mail")
    select = st.selectbox(label="Which topic you would like to discuss?",options=options)
    raw_message = st.text_area("Your message:",key="raw_message")
    submit_button = st.form_submit_button()
    message = f"""\
Subject: You have a new message From {usr_email}

From: {usr_email}
Topic: {select}
{raw_message}
    """
if submit_button:
    sm.send_mail(message)
    st.info("Your message has been submitted successfully. I will contact you as soon as possible!")

