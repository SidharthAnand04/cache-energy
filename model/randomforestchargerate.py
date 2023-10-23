import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import requests
from matplotlib.ticker import ScalarFormatter
import csv
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

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

response = requests.get(api_url, headers=headers)

if response.status_code == 200:

    data = response.json()
    
else:
    print("Failed to retrieve data. Status code: {response.status_code}")
    print(response.status_code)
    quit()

##filter for only useful energy demand values
filtered_data = [(entry['period'], entry['value']) for entry in data['response']['data'] if isinstance(entry['value'], int) and entry['value'] > 300000]
times, values = zip(*filtered_data)



##converting from the file's timestamps format to ints for the random forest model
def convert_timestamp_format(timestamp_str):
    parts = timestamp_str.split('T')
    if len(parts) == 2:
        date_part, time_part = parts
        year, month, day = map(int, date_part.split('-'))
        hour = int(time_part)
        return year, month, day, hour
    else:
        # Handle the case when the format is not as expected
        return None

# Apply the conversion to the entire list
new_data = [(*convert_timestamp_format(date_str), value) for date_str, value in filtered_data]


##fake price value generation
def generate_random_price():
    return random.randint(15, 30)

# Add the price value to each tuple
result1 = [(year, month, day, hour, value, generate_random_price()) for year, month, day, hour, value in new_data]

##fake charge rate value generation
def generate_random_chargerate():
    return random.random()

# Add a random value to each tuple
result2 = [(year, month, day, hour, value, price, generate_random_chargerate()) for year, month, day, hour, value, price in result1]

##set features and target from result 2 list
features = [(item[0], item[1], item[2], item[3], item[4], item[5]) for item in result2]
target = [item[6] for item in result2]

# Split the data into a training set (80%) and a testing set (20%)
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model on the training data
rf_model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = rf_model.predict(X_test)

# Evaluate the model's performance (you can use appropriate metrics depending on your problem, such as Mean Absolute Error, Mean Squared Error, etc.)
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

# You can use the model to predict the fourth value for new data

'''
new_data = [(new features here)]
new_predictions = rf_model.predict(new_data)

'''