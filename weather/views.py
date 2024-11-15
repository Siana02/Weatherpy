# views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.conf import settings

def home(request):
    return render(request, 'weather/index.html')

def get_weather(request):
    city = request.GET.get('city', 'Nairobi')
    api_key = settings.OPENWEATHER_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'main': data['main'],
            'weather': data['weather'],
            'sys': data['sys'],  # Includes sunrise and sunset
        }
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'City not found or error occurred'}, status=400)
