import requests
import json
from datetime import datetime, timedelta
import os

API_KEY = "2337f56db94f4ed3a4aab62163e3d997"

def open_meteo_weather(lat: float, lon: float) -> dict:
    '''Retrieves the Daily Precipitation Sum and Mean Temperature'''

    url = "https://api.open-meteo.com/v1/forecast"

    params = {"latitude": lat,
              "longitude": lon,
              "daily": ["precipitation_sum", "temperature_2m_mean"],
              "forecast_days": 14,
              "timezone": "auto" 
               
            }
    response = requests.get(url, params=params)
    data = response.json()


    return data

def cache_weather_data(data: dict) -> None:

    path = os.path.join("data/raw", "weather_data.json")

    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    print(f"✅ Datos guardados correctamente en {path}")

    return None
    

def get_soil_moisture(lat, lon, date, end_date):
    url = (
        f"https://api.weatherbit.io/v2.0/history/agweather"
        f"?lat={lat}&lon={lon}&start_date={date}&end_date={date + timedelta(days=1)}&key={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    
    soil_moisture_0_10 = data["data"][0].get("v_soilm_0_10cm", 0) * 100
    soil_moisture_10_40 = data["data"][0].get("v_soilm_10_40cm", 0) * 100

    return {
        "soil_moisture_0_10_cm": soil_moisture_0_10,
        "soil_moisture_10_40_cm": soil_moisture_10_40
    }

'''
def climate_current(lat, lon):
    url = (
        f"https://api.weatherbit.io/v2.0/current"
        f"?lat={lat}&lon={lon}&key={API_KEY}&include=minutely"
    )
    response = requests.get(url)
    data = response.json()["data"][0]

    return {
        "temperature_c": data.get("temp"),
        "precipitation_mm": data.get("precip"),
        "relative_humidity_percent": data.get("rh"),
        "weather_description": data.get("weather", {}).get("description")
    }
'''


def cache_moisture_data(lat, lon, today=None, end=None):
    # Sanity check for next month update
    today = datetime.now().date()
    end = today + timedelta(days=14)
    

    soil_data = get_soil_moisture(lat, lon, today, today)
    # climate_data = climate_current(lat, lon)

    json_data = {
        "location": {
            "latitude": lat,
            "longitude": lon
        },
        "date": {
            "start": today.isoformat(),
            "end": end.isoformat(),
            "timestamp": datetime.now().isoformat()
        },
        "soil_data": soil_data,
        "crop_reference": {
            "crop": "aguacate",
            "ideal_conditions": {
                "soil_humidity_percent": 40,
                "temperature_c": [20, 25],
                "annual_water_cm": 130,
                "ph_ideal": [6, 7],
                "ph_minimum": 5
            }
        }
    }
    filename = os.path.join("data/raw", "moisture.json")

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

    print(f"✅ Datos guardados correctamente en {filename}")

    return None


# ▶️ EJECUCIÓN
"""save_to_json(
    lat=19.4326,
    lon=-99.1332,
    start_date="2025-07-01",
    end_date="2025-07-02"
)"""

if __name__ == "__main__":
    lat, lon = 19.411, -102.056
    data = open_meteo_weather(lat, lon)
    cached_data = cache_weather_data(data)
    cached_data2 = cache_moisture_data(lat, lon)
    
    