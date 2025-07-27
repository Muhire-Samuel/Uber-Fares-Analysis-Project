# 🚕 Uber Fares Analysis Project

This project is part of the coursework for **INSY 8413: Introduction to Big Data Analytics** at [Your Institution], conducted under the guidance of **Eric Maniraguha**.

## 📊 Overview

This analysis explores the Uber Fares Dataset with a focus on understanding fare patterns, ride demand, and location-based trends. Visualizations and insights were generated using **Power BI**.

---

## 📁 Dataset Description

- **Source**: Kaggle - Uber Fares Dataset
- **Features**:
  - `fare_amount`: Uber fare charged (USD)
  - `pickup_datetime`: Timestamp of ride pickup
  - `pickup_longitude` & `pickup_latitude`: GPS coordinates of pickup location
  - `dropoff_longitude` & `dropoff_latitude`: GPS coordinates of drop-off
  - `passenger_count`: Number of passengers

---

## 🧹 Data Cleaning Methodology

1. **Removed missing values** using `dropna()`.
2. **Filtered out outliers** in `fare_amount`, such as values > $100 or < $0.
3. **Validated GPS coordinates** to keep only realistic NYC rides.
4. **Created new columns**:
   - `pickup_hour`
   - `pickup_day_of_week`
   - `trip_distance_km` (using geopy)

---

## 📈 Key Visualizations

- 📌 **Average Fare by Hour**: Revealed fare fluctuations across the day.
- 🔥 **Heat Map of Busiest Periods**: Highest demand seen between 5 PM–8 PM weekdays.
- 🗺️ **Pickup Locations Map**: Geospatial concentration of pickups around Manhattan.
- 👫 **Passenger Count Analysis**: Majority of rides had 1–2 passengers.

---

## 💡 Insights and Outcomes

- **Evening rides** have higher average fares, especially during rush hours.
- **Weekdays** show more consistent ride demand than weekends.
- **Geospatial analysis** shows hotspots in business districts.
- **Trip distance** positively correlates with fare, but not linearly due to base fare and surge pricing.

---

## 📌 Tools Used

- Power BI (visualizations & dashboards)
- Python (data preprocessing)
- Pandas, NumPy, Matplotlib, Seaborn
- Geopy (distance calculation)

---

## 🧠 Author & Course Info

- **Name**: MUHIRE Samuel 26092
- **Instructor**: Eric Maniraguha
- **Course**: INSY 8413 - Introduction to Big Data Analytics
- **Institution**: AUCA

---

## 📎 Report

The full project is available as a PowerPoint presentation in the repository:
- `Uber_Fares_Analysis_Report.pptx`

- ## link of unhanced fiel
- https://drive.google.com/file/d/1pcbaaUO39_ES9IdPOj85nu6awuLrjTdd/view?usp=drive_link

---

