import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests

api_url = "https://api.eia.gov/v2/electricity/rto/region-data/data/?api_key=Sr32RhpckMKBDCIz8HzmaB0Y7dKDW0T90edtf0rN&frequency=hourly&data[0]=value&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"

x_params = {
    "frequency": "hourly",
    "data": [
        "value"
    ],
    "facets": {},
    "start": None,
    "end": None,
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000
}

x_params_json = json.dumps(x_params)

headers = {
    "X-Params": x_params_json,
    "Content-Type": "application/json", 
}

def get_graph():
    response = requests.get(api_url, headers=headers)


    if response.status_code == 200:

        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(response.status_code)
        quit()
        
    # values = [entry["value"] for entry in data["response"]["data"]]
    # times = [entry["period"] for entry in data["response"]["data"]]

    # times = [pd.to_datetime(time) for time in times]

    # plt.figure(figsize=(10, 6))
    # plt.scatter(times, values, marker='o', color='b')
    # plt.title("Electricity Demand")
    # plt.xlabel("Period (MM-DD Hour)")
    # plt.ylabel("Demand (megawatthours)")
    # plt.xticks(rotation=45)
    # plt.grid(True)

    # plt.tight_layout()
    # plt.show()


