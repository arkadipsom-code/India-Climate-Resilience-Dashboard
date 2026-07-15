import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from modules.risk_engine import calculate_indices

def forecast_city_trends(df, target_year):
    
    forecasted_data = []
    years_ahead = target_year - 2026
    
    
    X_train = np.array([[2016], [2021], [2026]])
    
    for _, row in df.iterrows():
        city = row["City"]
        
        
        current_pop = row["Population"]
        growth_rate = row["Population_Growth_Rate"] / 100
        future_pop = current_pop * ((1 + growth_rate) ** years_ahead)
        
        
        # --- Temperature Model Fitting ---
        current_temp = row["Average_Summer_Temperature"]
        y_temp_train = np.array([current_temp - 0.4, current_temp - 0.2, current_temp])
        
        model_temp = LinearRegression()
        model_temp.fit(X_train, y_temp_train)
        
        future_temp = model_temp.predict(np.array([[target_year]]))[0]
        
        # --- Heatwave Frequency Model Fitting ---
        current_heat_days = row["Heatwave_Days"]
        
        y_heat_train = np.array([current_heat_days - 5, current_heat_days - 2, current_heat_days])
        
        model_heat = LinearRegression()
        model_heat.fit(X_train, y_heat_train)
        future_heat_days = model_heat.predict(np.array([[target_year]]))[0]
        
       
        current_water_ratio = row["Water_Demand_Supply_Ratio"]
        future_water_ratio = current_water_ratio * (1 + (growth_rate * 0.5 * years_ahead))
        
        
        future_metrics = {
            "City": city,
            "Population": int(future_pop),
            "Area": row["Area"],
            "Population_Density": round(future_pop / row["Area"], 2),
            "Population_Growth_Rate": row["Population_Growth_Rate"],
            "Average_Summer_Temperature": round(future_temp, 1),
            "Heatwave_Days": max(0, int(future_heat_days)),
            "Annual_Rainfall": row["Annual_Rainfall"], # Constant base climate variable
            "Extreme_Rainfall_Days": row["Extreme_Rainfall_Days"],
            "Groundwater_Depletion": row["Groundwater_Depletion"],
            "Water_Demand_Supply_Ratio": round(future_water_ratio, 2),
            "Sewage_Treatment_Coverage": row["Sewage_Treatment_Coverage"],
            "Road_Density": row["Road_Density"],
            "Green_Cover_Percentage": row["Green_Cover_Percentage"],
            "Public_Transport_Score": row["Public_Transport_Score"]
        }
        forecasted_data.append(future_metrics)
        
    
    forecasted_df = pd.DataFrame(forecasted_data)
    
    
    final_forecasted_df = calculate_indices(forecasted_df)
    
    return final_forecasted_df