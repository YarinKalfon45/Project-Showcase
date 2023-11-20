import streamlit as st
import pandas


col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_1309.jpeg")

with col2:
    st.header("Yarin Kalfon")
    st.info("""Hi, My name is Yarin.\n\n I'm a 3rd year student at Ben-Gurion University.\n\nThis website is created to
     showcase my programing skills.
            """)

st.write("If you have any more questions feel free to contact me in the link down below!")

