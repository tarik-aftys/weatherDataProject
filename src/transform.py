import json
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)

input_file = os.path.join(project_dir, "data", "raw", "weather_raw.json")
output_file = os.path.join(project_dir, "data", "processed", "weather_clean.csv")

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

hourly_data = data["hourly"]

df = pd.DataFrame({
    "time": hourly_data["time"],
    "temperature 2m": hourly_data["temperature_2m"],
    "relative humidity 2m": hourly_data["relative_humidity_2m"],
    "wind speed 10m": hourly_data["wind_speed_10m"]
})

df["time"] = pd.to_datetime(df["time"])
df = df.dropna()
os.makedirs(os.path.dirname(output_file), exist_ok=True)
df.to_csv(output_file, index=False, encoding="utf-8")

