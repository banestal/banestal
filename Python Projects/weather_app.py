import requests
from prettytable import PrettyTable

#This function grabs data from the OpenWeather API website
def getWeather(city, apiKey):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": apiKey,
        "units": "imperial"
    }
    response = requests.get(baseUrl, params=params) 
    weatherData = response.json() 
    return weatherData

#This prints out the table using the prettytable module
def printWeatherData(weatherData):
    weatherTable = PrettyTable()
    
    weatherTable.field_names = ["City", "Temperature (F)", "Humidity (%)", "Pressure (hPa)"]
    weatherTable.add_row([
        weatherData['name'],
        weatherData['main']['temp'],
        weatherData['main']['humidity'],
        weatherData['main']['pressure']
    ])
    
    print(weatherTable)


apiKey = '56247e457f766730964fcba05cbb1ae8' #My offical API code to be used
userWelcome = input("Welcome To My Weather App! (Press Any Key)") #Just a random welcome to make the user feel engaged
city = input("What's the name of your city?: ") # Whatever they input gets searched through the API
weatherData = getWeather(city, apiKey) 

printWeatherData(weatherData)

