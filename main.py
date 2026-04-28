import streamlit as st 
st.title("Meow")
st.write("Now this looks like a job for me, so everybody, just follow me, 'cause we need a little bit o'controversy, 'cause it feels so empty without me!")
st.write()
st.write()
with st.form("my_form"):
    name = st.text_input("Name (Required)")
    email = st.text_input("Email (Required)")
    
    # Every form must have a submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        if not name or not email:
            st.error("Please fill in all required fields.")
        else:
            st.success(f"Form submitted for {name}!")
