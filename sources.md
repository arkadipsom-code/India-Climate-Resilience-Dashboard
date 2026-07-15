# Data Sources & Analytical Methodology

This project utilizes a **Hybrid Fact-Base Model** to evaluate urban climate vulnerability and optimize infrastructure investments across 20 major Indian metropolitan areas. 

### Core Index Mappings & Policy Citations:

1. **Urban Flooding Exposure (`Annual_Rainfall`, `Extreme_Rainfall_Days`)**
   * **Source:** India Meteorological Department (IMD) historical gridded climate averages. 
   * **Policy Link:** High-risk baselines match the target funding zones prioritized under the **15th Finance Commission of India (National Disaster Mitigation Fund)**, which allocated ₹2,500 Crore explicitly for urban flood mitigation in high-risk metros (Mumbai, Chennai, Kolkata, Bengaluru, Hyderabad, Ahmedabad, Pune).

2. **Water Resource Deficits (`Groundwater_Depletion`, `Water_Demand_Supply_Ratio`)**
   * **Source:** NITI Aayog's **Composite Water Management Index (CWMI)**.
   * **Policy Link:** Anchored against the critical urban groundwater drawdown warnings (measured in meters below ground level) flagged across major core economic hubs including Delhi, Bengaluru, Hyderabad, and Chennai.

3. **Thermal Shocks & Heatwaves (`Average_Summer_Temperature`, `Heatwave_Days`)**
   * **Source:** National Disaster Management Authority (NDMA) Heat Action Plans and IMD severe weather records.
   * **Policy Link:** Tracks core trends in internal grid stresses, heavily weighted towards northern and inland locations experiencing sustained days above 40°C.

4. **Demographic Risk Modifiers (`Population`, `Population_Density`, `Population_Growth_Rate`)**
   * **Source:** Census of India & Ministry of Housing and Urban Affairs (MoHUA) urban profiles.
   * **Policy Link:** Used as proxy metrics for the **Urban Heat Island (UHI)** effect and resource consumption runaways during long-term public policy forecasting (2030–2040).

5. **Adaptive Resilience Capacity (`Sewage_Treatment_Coverage`, `Green_Cover_Percentage`, `Public_Transport_Score`)**
   * **Source:** MoHUA Smart Cities Mission Indicators and Central Pollution Control Board (CPCB) urban waste inventories.