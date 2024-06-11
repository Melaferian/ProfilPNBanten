import streamlit as st
import streamlit.components.v1 as components

USERS = {
    "user1": "password1",
    "user2": "password2"
}

# Function to verify user credentials
def verify_login(username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# Login page
def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if verify_login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def dashboard_page():
# Set the title of the app
    st.title("Dashboard Profil Piutang Negara Kanwil DJKN Banten")

# URL of the dashboard to be embedded
    dashboard_url = "https://app.powerbi.com/view?r=eyJrIjoiZDNhNWEyZTctY2FlMi00NDQ3LWFkNTUtNzEwMmEwNzc2NDU2IiwidCI6ImVkNmZiMzY2LTgzMjItNDZmMy05MTVlLWM0ZDAzN2E0NTRhOSIsImMiOjEwfQ%3D%3D"

# Embed the dashboard using an iframe
    st.components.v1.iframe(src=dashboard_url, width=800, height=400)
    logout_button = st.button("Logout")
    if logout_button:
        st.session_state.logged_in = False
        st.session_state.username = ""

# Display the appropriate page based on the login status
if st.session_state.logged_in:
    dashboard_page()
else:
    login_page()