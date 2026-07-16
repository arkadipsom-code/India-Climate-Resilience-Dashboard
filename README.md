# India's Climate Resilience & Strategic Capital Allocation Platform

An empirical analytical dashboard for quantifying long-range urban climate risk and optimizing infrastructure fund allocation across major Indian metropolitan areas. The platform simulates predictive climate trends out to the year 2040 using machine learning regressions and dynamically adjusts budget recommendations based on localized risk priorities.

👉 **Live Production URL:** [https://india-climate-resilience-dashboard.streamlit.app/](https://india-climate-resilience-dashboard.streamlit.app/)

---

## 🚀 Key System Capabilities

* **Multi-Vector Risk Indexes:** Quantifies and maps Heatwave Risk, Flood Risk, Water Stress, Population Pressure, and Infrastructure Readiness scores out of 100.
* **Predictive Simulation Engines:** Employs Ordinary Least Squares (OLS) Linear Regression models to forecast urban temperature drift and extreme weather event frequencies up to the year 2040.
* **Algorithmic Capital Optimization:** Automatically routes user-defined adaptation fund pools (up to ₹20,000 Crores) directly to highest-priority vulnerabilities using a custom prioritization matrix.
* **Native Interactive UI:** Streamlined, highly intuitive layout complete with dynamic status alerts, custom interactive visual distribution plots, and granular asset configuration dataframes.

---

## 🧮 Methodological Framework & Core Formulations

All raw parameters undergo high-fidelity **Min-Max Standardization (0 to 100 scaling)** dynamically before calculating aggregate index values.

### 1. Unified Climate Resilience Score
The absolute score is determined by balancing four threat sub-indexes alongside one infrastructure defense vector:

$$\text{Resilience Score} = 0.25 \times (100 - \text{Heatwave Risk}) + 0.25 \times (100 - \text{Flood Risk}) + 0.20 \times (100 - \text{Water Stress}) + 0.15 \times (100 - \text{Population Pressure}) + 0.15 \times \text{Infrastructure Readiness}$$

### 2. Operational Vulnerability Tier Thresholds
* **🟢 High Resilience:** $\ge 80$ | Solid defensive urban infrastructure metrics.
* **🟡 Moderate Resilience:** $60 \text{ to } 79.9$ | Balanced metrics with distinct localized vulnerability vectors.
* **🟠 Vulnerable Status:** $40 \text{ to } 59.9$ | Significant active risk exposures. Target capital injection required.
* **🔴 Critical Alert:** $< 40$ | Severe structural deficiencies. Immediate crisis mitigation infrastructure required.

### 3. Threat Matrix Equations
* **Heatwave Risk Index:** $(0.4 \times \text{Summer Temp}) + (0.4 \times \text{Heatwave Days}) + (0.2 \times \text{Population Density})$
* **Flood Risk Index:** $(0.3 \times \text{Annual Rainfall}) + (0.5 \times \text{Extreme Rainfall Days}) + (0.2 \times \text{Inverted Road Density})$
* **Water Stress Index:** $(0.5 \times \text{Groundwater Depletion}) + (0.5 \times \text{Water Demand-Supply Ratio})$
* **Population Pressure Index:** $(0.5 \times \text{Population Density}) + (0.5 \times \text{Population Growth Rate})$
* **Infrastructure Readiness Index:** $(0.4 \times \text{Sewage Coverage}) + (0.3 \times \text{Green Cover}) + (0.3 \times \text{Public Transport})$

---

## 🛠️ Repository File Architecture

```text
├── .gitignore                     # Git tracking exclusions configuration
├── README.md                      # Comprehensive application documentation
├── app.py                         # Primary execution file and core UI assembly
├── requirements.txt               # Declared system dependencies
├── data/
│   └── city_data.csv              # Base historical data matrix for Indian cities
└── modules/
    ├── risk_engine.py             # Math pipeline for index and tier processing
    ├── investment_engine.py       # Portfolio optimization engine
    └── forecast_engine.py         # OLS machine learning prediction models
