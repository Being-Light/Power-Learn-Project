import requests
from django.shortcuts import render
from django.http import HttpResponse

def weather_view(request):
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API Key
    city = 'London'  # Default city
    
    if 'city' in request.GET:
        city = request.GET['city']

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return render(request, 'weather/weather.html', weather_data)
    else:
        return HttpResponse("Error fetching weather data", status=500)
