import numpy as np
import pandas as pd

def recommend_investment(city_row, total_budget_crores):

    heat_risk = city_row['Heatwave_Risk_Index']
    flood_risk = city_row['Flood_Risk_Index']
    water_stress = city_row['Water_Stress_Index']
    population_pressure = city_row['Population_Pressure_Index']
    infrastructure_gap = 100 - city_row['Infrastructure_Readiness_Index']

    weights = {
        "Urban Cooling & Green Canopies": heat_risk * 0.25,
        "Stormwater Drainage Infrastructure": flood_risk * 0.30,
        "Water Security & Grid Management": water_stress * 0.25,
        "Public Transit & Decentralization": population_pressure * 0.10,
        "Wastewater & Sewage Treatment Expansion": infrastructure_gap * 0.10
    }

    total_weight = sum(weights.values())

    allocation_data = []
    for sector, weight in weights.items():
        percentage = (weight / total_weight) if total_weight > 0 else 0.20
        allocated_amount = percentage * total_budget_crores
        
        allocation_data.append({
            "Sector Framework": sector,
            "Allocation Percentage (%)": round(percentage * 100, 2),
            "Recommended Investment (₹ Crores)": round(allocated_amount, 2)
        })
        
    return pd.DataFrame(allocation_data)
    