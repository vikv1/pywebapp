import streamlit as st
import streamlit.components.v1 as components

st.title("My music!")
st.subheader("I used to make music often, getting back into it!")

components.html(
   """
   <iframe style="border-radius:12px" src="https://open.spotify.com/embed/artist/7akxaK7XwnHSE87rOH3SoQ?utm_source=generator&theme=0" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy">
   </iframe>
   """,
   height=365,
)


st.caption("Here is what I have done so far!")
st.divider()

welcome = st.button("Home")
about_me = st.button("About Me")

if(welcome):
   st.switch_page("Welcome.py")

if(about_me):
   st.switch_page("pages/About_Me.py")