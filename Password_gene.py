import random
import string
import streamlit as st

def gene_passw(length):
    if length < 4:
        st.write("Password length should be at least 4 characters.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Streamlit app UI
st.title('Password Generator')
passw_length = st.slider("Choose password length", 4, 20, 8)  # Slider to choose password length
generated_password = gene_passw(passw_length)  # Call the password generation function

if generated_password:
    st.write("Generated Password:", generated_password)


