import requests
import json
from datetime import datetime

API_KEY = "2337f56db94f4ed3a4aab62163e3d997"


def humidity(lat, lon, date, date_end):
    url = (
        f"https://api.weatherbit.io/v2.0/history/agweather"
        f"?lat={lat}&lon={lon}&start_date={date}&end_date={date_end}&key={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()

    soil_moisture_0_10 = data["data"][0].get("v_soilm_0_10cm", 0) * 100
    soil_moisture_10_40 = data["data"][0].get("v_soilm_10_40cm", 0) * 100

    return {
        "soil_moisture_0_10_cm": soil_moisture_0_10,
        "soil_moisture_10_40_cm": soil_moisture_10_40
    }


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


def save_to_json(lat, lon, start_date, end_date, filename="aguacate_data.json"):
    soil_data = humidity(lat, lon, start_date, end_date)
    climate_data = climate_current(lat, lon)

    json_data = {
        "location": {
            "latitude": lat,
            "longitude": lon
        },
        "date": {
            "start": start_date,
            "end": end_date,
            "timestamp": datetime.now().isoformat()
        },
        "soil_data": soil_data,
        "climate_data": climate_data,
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

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

    print(f"✅ Datos guardados correctamente en {filename}")


# ▶️ EJECUCIÓN
"""save_to_json(
    lat=19.4326,
    lon=-99.1332,
    start_date="2025-07-01",
    end_date="2025-07-02"
)"""
