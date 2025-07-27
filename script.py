import pandas as pd

df = pd.read_csv('uber_fares.csv')  

df.head()
# Dataset structure
print("Shape of dataset:", df.shape)

# Column names and data types
print("\nData types:")
print(df.dtypes)

# General info
print("\nDataset info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))

# Drop rows with missing values
df_cleaned = df.dropna()

# Remove invalid passenger counts (Uber only allows 1–6)
df_cleaned = df_cleaned[(df_cleaned['passenger_count'] > 0) & (df_cleaned['passenger_count'] <= 6)]

# Remove invalid fare_amount (no negative fares)
df_cleaned = df_cleaned[df_cleaned['fare_amount'] > 0]

# Remove invalid coordinates (basic range check for NYC region)
df_cleaned = df_cleaned[
    (df_cleaned['pickup_latitude'].between(40, 42)) &
    (df_cleaned['pickup_longitude'].between(-75, -72)) &
    (df_cleaned['dropoff_latitude'].between(40, 42)) &
    (df_cleaned['dropoff_longitude'].between(-75, -72))
]

# Confirm cleaning
print("Shape after cleaning:", df_cleaned.shape)
# Export cleaned dataset to CSV
df_cleaned.to_csv("cleaned_uber_fares.csv", index=False)

import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv('cleaned_uber_fares.csv')

# Descriptive statistics
print("=== Descriptive Statistics ===")
print(df.describe())

# Median
print("\nMedian Fare Amount:", df['fare_amount'].median())

# Mode
print("\nMode Passenger Count:", df['passenger_count'].mode()[0])

# Range (Max - Min)
fare_range = df['fare_amount'].max() - df['fare_amount'].min()
print("\nFare Amount Range:", fare_range)

# Outlier detection using IQR
Q1 = df['fare_amount'].quantile(0.25)
Q3 = df['fare_amount'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['fare_amount'] < (Q1 - 1.5 * IQR)) | (df['fare_amount'] > (Q3 + 1.5 * IQR))]
print("\nOutliers in fare_amount:", outliers.shape[0])

import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set(style="whitegrid")

# Histogram of fare amount
plt.figure(figsize=(10, 6))
sns.histplot(df['fare_amount'], bins=50, kde=True)
plt.title('Distribution of Uber Fare Amounts')
plt.xlabel('Fare Amount ($)')
plt.ylabel('Frequency')
plt.xlim(0, 100)  # limit to remove extreme outliers
plt.show()

# Box plot to detect outliers
plt.figure(figsize=(10, 2))
sns.boxplot(x=df['fare_amount'])
plt.title('Box Plot of Uber Fare Amounts')
plt.xlim(0, 100)  # adjust range if needed
plt.show()

from geopy.distance import geodesic

# Function to calculate distance
def calculate_distance(row):
    pickup = (row['pickup_latitude'], row['pickup_longitude'])
    dropoff = (row['dropoff_latitude'], row['dropoff_longitude'])
    return geodesic(pickup, dropoff).km

# Apply to dataframe (this may take a few minutes)
df['trip_distance_km'] = df.apply(calculate_distance, axis=1)

# Save updated dataset
df.to_csv("enhanced_uber_fares.csv", index=False)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='trip_distance_km', y='fare_amount', data=df, alpha=0.3)
plt.title('Fare Amount vs. Trip Distance')
plt.xlabel('Trip Distance (km)')
plt.ylabel('Fare Amount ($)')
plt.xlim(0, 30)
plt.ylim(0, 100)
plt.show()

# Ensure datetime column is in datetime format
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# Extract hour, day, month
df['pickup_hour'] = df['pickup_datetime'].dt.hour
df['pickup_day'] = df['pickup_datetime'].dt.day
df['pickup_month'] = df['pickup_datetime'].dt.month
df['pickup_day_of_week'] = df['pickup_datetime'].dt.day_name()

def categorize_peak(hour):
    if 7 <= hour <= 10 or 16 <= hour <= 19:
        return 'Peak'
    else:
        return 'Off-Peak'

df['time_category'] = df['pickup_hour'].apply(categorize_peak)

# Encode day_of_week and time_category if needed
df['pickup_day_of_week_encoded'] = df['pickup_day_of_week'].astype('category').cat.codes
df['time_category_encoded'] = df['time_category'].astype('category').cat.codes

df.to_csv("enhanced_uber_fares.csv", index=False)


