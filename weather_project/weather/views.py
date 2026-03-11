from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import requests

API_KEY = 'e5d24466ad1b033f75cbf0d69415650a'

def index(request):
    return render(request, 'weather/index.html')

@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city')
    if not city:
        return Response({'error': 'City is required'}, status=status.HTTP_400_BAD_REQUEST)

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()

        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'].title(),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return Response(weather)
    except requests.exceptions.HTTPError:
        return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
