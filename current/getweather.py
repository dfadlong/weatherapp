key = '9dd24f6d5670fd19d270ff159f794d07'

import urllib
import urllib2
import json
import sys


def fetchWeatherData(location):
  address = ('http://api.openweathermap.org/data/2.5/'
	'weather?q=' + urllib.quote(location) + '&appid=' + key)
  request = urllib2.Request(address)
  response = urllib2.urlopen(request)
  reply = response.read()
  return reply

def getTemperature(data):
  data = json.loads(data)
  temp = data['main']['temp']
  fahrenheight = temp * 9 / 5 - 459.67
  return fahrenheight

def getHumidity(data):
  data = json.loads(data)  
  humidity = data['main']['humidity']
  return humidity

def getDescription(data):
  data = json.loads(data)  
  description = data['weather'][0]['description']
  return description
