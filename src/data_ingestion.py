# EXTRACT THE DATA USED FOR MODEL FROM API'S
import requests as req
import os
import json

def open_meteo_weather(lat: float, lon: float) -> dict:
    '''Retrieves the Daily Precipitation Sum and Mean Temperature'''

    url = "https://api.open-meteo.com/v1/forecast"

    params = {"latitude": lat,
              "longitude": lon,
              "daily": ["precipitation_sum", "temperature_2m_mean"],
              "forecast_days": 14,
              "timezone": "auto" 
               
            }
    response = req.get(url, params=params)
    data = response.json()


    return data

def cache_weather_data(data: dict) -> None:

    path = os.path.join("data/raw", "weather_data.json")

    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    except req.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    return None
    


if __name__ == "__main__":
    lat, lon = 19.411, -102.056
    data = open_meteo_weather(lat, lon)
    cached_data = cache_weather_data(data)
    
    