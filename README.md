# Sky View 🌤️

A lightweight weather forecast app built with **Streamlit** that displays upcoming weather conditions for any city using the OpenWeatherMap API.

---

## Features

- Search weather forecasts by city name
- Displays temperature, conditions, and weather icons
- Shows forecasts in a clean 2-column grid layout
- Custom dark-themed UI

---

## Requirements

```
streamlit
requests
Pillow
```

Install with:

```bash
pip install streamlit requests Pillow
```

---

## Setup

1. Grab a free API key from [openweathermap.org](https://openweathermap.org/api)
2. Replace the `API_KEY` value in the script with your own key
3. Run the app:

```bash
streamlit run app.py
```

---

## Usage

Enter a city name in the search box and hit **Search** to load the 5-day / 3-hour forecast.

---

> ⚠️ **Note:** Keep your API key private — avoid committing it directly in source code. Consider using environment variables or a `.env` file instead.
