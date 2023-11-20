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
col3,empty, col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if index%2 == 0:
            st.header(row['title'])
            st.write(row['description'])
            st.image(f"images/{index+1}.png")
            st.write(f"[Source code]({row['url']})")

with col4:
    for index,row in df.iterrows():
        if index%2 ==1:
            st.header(row['title'])
            st.write(row['description'])
            st.image(f"images/{index+1}.png")
            st.write(f"[Source code]({row['url']})")
