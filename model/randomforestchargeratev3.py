
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import json
import requests
from matplotlib.ticker import ScalarFormatter
import math  


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

filtered_data = [(entry['period'], entry['value']) for entry in data['response']['data'] if isinstance(entry['value'], int) and entry['value'] > 300000]
times, values = zip(*filtered_data)




# Extract the features (independent variables)
timestamps = pd.to_datetime(times)
prices = []
chargerate = []
demand = values

amplitude1 = 5
amplitude2 = 0.5
frequency = 0.5
n = len(timestamps)
holders = np.linspace(0, n, n)

for holder in holders:
    value = 10 + amplitude1 * math.sin(frequency * holder)  # Cyclic values between 5 and 15
    prices.append(value)



for holder in holders:
    value = 0.5 + amplitude2 * math.sin(frequency * holder)  # Cyclic values between 5 and 15
    chargerate.append(value)

s1 = len(prices)
s2 = len(times)
s3 = len(timestamps)
s4 = len(chargerate)

print(s1)
print(s2)
print(s3)
print(s4)




# Convert the datetime values to numeric using a timestamp representation
timestamps_numeric = (timestamps - timestamps.min()) / np.timedelta64(1, 'D')

# Combine the numeric features into a DataFrame
features = pd.DataFrame({'Timestamp': timestamps_numeric, 'Price': prices, 'Demand': demand})

# Extract the target variable (dependent variable)


# Split the data into a training set (80%) and a testing set (20%)
X_train, X_test, y_train, y_test = train_test_split(features, chargerate, test_size=0.2, random_state=42)

# Initialize the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model on the training data
rf_model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = rf_model.predict(X_test)


# Evaluate the model's performance (e.g., Mean Squared Error)
mse = mean_squared_error(y_test, predictions)


newtimestamp = ['2023-10-01 00:00:00']
newprice = 50
newdemand = 439690

print("Features: ") 
print(newtimestamp, newprice, newdemand)
print(f"Mean Squared Error: {mse}")

newtimestamp = pd.to_datetime(newtimestamp)
newtimestamp_numeric = (newtimestamp - newtimestamp.min()) / np.timedelta64(1, 'D')



# Create a new DataFrame with the features for the data you want to predict
new_data = pd.DataFrame({'Timestamp': newtimestamp_numeric, 'Price': newprice, 'Demand': newdemand})

# Use the trained model to make a prediction
predicted_charge_rate = rf_model.predict(new_data)

# The variable 'predicted_charge_rate' now contains the predicted charge rate for your new data point.

print(f"Predicted Charge Rate: {predicted_charge_rate[0]}")


# uncomment to get visual of actual vs predicted value(linear looking graph)
'''
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, alpha=0.5)
plt.xlabel("Actual Charge Rate")
plt.ylabel("Predicted Charge Rate")
plt.title("Actual vs. Predicted Charge Rate")
plt.grid(True)
plt.show()
'''

#this is visual of actual and predicted vs time(not linear)
# Plotting the graph
plt.figure(figsize=(10, 6))

# Scatter plot for actual values vs. time
plt.scatter(X_test['Timestamp'], y_test, label='Actual', marker='o', color='blue')

# Scatter plot for predicted values vs. time
plt.scatter(X_test['Timestamp'], predictions, label='Predicted', marker='x', color='green')


plt.xlabel("Time")
plt.ylabel("Charge Rate")
plt.title("Actual and Predicted Charge Rate Over Time")
plt.legend()
plt.grid(True)
plt.show()