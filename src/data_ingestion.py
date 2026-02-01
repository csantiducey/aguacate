import requests


API_KEY = "2337f56db94f4ed3a4aab62163e3d997"


def humidity(lat,lon,date,date_end):
    URL =f"https://api.weatherbit.io/v2.0/history/agweather?lat={lat}&lon={lon}&start_date={date}&end_date={date_end}&key={API_KEY}"
    response = requests.get(URL)
    data = response.json()
    soil_moisture_0_10 = data["data"][0].get("v_soilm_0_10cm")*100
    soil_moisture_10_40 = data["data"][0].get("v_soilm_10_40cm")*100
    """print(f"Humedad del suelo (0–10 cm): {soil_moisture_0_10}")
    print(f"Humedad del suelo (10–40 cm): {soil_moisture_10_40}")"""
    return soil_moisture_0_10,soil_moisture_10_40

def climate_current(lat,lon):
    URL=f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={API_KEY}&include=minutely"
    response = requests.get(URL)
    data = response.json()

    # 🌡️ Temperatura actual (°C)
    temperature = data["data"][0].get("temp")

    # 🌧️ Precipitación (mm)
    precipitation = data["data"][0].get("precip")

    # 💧 Humedad relativa (% - usada como % de lluvia aproximado)
    rain_percentage = data["data"][0].get("rh")

    # 🌤️ Clima actual (descripción)
    weather_description = data["data"][0].get("weather", {}).get("description")
    """
    print("Temperatura:", temperature, "°C")
    print("Precipitación:", precipitation, "mm")
    print("Porcentaje de lluvia (humedad):", rain_percentage, "%")
    print("Clima actual:", weather_description)
    """
    return temperature,precipitation,rain_percentage,weather_description
#print(humidity(19.4326 ,-99.1332,"2025-07-01","2025-07-02"))
#print(climate_current(19.4326 ,-99.1332))
