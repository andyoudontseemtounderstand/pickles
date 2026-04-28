import streamlit as st 
st.title("Meow")
st.write("Now this looks like a job for me, so everybody, just follow me, 'cause we need a little bit o'controversy, 'cause it feels so empty without me!")
st.write()
st.write()
name = st.text_input("What's your name?: ")
age = st.number_input("What's your age?: ")

if st.button("Press this so I can sell your info for free money"):
  st.write("Thanks")
