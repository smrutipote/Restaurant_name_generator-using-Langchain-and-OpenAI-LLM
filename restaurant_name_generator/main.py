import streamlit as st
from langchain_community.llms import OpenAI
st.title('Restaurant Name Generator')
cuisine=st.sidebar.selectbox('Pick a cuisine',('Indian','Mexican','Chinese','Continental','Arabic','American'))
import alldetails


if cuisine:
   response=alldetails.restaurant_generator(cuisine)
   st.header(response['restaurant_name'].strip())
   menu_items=response['menu_items'].strip().split(',')
   st.write('**Menu Items**')
   for item in menu_items:
       st.write('-',item)


///////In Terminal : streamlit run main.py  //////////////////////////////























































































