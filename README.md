# FLASKWEATHERAPP
Project- 
The project involves building a Flask-based weather application. 
The server interacts with the Tomorrow.io API to retrieve weather data, while the client, using Python, makes requests to the server and displays the weather information. 
The client provides hourly and daily weather forecasts for a specified location, ensuring accurate formatting of user inputs for city, state, and country.
Note - the hourly data is provided for next 6 hours only and is a rough estimate of average weather. the daily weather data is also a average of the whole day(24hrs)
and it might vary 4-5 degrees from other weather sources such as weather.com etc. The timestamps for hourly data may or may not update since i am using a free version
of API and it has few restrictions. All the other field such as humidity, wind speed, wind gusts, wind direction may also vary a bit from actual numbers shown
on weather apps. 


Implementation- 
This project involves a Flask weather app. Technologies used - PYTHON,FLASK,API'S
Libraries include Flask for the server, requests for API calls, datetime for time handling, and pytz for timezone conversion. 
The client uses Python with requests for HTTP communication, fetching and displaying weather data from a Flask server. 
The server, implemented in Flask, connects to the Tomorrow.io API, retrieves weather information based on user input, and returns it as JSON. 
The client then processes and displays this information. 
The server handles API requests, validates user input, 
and communicates with the external weather API, while the client focuses on user interaction and displaying the received data.



Instructions -

flask server, request libraries installation may be necessary depending on the computer or Jupyterlab where this program is tested on. 
To install flask server into Jupyterlab use the following command - pip install flask
To install requests library into Jupyterlab use the following command - pip install requests
The installation of flask server and requests library will have to be done before compiling and testing the programs. 

To compile and run the program
make sure when the program is tested its in the corrrect directory. 
1. Load Server.py and Client.py in JupyterLab
2. Compile the Server.py using  - python Server.py
3. Compile the Client.py using - python Client.py
4. It will prompt the user for the location. It will print something like this:
Make sure to Capitalize the first letter of the city, the state has to be an acronym such as TN, and the country fully capitalized.
Enter a city name and state and country (e.g., Murfreesboro, TN , USA):

Enter the cityname, state and country as shown. The programs lets you search forecasts for United states. It is capable of providing data for other countires
but the data is not consistent all the time due to API restrictions. For this project i am using Tomorrow.io API which limits me to making only 1000 calls a day
which is plenty to test this program. 
The plan i have for this API is limited to me using field such as -temperature,humidity,windSpeed,windGust,windDirection,precipitationIntensity.



LINK TO THE DEMO VIDEO - https://youtu.be/4xzaP74Lq_c
