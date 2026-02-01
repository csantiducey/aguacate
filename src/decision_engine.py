# IRRIGATION PREDICTION
import json

# PARAMETERS FOR THE AVOCADO
field_capacity = 38.0 # max % of water soil plant can hold
wilting_point = 26.74 # min amount of water soil begfore plant dies
mad_threshold = 0.4   # percetage of water depletion before causing root stress

def predict_irrigation(moisture_data: json, weather_data: json, age, forecast=14) -> dict:
    '''Use the weather data to make a forecast of soil humidity'''

    # 1. Load cached Data
    with open(moisture_data, 'r') as f:
        soil_data = json.load(f)
    
    with open(weather_data, 'r') as f:
        weather_forecast = json.load(f)

    # 2. Compute the Critical Moisture
    critical_moisture = wilting_point + (field_capacity - wilting_point) + mad_threshold
    # 3. Compute the Soil Moisture Projections
    
    predictions = []
    sm = soil_data["soil_data"]["soil_moisture_10_40_cm"]

    for day in range(1, forecast):

        dailyAvgTemp = weather_forecast["daily"]["temperature_2m_mean"]
        precipitation = weather_forecast["daily"]["precipitation_sum"]

        
        if age < 4: kc = 0.4
        else: kc = 0.75

        et = 0.15 * dailyAvgTemp[day] * kc

        # Compute the Soil Moisture Prediction
        sm_new = ((sm / 100) * 40) + precipitation[day] - et

        # 3. Compare with Threshold to suggest action
        status = "NO IRRIGATION NEEDED FOR 24 HRS"

        if sm_new < critical_moisture and precipitation[day] < 10 :
            status = "IRRIGATE TODAY"
            
        
        predictions.append({"date": weather_forecast["daily"]["time"][day],
                            
                            "predicted_humidity": round(sm_new, 2),

                            "recommendation": status
        })

        sm = sm_new

        if status == "IRRIGATE TODAY": break

    return predictions

if __name__ == "__main__":
    results = predict_irrigation("data/raw/moisture.json", "data/raw/weather_data.json", 3)
    print(results)

        



    


