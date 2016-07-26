from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

from getweather import *

def greeting(request):
  location = request.GET.get('location', '')
  if location == '':
    template = loader.get_template(
  		'current/input.html')
    output = template.render()
    return HttpResponse(output)

  data = fetchWeatherData(location)

  temp = getTemperature(data)
  humidity = getHumidity(data)

  template = loader.get_template(
  	'current/location.html')
  context = {'location': location,
             'temp': temp,
             'humidity': humidity}
  output = template.render(context)
  return HttpResponse(output)