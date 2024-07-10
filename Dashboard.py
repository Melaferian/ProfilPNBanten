import streamlit as st
import streamlit.components.v1 as components

# Set the title of the app
st.write("### Dashboard Profil Piutang Negara Kanwil DJKN Banten")

# URL of the dashboard to be embedded
dashboard_url = "https://app.powerbi.com/view?r=eyJrIjoiZDNhNWEyZTctY2FlMi00NDQ3LWFkNTUtNzEwMmEwNzc2NDU2IiwidCI6ImVkNmZiMzY2LTgzMjItNDZmMy05MTVlLWM0ZDAzN2E0NTRhOSIsImMiOjEwfQ%3D%3D"

# Embed the dashboard using an iframe
components.iframe(src=dashboard_url, width=800, height=400)
