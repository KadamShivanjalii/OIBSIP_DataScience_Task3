"""
Unemployment Analysis in India
Dataset: Unemployment_Rate_upto_11_2020.csv
Platform: Google Colab
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (uploaded in Google Colab)
df = pd.read_csv('/content/Unemployment_Rate_upto_11_2020.csv')

# Display dataset information
print("Dataset Shape:", df.shape)
print("\nDataset Information:")
print(df.info())

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plot unemployment rate over time
plt.figure(figsize=(8,5))
plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'])
plt.xlabel("Date")
plt.ylabel("Estimated Unemployment Rate (%)")
plt.title("Unemployment Rate in India Over Time")
plt.tight_layout()
plt.show()
