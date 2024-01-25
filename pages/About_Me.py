import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import graphviz
import time

def coolMap():
   chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

   st.pydeck_chart(pdk.Deck(
      map_style=None,
      initial_view_state=pdk.ViewState(
         latitude=47.7590,
         longitude=-122.1925,
         zoom=15,
         pitch=50,
      ),
      layers=[
         pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[-122.19142223569749, 47.75885464784375]',
            radius=20,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
      ],
   ))
   return

def drawThing():
   graph = graphviz.Digraph()
   graph.edge('Wake up', 'Go to the gym')
   graph.edge('Go to the gym', 'School')
   graph.edge('School', 'Do Homework')
   graph.edge('School', 'Leetcode', 'If no HW')
   graph.edge('Do Homework', 'Leetcode')
   graph.edge('Leetcode', 'Apply to Internships')
   graph.edge('Leetcode', 'Go to the gym', 'If did not go')
   graph.edge('Apply to Internships', 'Watch YouTube')
   graph.edge('Watch YouTube', 'Sleep')
   graph.edge('Sleep', 'Wake up')


   st.graphviz_chart(graph)

   return



# with st.spinner('Loading!'):
#     time.sleep(2)
# st.success('Done!')

st.title("About Me")
st.divider()
st.write("Hi, my name is Vikrant Verma, a student of CSS 483- Bioninformatics Algorithms at UWB (below)!")
coolMap()
st.divider()
st.subheader("Hobbies")
st.write("I like going to the gym, playing chess, making music and video, and playing soccer! I also like to do coding projects sometimes, here is my GitHub.")
st.link_button("GitHub", "https://github.com/vikv1")

st.divider()
st.subheader("My Day")
st.write("I try to follow a decent routine every day! I will attempt to draw it with a Streamlit library!")
drawThing()
st.divider()


welcome = st.button("Home")
music = st.button("Music")

if(welcome):
   st.switch_page("Welcome.py")

if(music):
   st.switch_page("pages/Music.py")
