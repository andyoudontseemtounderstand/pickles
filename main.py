import streamlit as st 
st.title("Meow")
st.write("Now this looks like a job for me, so everybody, just follow me, 'cause we need a little bit o'controversy, 'cause it feels so empty without me!")
st.write()
st.write()
with st.form("my_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Enter your age", value=0, min_value=0, step=1)
    gender = st.text_input("Enter "M" for male or "F" for female.").lower()
    
    # Every form must have a submit button
    submitted = st.form_submit_button("Press this so I can sell your info")
    
    if submitted:
        if not name or not email:
            st.error("Hey! I can't sell your info without a filled form")
        else:
            if gender == "m":
                st.success(f"{name} is a good boy!")
            elif gender == "f":
                st.success(f"{name} is a good girl!")
            else:
                st.error("How in the actual fuck are you incapable of mentioning your own gender?")
