from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3cdb6d958eea092dd4f5c26eecd7036e"
    cities = City.objects.all() #get all the cities from the database

    #only true if the form is submitted
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'country':city_weather['sys']['country']
        }

        weather_data.append(weather) # add the current data for our city to the list

    context = { 'weather_data':weather_data,'form':form}

    return render(request,'weather/index.html',context)