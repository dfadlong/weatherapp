key = '9dd24f6d5670fd19d270ff159f794d07'

import urllib2

address = ('http://api.openweathermap.org/data/2.5/'
	'weather?q=NYC&appid=' + key)

request = urllib2.Request(address)

response = urllib2.urlopen(request)

reply = response.read()

import json
data = json.loads(reply)

temp = data['main']['temp']

fahrenheight = temp * 9 / 5 - 459.67

print(fahrenheight)