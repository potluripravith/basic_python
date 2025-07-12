# weather_service.py
import requests

# weather_service.py (updated)
def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=API_KEY&units=metric"
        response = requests.get(url)
        
        if response.status_code != 200:
            return None
            
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
            
    except (ValueError, KeyError, IndexError):
        return None