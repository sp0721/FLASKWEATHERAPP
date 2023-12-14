#SERVER CODE
#Shreeji Patel
#FINAL PROJECT
#FLASK WEATHER APP
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = "cfu02Y7fBwjoXDJt5pYCFd0IjJzAsPMX"

@app.route("/weather", methods=["GET"])
def get_weather():
    # Get the location input from the request
    location_input = request.args.get("location", "")
    # Define the fields to retrieve from the API
    fields = "temperature,humidity,windSpeed,windGust,windDirection,precipitationIntensity"
    # Construct the API URL with the location, fields, and API key
    url = f"https://api.tomorrow.io/v4/timelines?location={location_input}&fields={fields}&timesteps=1h,1d&units=imperial&apikey={API_KEY}"

    # Make a request to the Tomorrow.io API
    response = requests.get(url)
    if response.status_code == 200:
        # If the request is successful, return the weather data as JSON
        return jsonify(response.json())
    else:
        # If there's an error, return an error message and status code
        return jsonify({"error": "Unable to fetch weather data"}), response.status_code

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
