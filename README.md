🌦️ Sky View Weather Forecast
Sky View is a sleek, web-based weather application built with Streamlit. It fetches real-time 5-day weather forecasts using the OpenWeatherMap API and displays them in a clean, dual-column layout with custom-styled UI elements.

✨ Features
Real-time Forecasts: Fetches up-to-date weather data including temperature and atmospheric conditions.

Visual Icons: Displays official weather icons corresponding to the current conditions.

Custom UI: Enhanced with custom CSS for a dark-themed, modern input and button design.

Responsive Layout: Uses a 2-column grid to display upcoming forecast intervals.

🛠️ Tech Stack
Python 3.x

Streamlit (Web Interface)

Requests (API Calls)

Pillow (PIL) (Image Processing)

OpenWeatherMap API (Weather Data)

🚀 Getting Started
1. Prerequisites
Ensure you have Python installed, then install the required dependencies:

Bash
pip install streamlit requests Pillow
2. Configuration
The app uses an OpenWeatherMap API key. In the current script, it is hardcoded as:
API_KEY = "9f1e1d3a18d40be562129baafe0dae67"

Note: For production or public repositories, it is recommended to use Streamlit Secrets or environment variables to store your API keys.

3. Running the App
Navigate to the project directory and run:

Bash
streamlit run your_filename.py
🖥️ Usage
Enter a City Name in the search bar.

Click the Search button.

View the chronological forecast including dates, times, temperatures (in Celsius), and conditions.
