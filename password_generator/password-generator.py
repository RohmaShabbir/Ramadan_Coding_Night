import streamlit as st
import random
import string

# Function to generate a secure password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # By default, include uppercase and lowercase letters

    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation  # Adds special characters (!@#$%^&* etc.) if selected

    return "".join(random.choice(characters) for _ in range(length))  # Generates a random password

# App Title with Emoji
st.title("🔐 Secure Password Generator")

# User input section with styling
st.markdown("### Customize your password:")

# Password length selection
length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

# Checkboxes for additional options
use_digits = st.checkbox("Include Numbers (0-9)")
use_special = st.checkbox("Include Special Characters (!@#$%^&*)")

# Button to generate password
if st.button("🔄 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    
    # Styled output for better visibility
    st.markdown("### 🔑 Your Secure Password:")
    st.code(password, language="plaintext")


