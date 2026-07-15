import numpy as np;
import pandas as pd;

def min_max_scaler(series, invert=False):

    min_val = series.min()
    max_val = series.max()

    if min_val == max_val:
        return series * 0.0
    
    normalized = (series - min_val) / (max_val - min_val) * 100

    if invert:
        return 100 - normalized
    return normalized

def calculate_indices(df):
    processed_df = df.copy()

    # Heatwave Risk Index
    temp_score = min_max_scaler(processed_df['Average_Summer_Temperature'])
    heatwave_score = min_max_scaler(processed_df['Heatwave_Days'])
    uhi_score = min_max_scaler(processed_df["Population_Density"])
    processed_df["Heatwave_Risk_Index"] = (temp_score * 0.4) + (heatwave_score * 0.4) + (uhi_score * 0.2)

    # Flood Risk Index
    rainfall_score = min_max_scaler(processed_df['Annual_Rainfall'])
    extreme_rainfall_score = min_max_scaler(processed_df['Extreme_Rainfall_Days'])
    drainage_proxy = min_max_scaler(processed_df["Road_Density"], invert=True)
    processed_df["Flood_Risk_Index"] = (rainfall_score * 0.3) + (extreme_rainfall_score * 0.5) + (drainage_proxy * 0.2)

    # Water Stress Index
    groundwater_score = min_max_scaler(processed_df['Groundwater_Depletion'])
    water_demand_score = min_max_scaler(processed_df['Water_Demand_Supply_Ratio'])
    processed_df["Water_Stress_Index"] = (groundwater_score * 0.5) + (water_demand_score * 0.5)

    # Population Pressure Index
    population_density_score = min_max_scaler(processed_df['Population_Density'])
    growth_score = min_max_scaler(processed_df['Population_Growth_Rate'])
    processed_df["Population_Pressure_Index"] = (population_density_score * 0.5) + (growth_score * 0.5)

    # Infrastructure Readiness Index
    sewage = min_max_scaler(processed_df["Sewage_Treatment_Coverage"])
    green = min_max_scaler(processed_df["Green_Cover_Percentage"])
    transit = min_max_scaler(processed_df["Public_Transport_Score"])
    processed_df["Infrastructure_Readiness_Index"] = (sewage * 0.4) + (green * 0.3) + (transit * 0.3)

    # Final Climate Resilience Score Calculation
    processed_df["Climate_Resilience_Score"] = (
        0.25 * (100 - processed_df["Heatwave_Risk_Index"]) +
        0.25 * (100 - processed_df["Flood_Risk_Index"]) +
        0.20 * (100 - processed_df["Water_Stress_Index"]) +
        0.15 * (100 - processed_df["Population_Pressure_Index"]) +
        0.15 * processed_df["Infrastructure_Readiness_Index"]
    )

    def categorize_resilience_score(score):
        if score >= 80:
            return 'High'
        elif score >= 60:
            return 'Moderate'
        elif score >= 40:
            return 'Vulnerable'
        else:
            return 'Critical'

    processed_df["Resilience_Category"] = processed_df["Climate_Resilience_Score"].apply(categorize_resilience_score)
    
    return processed_df