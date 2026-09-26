import requests

city = input("Enter your city: ")

url = "https://geocoding-api.open-meteo.com/v1/search"

system_params = {
    "name": city,
    "count": 1
}

response = requests.get(url, params=system_params)

data = response.json()

if "results" not in data:
    print("City not found")
else:
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "auto"
    }

    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()

    current = weather_data["current"]

    temperature = current["temperature_2m"]
    time = current["time"]
    wind_speed = current["wind_speed_10m"]

    print(f"City: {city}")
    print(f"Temperature: {temperature} °C")
    print(f"Wind Speed: {wind_speed} km/h")
    print(f"Time: {time}")