import requests
from PIL import Image
import streamlit as st

# Constants
API_KEY = "9f1e1d3a18d40be562129baafe0dae67"

# Define custom CSS styles
CUSTOM_STYLE = """
<style>
    .stTextInput>div>div>input {
        background-color: #0f081c !important;
        border: 2px solid #ccc !important;
        border-radius: 5px !important;
        padding: 10px !important;
    }
    .stButton>button {
        background-color: #4CAF50 !important;
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
        background-color: #45a049 !important;
    }
</style>
"""


# Function to fetch weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}"
    response = requests.get(url)

    if response.status_code == 404:
        st.error("City Not Found")
        return None
    else:
        # Parse the response JSON to get weather information
        weather_data = response.json()
        temperature = int(((weather_data['main']['temp']) - 32) * (5 / 9))
        description = weather_data['weather'][0]['description']
        city_name = weather_data['name']
        country = weather_data['sys']['country']

        # Get the icon URL and return all the weather information
        icon_url = f"https://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}.png"
        return [icon_url, temperature, description, city_name, country]


# Main function
def main():
    # Add custom CSS
    st.markdown(CUSTOM_STYLE, unsafe_allow_html=True)

    # Title
    st.title("Sky View")

    # Input for city
    city = st.text_input("Enter City:", "")

    # Search button
    if st.button("Search"):
        if city:
            result = get_weather(city)
            if result:
                # Unpack the weather information
                icon_url, temperature, description, city_name, country = result

                # Display city and country
                st.markdown(f"<h2 style='text-align:center;'>{city_name}, {country}</h2>", unsafe_allow_html=True)

                # Display weather icon
                image = Image.open(requests.get(icon_url, stream=True).raw)
                image = image.resize((100, 100))  # Adjust the size here
                st.image(image, caption='', use_column_width=True)

                # Display temperature
                st.markdown(f"<p style='text-align:center;font-size:20px;'>Temperature: {temperature}°C</p>",
                            unsafe_allow_html=True)

                # Display weather description
                st.markdown(f"<p style='text-align:center;font-size:20px;'>Description: {description}</p>",
                            unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    main()
