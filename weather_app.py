import tkinter as tk
from tkinter import messagebox
import requests
from typing import Optional

def get_weather(api_key: str, city: str) -> Optional[str]:
    if not api_key:
        raise ValueError("API key must be provided")
    if not city:
        raise ValueError("City must be provided")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant information from the API response
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            clouds = data["clouds"]["all"]
            visibility = data["visibility"]
            dew_point: Optional[float] = data.get("main", {}).get("dew_point")
            rain: Optional[float] = data.get("rain", {}).get("1h", 0)

            # Format the weather information
            weather_info = (
                f"Weather in {city}:\n"
                f"\tTemperature: {temperature}℃\n"
                f"\tFeels Like: {feels_like}°C\n"
                f"\tMin Temperature: {temp_min}℃\n"
                f"\tMax Temperature: {temp_max}℃\n"
                f"\tHumidity: {humidity}%\n"
                f"\tWind Speed: {wind_speed} m/s\n"
                f"\tCloud Coverage: {clouds}%\n"
                f"\tVisibility: {visibility} m\n"
                f"\tDew Point: {dew_point}°C\n"
                f"\tPressure: {pressure} hPa\n"
                f"\tRain: {rain} mm"
            )
            return weather_info
        else:
            return f"Error: {data['message']}"

    except Exception as e:
        return f"An error occurred: {e}"

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name or PIN code.")
        return

    api_key = "6ac51341fbe25af0043f9a7e166961c4"  # Replace with your actual API key
    weather_info = get_weather(api_key, city)

    # Display the weather information in the result label
    result_label.config(text=weather_info)

# Create the main window
root = tk.Tk()
root.title("GUNAS Weather App")
root.geometry("400x400")  # Increased height for better layout
root.configure(bg="lightblue")

# Create a frame to center the contents
frame = tk.Frame(root, bg="lightblue")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title label with bold font
title_label = tk.Label(frame, text="GUNAS Weather Application", font=("Helvetica", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Input for city name or PIN code with bold font
city_label = tk.Label(frame, text="Enter City Name or PIN Code:", font=("Helvetica", 12, "bold"), bg="lightblue")
city_label.pack(pady=5)
city_entry = tk.Entry(frame, font=("Helvetica", 12, "bold"))
city_entry.pack(pady=5)

# Button to get weather with bold font
get_weather_button = tk.Button(frame, text="Get Weather", command=show_weather, bg="lightgreen", font=("Helvetica", 12, "bold"))
get_weather_button.pack(pady=10)

# Label to display the weather result with bold font
result_label = tk.Label(frame, text="", bg="lightblue", font=("Helvetica", 10, "bold"))
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
