import streamlit as st
import re
import secrets
import string

#check the password strength
def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.write("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.write("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.write("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*_]", password):
        score += 1
    else:
        st.write("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        st.write("✅ Strong Password!")
    elif score == 3:
        st.write("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.write("❌ Weak Password - Improve it using the suggestions above.")

#Genrate the password
def password_generator(length = 8):
    make_password = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return " ".join(secrets.choice(make_password) for _ in range(length))

#user interface
st.title("🔐 Password Strength Meter!")
st.write("Use this simple tool to make or generate a storng password 🔑")

password = st.text_input("Please enter the password: ", type="password")

button = st.button("Check Password Strength")

if(button == True):
    if(password == ""):
        st.error("❗Enter the password")
    else:
        st.title("Improvement Suggestions:")
        check_password_strength(password)

st.title("🔑Suggest a strong Password!")

generate = st.button("Generate Password")

if(generate == True):
    generate_password = password_generator()

    st.success(generate_password)
