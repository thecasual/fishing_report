import requests
import json

class weather():
    def __init__(self, coords):
        self.coords = coords
        #self.url = 'https://api.weather.gov/points/{0}/forecast'.format(self.coords)
        self.url = 'https://api.weather.gov/points/{}'.format(self.coords)
        self.getweather()

    def getweather(self):
        r = requests.get(self.url)

        if r.status_code == 200:
            r_json = r.json()
            forecastHourly_url = r.json()['properties']['forecastHourly']
        else:
            print("Error hitting api!")
            exit()

        j = requests.get(forecastHourly_url)

        if j.status_code == 200:
             forecastHourly = j.json()

        else:
            print("Error hitting api!")
            exit()

        print(forecastHourly)
        
        #response = r.json()['properties']['periods']
        #self.tonightweather = response[1]['detailedForecast']
        #self.allweatherstatuses = response
        #self.afternoonweather = response[0]['detailedForecast']