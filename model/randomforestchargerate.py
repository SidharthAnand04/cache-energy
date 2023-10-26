import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load your data from the CSV file
data = pd.read_csv('randomforestdata.csv')

# Extract the features (independent variables)
timestamps = pd.to_datetime(data['Timestamp'])
prices = data['Price']
demand = data['Demand']

# Convert the datetime values to numeric using a timestamp representation
timestamps_numeric = (timestamps - timestamps.min()) / np.timedelta64(1, 'D')

print(timestamps_numeric)

# Combine the numeric features into a DataFrame
features = pd.DataFrame({'Timestamp': timestamps_numeric, 'Price': prices, 'Demand': demand})

# Extract the target variable (dependent variable)
chargerate = data['Charge Rate']

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
print(f"Mean Squared Error: {mse}")

newtimestamp = ['2023-10-01 00:00:00']
newtimestamp = pd.to_datetime(newtimestamp)
newtimestamp_numeric = (newtimestamp - newtimestamp.min()) / np.timedelta64(1, 'D')
print(newtimestamp_numeric)

# Create a new DataFrame with the features for the data you want to predict
new_data = pd.DataFrame({'Timestamp': newtimestamp_numeric, 'Price': 50, 'Demand': 439690})

# Use the trained model to make a prediction
predicted_charge_rate = rf_model.predict(new_data)

# The variable 'predicted_charge_rate' now contains the predicted charge rate for your new data point.
print(f"Predicted Charge Rate: {predicted_charge_rate[0]}")

#visualization for accuracy
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, alpha=0.5)
plt.xlabel("Actual Charge Rate")
plt.ylabel("Predicted Charge Rate")
plt.title("Actual vs. Predicted Charge Rate")
plt.grid(True)
plt.show()


# create predictions here
newtimestamp = ['2023-10-01 00:00:00']
newtimestamp = pd.to_datetime(newtimestamp)
newtimestamp_numeric = (newtimestamp - newtimestamp.min()) / np.timedelta64(1, 'D')

newprice = 50
newdemand = 439690

# Create a new DataFrame with the features for the data you want to predict
new_data = pd.DataFrame({'Timestamp': newtimestamp_numeric, 'Price': newprice, 'Demand': newdemand})

# Use the trained model to make a prediction
predicted_charge_rate = rf_model.predict(new_data)

# The variable 'predicted_charge_rate' now contains the predicted charge rate for your new data point.
print(f"Predicted Charge Rate: {predicted_charge_rate[0]}")
