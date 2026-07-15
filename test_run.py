import pandas as pd
from modules.risk_engine import calculate_indices
from modules.investment_engine import recommend_investment
from modules.forecast_engine import forecast_city_trends

# 1. Load the raw matrix
raw_data = pd.read_csv("data/city_data.csv")

# 2. Process risks
processed_data = calculate_indices(raw_data)

print("--- CLIMATE RESILIENCE DATA PROCESSING TEST ---")
print(processed_data[["City", "Climate_Resilience_Score", "Resilience_Category"]].head())

# 3. Process a test investment allocation for Mumbai
mumbai_row = processed_data[processed_data["City"] == "Mumbai"].iloc[0]
mumbai_budget = recommend_investment(mumbai_row, 1000)

print("\n--- INVESTMENT RECOMMENDATION FOR MUMBAI (₹1000 CR) ---")
print(mumbai_budget)

kolka_row = processed_data[processed_data["City"] == "Kolkata"].iloc[0]
kolka_budget = recommend_investment(kolka_row, 1000)

print("\n--- INVESTMENT RECOMMENDATION FOR KOLKATA (₹1000 CR) ---")
print(kolka_budget)

data_2040 = forecast_city_trends(raw_data, 2040)

print("\n--- CLIMATE SCENARIO FORECASTING TEST (YEAR 2040) ---")
print(data_2040[["City", "Population", "Average_Summer_Temperature", "Climate_Resilience_Score", "Resilience_Category"]].head())