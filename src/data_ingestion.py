import requests


API_KEY = "2337f56db94f4ed3a4aab62163e3d997"


def humidity(lat,lon,date,date_end):
    URL =f"https://api.weatherbit.io/v2.0/history/agweather?lat={LAT}&lon={LON}&start_date={date}&end_date={date_end}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    soil_moisture_0_10 = data["data"][0].get("v_soilm_0_10cm")
    soil_moisture_10_40 = data["data"][0].get("v_soilm_10_40cm")
