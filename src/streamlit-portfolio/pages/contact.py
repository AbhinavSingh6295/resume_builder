import streamlit as st

st.title("Contact Me")

st.header("Get in Touch")

st.write("Feel free to reach out through the form below:")

contact_form = st.form(key='contact_form')
name = contact_form.text_input("Your Name")
email = contact_form.text_input("Your Email")
message = contact_form.text_area("Your Message")
submit_button = contact_form.form_submit_button(label='Send')

if submit_button:
    st.success("Thank you for your message! I'll get back to you soon.")