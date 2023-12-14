# Client Code
#Shreeji Patel
#FINAL PROJECT
#FLASK WEATHER APP

import requests
from datetime import datetime, timedelta
import pytz

def get_weather_from_server(location_input):
    # Make a request to the Flask server for weather data
    response = requests.get(f"http://localhost:5000/weather?location={location_input}")
    return response.json()

def format_time(time_str, timezone_str="America/Chicago"):
    # Convert UTC time to local time
    utc_time = datetime.fromisoformat(time_str.replace("Z", "+00:00"))
    local_time = utc_time.astimezone(pytz.timezone(timezone_str))
    return local_time.strftime("%Y-%m-%d %H:%M:%S")

def convert_direction(direction):
    # Convert wind direction in degrees to a compass direction
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = int(round(direction / 22.5)) % 16
    return directions[index]

def display_weather(data):
    if "data" not in data:
        print("No weather data available.")
        return

    hourly_data = data["data"]["timelines"][0]["intervals"]
    daily_data = data["data"]["timelines"][1]["intervals"]
    current_time = datetime.now(pytz.timezone("America/Chicago"))

#Print Hourly Forecasts weather. Note- the daily forecasts is the average of the whole day which is 12 hour from when the program is ran. 
    print("\nHourly Weather Forecast:")
    for i, hour in enumerate(hourly_data):
        local_time = format_time(hour["startTime"], "America/Chicago")
        temp = hour["values"]["temperature"]
        humidity = hour["values"]["humidity"]
        wind_gust = hour["values"]["windGust"]
        wind_speed = hour["values"]["windSpeed"]
        wind_direction = convert_direction(hour["values"]["windDirection"])
        precipitation = hour["values"].get("precipitationIntensity")

        #icons indicating weather
        if precipitation:
            icon = "☔️"
        elif wind_gust > 20:
            icon = "🌬"
        elif humidity > 70:
            icon = "☁️"
        else:
            icon = "☀️"

        print(f"{i+1:2}: {local_time}:Temperature:{temp}°F {icon},Humidity: {humidity}%, Wind Gust: {wind_gust} mph, Wind Speed: {wind_speed} mph, Wind Direction: {wind_direction}")
        if precipitation:
            print(f"Precipitation: {precipitation} mm/hr")

#Print Daily Forecasts weather. Note- the daily forecasts is the average of the whole day which is 12 hour from when the program is ran. 
    print("\nDaily Weather Forecast:")
    for i, day in enumerate(daily_data[:6]):
        date = current_time + timedelta(days=i)
        formatted_date = date.strftime("%a, %b %d")
        temp = day["values"]["temperature"]
        humidity = day["values"].get("humidity")
        wind_gust = day["values"].get("windGust")
        wind_speed = day["values"].get("windSpeed")
        wind_direction = convert_direction(day["values"].get("windDirection"))

        #icons indicating weather
        if precipitation:
            icon = "☔️"
        elif wind_gust > 20:
            icon = "🌬"
        elif humidity > 70:
            icon = "☁️"
        else:
            icon = "☀️"

        print(f"{formatted_date}:Temperature: {icon} {temp}°F,Humidity: {humidity}%, Wind Gust: {wind_gust} mph, Wind Speed: {wind_speed} mph, Wind Direction: {wind_direction}")

if __name__ == "__main__":
    print("Make sure to Capitalize the first letter of the city, the state has to be an acronym such as TN, and the country fully capitalized.")
    location_input = input("Enter a city name and state and country (e.g., Murfreesboro, TN , USA): ")
    weather_data = get_weather_from_server(location_input)
    display_weather(weather_data)
