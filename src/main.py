from data_ingestion import open_meteo_weather, cache_weather_data, get_soil_moisture, cache_moisture_data
from decision_engine import predict_irrigation

def main(lat, lon):
    weather_data = open_meteo_weather(lat, lon)
    cache_weather_data(weather_data)
    soil_data = get_soil_moisture(lat, lon)
    cache_moisture_data(lat, lon)

    # Irrigation Prediction
    predictions = predict_irrigation("data/raw/moisture.json", "data/raw/weather_data.json", 3)
    print(predictions)


if __name__ == "__main__":
    lat, lon = 19.411, -102.056
    main(lat, lon)