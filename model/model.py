from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

data = pd.read_csv('model/electricity_prices.csv')

# Assuming the CSV file has two columns: 'Timestamp' and 'Price'
timestamps = pd.to_datetime(data['Timestamp'])
prices = data['Price']

# Define the number of clusters (charge times) you want to identify
num_clusters = 3  # You can adjust this based on your needs

# Reshape the data into a 2D array
X = np.column_stack((np.arange(len(timestamps)), prices))

# Use K-Means clustering to identify optimal charging times
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(X)
data['Cluster'] = kmeans.labels_

# Calculate the cluster centers (optimal charge times)
cluster_centers = kmeans.cluster_centers_
cluster_centers = sorted(cluster_centers, key=lambda x: x[1])
optimal_charge_time = cluster_centers[0][0]

# Set the threshold for charging
threshold_price = cluster_centers[0][1]

# Function to determine if the battery should charge based on predicted future prices


def should_charge(predicted_price, threshold):
    return predicted_price < threshold


# Fit an ARIMA model to predict future prices
model = ARIMA(prices, order=(5, 1, 0))
model_fit = model.fit()
forecast_steps = 24  # Number of hours to forecast into the future
# forecast, stderr, conf_int = model_fit.forecast(steps=forecast_steps)
forecast = model_fit.forecast(steps=forecast_steps)

# Predict when to charge in the future based on forecasted prices
future_timestamps = [timestamps.iloc[-1] +
                     timedelta(hours=i) for i in range(1, forecast_steps + 1)]
future_prices = forecast.tolist()

future_charging_decisions = [should_charge(
    price, threshold_price) for price in future_prices]

# Print the results
print("            ")
print("            ")
print("            ")
print("Optimal Charge Time (Hour of the day):", int(optimal_charge_time))
print("Threshold Price:", threshold_price)

print("\nFuture Price Predictions:")
future_data = pd.DataFrame({'Timestamp': future_timestamps,
                           'Predicted_Price': future_prices, 'ShouldCharge': future_charging_decisions})
print(future_data)

# Visualization of data and optimal charge times
plt.scatter(data['Timestamp'], data['Price'],
            c=data['Cluster'], cmap='viridis')
plt.xlabel('Timestamp')
plt.ylabel('Price')
plt.title('Electricity Price vs. Time with Optimal Charge Times')

# Convert the optimal charge time to a string
optimal_charge_time_str = str(timestamps[optimal_charge_time])

# Plot the vertical line at the optimal charge time
plt.axvline(x=optimal_charge_time_str, color='r',
            linestyle='--', label='Optimal Charge Time')
plt.legend()


# Create and plot the second figure
plt.figure()
plt.plot(future_data['Timestamp'],
         future_data['Predicted_Price'], label='Predicted Price')
plt.axhline(y=threshold_price, color='r',
            linestyle='--', label='Threshold Price')
plt.xlabel('Timestamp')
plt.ylabel('Price')
plt.title('Future Price Predictions')
plt.legend()

# Display both figures
plt.show()
