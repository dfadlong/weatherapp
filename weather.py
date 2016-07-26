key = '9dd24f6d5670fd19d270ff159f794d07'

import urllib2
import json


def fetchWeatherData(location):
  address = ('http://api.openweathermap.org/data/2.5/'
	'weather?q=' + location + '&appid=' + key)
  request = urllib2.Request(address)
  response = urllib2.urlopen(request)
  reply = response.read()
  return reply

def getTemperature(location):
  data = json.loads(fetchWeatherData(location))
  temp = data['main']['temp']
  fahrenheight = temp * 9 / 5 - 459.67
  return fahrenheight

def getHumidity(location):
  data = json.loads(fetchWeatherData(location))  
  humidity = data['main']['humidity']
  return humidity

nyc_temp = getTemperature('NYC')
print(nyc_temp)
nyc_humidity = getHumidity('NYC')
print(nyc_humidity)


