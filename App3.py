import requests
from PIL import Image
import streamlit as st
from datetime import datetime

API_KEY = "9f1e1d3a18d40be562129baafe0dae67"

CUSTOM_STYLE = """
<style>
    .stTextInput>div>div>input {
        background-color: #0c061a !important;
        border: 3px Groove #ffffff !important;
        border-radius: 2px !important;
        padding: 10px !important;
    }
    .stTextInput>div>div>input:hover {
        background-color: #140b2f !important;
        border: 3px Groove #0049ff !important;
        border-radius: 2px !important;
        padding: 10px !important;
    }
    .stButton>button {
        background-color: #249028 !important;
        color: white !important;
        padding: 10px 20px !important;
        text-align: center !important;
        text-decoration: none !important;
        display: inline-block !important;
        font-size: 16px !important;
        cursor: pointer !important;
        border-radius: 5px !important;
        border: none !important;
        transition-duration: 0.4s !important;
    }
    .stButton>button:hover {
        background-color: #5d008c !important;
    }
</style>
"""

def get_forecast_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)

    if response.status_code == 404:
        st.error("Forecast weather data not available")
        return None
    else:
        weather_data = response.json()
        forecast = []
        for data in weather_data['list']:
            timestamp = data['dt']
            dt_object = datetime.fromtimestamp(timestamp)
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            icon_url = f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
            forecast.append([icon_url, temperature, description, dt_object])

        return forecast

def main():
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    st.title("Sky View")

    city = st.text_input("Enter Location:", "")

    if st.button("Search"):
        if city:
            forecast = get_forecast_weather(city)
            if forecast:
                st.subheader("Upcoming Forecast")
                row_counter = 0
                for i in range(0, len(forecast), 2):
                    if row_counter % 2 == 0:
                        col1, col2 = st.columns(2)
                        with col1:
                            display_forecast_entry(forecast[i])
                        with col2:
                            if i + 1 < len(forecast):
                                display_forecast_entry(forecast[i + 1])
                    row_counter += 1

def display_forecast_entry(data):
    icon_url, temperature, description, dt_object = data
    st.markdown(f"**{dt_object.strftime('%A, %d %B %Y %I:%M %p')}**")
    image = Image.open(requests.get(icon_url, stream=True).raw)
    st.image(image, caption='', width=100)
    st.write(f"Temperature: {temperature}°C")
    st.write(f"Description: {description}")
    st.write("---")

if __name__ == "__main__":
    main()
