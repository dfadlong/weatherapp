key = '9dd24f6d5670fd19d270ff159f794d07'

import urllib2
import json


def fetchWeatherData():
  address = ('http://api.openweathermap.org/data/2.5/'
	'weather?q=NYC&appid=' + key)
  request = urllib2.Request(address)
  response = urllib2.urlopen(request)
  reply = response.read()
  return reply

def getTemperature():
  data = json.loads(fetchWeatherData())
  temp = data['main']['temp']
  fahrenheight = temp * 9 / 5 - 459.67
  print(fahrenheight)

getTemperature()
