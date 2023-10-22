import streamlit as st
st.set_page_config(
    page_title= 'minecraft map',
    page_icon= 'img\minecraftemg.png'
)
lab1 = '측면'
lab2 = '정면 3층'

with st.expander(label=lab1):
    st.image('sideview.png',use_column_width=True)
with st.expander(label=lab2):
    st.image('Frontview.png',use_column_width=True)
