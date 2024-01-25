import streamlit as st
import base64

def displayGIFOLD():
   file_ = open("./images/dragonball.gif", "rb")
   contents = file_.read()
   data_url = base64.b64encode(contents).decode("utf-8")
   file_.close()

   st.markdown(
      f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" class="center">',
      unsafe_allow_html=True,
   )
   return

def displayGif():
   col1, col2, col3 = st.columns([1,6,1])

   with col1:
      st.write("")

   with col2:
      st.image("images\dragonball.gif", width=500, caption="(dragon ball is one of my favorite shows!)")

   with col3:
      st.write("")

st.toast('Welcome!', icon='🐵')
st.title("WELCOME!")
st.subheader("This is my first time using Streamlit!")
st.divider()
st.text("Welcome to my Streamlit introduction page for CSS 483!")
st.divider()
st.subheader("Quick Links (or use the sidebar!):")

about_me = st.button("About Me", use_container_width=True)
music = st.button("Music", use_container_width=True)
github = st.link_button("GitHub", "https://www.github.com/vikv1", use_container_width=True)
linkedin = st.link_button("LinkedIn", "https://www.linkedin.com/in/vikrant-verma1", use_container_width=True)

displayGif()

if(about_me):
   st.switch_page("pages/About_Me.py")

if(music):
   st.switch_page("pages/Music.py")






