from urllib.error import HTTPError

from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
import json
import urllib.request


# Create your views here.

def index(request):
    if request.method == 'POST':

        search = request.POST['search']
        res = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + search + '&appid''=69b17d96f6e90caf979865cdc6bfd303').read()
        json_data = json.loads(res)
        data = {
            'country': str(json_data['sys']['country']),
            'timezone': str(json_data['timezone']),
            'lon': str(json_data['coord']['lon']),
            'lat': str(json_data['coord']['lat']),
            'temperature': str(json_data['main']['temp'] - 272.15) + ' K',
            'feels_like': str(json_data['main']['feels_like']) + ' K',
            'pressure': str(json_data['main']['pressure']) + ' hPa',
            'speed': str(json_data['wind']['speed']) + ' mph',
            'humidity': str(json_data['main']['humidity']) + '%',
            'visibility': str(json_data['visibility']),
        }
        if HTTPError(404, json_data, data,):
            messages.error(request, 'No City Found')
            return redirect('index')
        else:
            messages.error(request, 'Search for a city to display its weather')
            return redirect('index')

    else:
        search = ''
        data = {}

    return render(request, 'index.html', {'search': search, 'data': data})
