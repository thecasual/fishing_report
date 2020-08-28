import fishing_report.fishing_report
from fishing_report.weather import weather

import json

with open('conf/fish_report.conf', 'r') as f:
    config = json.load(f)

coords = config['coords']

weather = weather(coords)

print(weather.tonightweather)