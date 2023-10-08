import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests

with open ('mywork\mydata.json') as json_file:
    data = json.load(json_file)

timestamps = [entry["Timestamp (Hour Ending)"] for entry in data["series"][0]["data"]]
values = [entry["value"] for entry in data["series"][0]["data"]]

timestamps = [timeval.replace("a.m.", "AM").replace("p.m.", "PM") for timeval in timestamps]


timeformat = "%m/%d/%Y %I %p EDT"

timestamps = [datetime.strptime(ts, timeformat) for ts in timestamps]
print(values)

plt.figure(figsize=(12, 6))
plt.plot(timestamps, values, marker='o', linestyle='-', color='b')
plt.title(data["title"])
plt.xlabel("Timestamp (Hour Ending)")
plt.ylabel("Value")
plt.grid(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()