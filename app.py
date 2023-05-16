import streamlit as st

st.checkbox('yes')
st.button('click')
st.radio('pick your gender', ['male', 'female'])
st.selectbox('pick your gender', ['male', 'female'])
st.multiselect('choose a planet', ['jupiter', 'mars', 'neptune'])
st.select_slider('pick a mark', ['bad', 'good', 'execellent'])
st.slider('pick a number', 0, 50)