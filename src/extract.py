import requests
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
fichier = os.path.join(project_dir, "data", "raw", "weather_raw.json")

url = "https://api.open-meteo.com/v1/forecast"
indent = 4
params = {
    "latitude": 48.85,
    "longitude": 2.35,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    os.makedirs(os.path.dirname(fichier), exist_ok=True)
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
    print(f"Données enregistrées avec succès dans {os.path.abspath(fichier)}")

else:
    print(f"Erreur: Status code {response.status_code}")
    print(response.text)
