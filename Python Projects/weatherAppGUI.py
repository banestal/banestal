from tkinter import *
from tkinter import ttk
from prettytable import PrettyTable
import requests
from datetime import datetime

#This function grabs data from the OpenWeather API website
def get_weather(city, apiKey):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": apiKey,
        "units": "metric"
    }
    response = requests.get(baseUrl, params=params) 
    weatherData = response.json() 
    return weatherData

#This prints out the table using the prettytable module
def printWeatherData(weatherData):
    weatherTable = PrettyTable()
    
    weatherTable.field_names = ["City", "Temp(C)", "Humid(%)", "(hPa)", "Time"]
    weatherTable.add_row([
        weatherData['name'],
        weatherData['main']['temp'],
        weatherData['main']['humidity'],
        weatherData['main']['pressure'],
        datetime.fromtimestamp(weatherData['dt']).strftime('%H:%M')
    ])
    
    resultLabel.config(text=str(weatherTable))
    
def grabWeather():
    city = cityEntry.get()
    weatherData = get_weather(city, apiKey)
    printWeatherData(weatherData)
    
apiKey = '56247e457f766730964fcba05cbb1ae8' #My offical API code to be used

#TK window
window = Tk()
window.title("Weather App")
window.configure(bg='#ADD8E6') #Changes the Background Color
window.geometry("700x300")

# Changing the font size, family and color
style = ttk.Style(window)
style.configure("TLabel", font=("Arial", 15), foreground="blue", background='#ADD8E6')
style.configure("TButton", font=("Arial", 14), foreground="black")
style.configure("TEntry", font=("Arial", 14), foreground="black")

cityLabel = ttk.Label(window, text="Enter City Name:")
cityLabel.pack(pady=10)
cityEntry = ttk.Entry(window)
cityEntry.pack(ipadx=10, ipady=5, pady=10)

getWeatherButton = ttk.Button(window, text="Get Weather", command=grabWeather)
getWeatherButton.pack(ipadx=10, ipady=5, pady=10)

resultLabel = ttk.Label(window)
resultLabel.pack(pady=10)

#Running the event loop
window.mainloop()
