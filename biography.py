import streamlit as st
import PIL as image
import datetime as datetime

st.title("My Biography")

st.sidebar.header("Full Name")
name = st.sidebar.text_input("Name", "Marialyn Ramada")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
occupation = st.sidebar.text_input("Occupation", "")
hobbies = st.sidebar.text_area("Hobbies (comma-separated)", "")
goals = st.sidebar.text_area("Goals or Aspirations", "")

# Display biography
if st.sidebar.button("Generate Biography"):
    if name and age and occupation:
        st.header("Your Biography")
        st.write(f"*Name:* {name}")
        st.write(f"*Age:* {age}")
        st.write(f"*Occupation:* {occupation}")
        st.write(f"*Hobbies:* {', '.join(hobby.strip() for hobby in hobbies.split(',')) if hobbies else 'None'}")
        st.write(f"*Goals:* {goals if goals else 'Not specified'}")
    else:
        st.error("Please fill in all the required fields (Name, Age, and Occupation).")