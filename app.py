import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Importing engines
from modules.risk_engine import calculate_indices
from modules.investment_engine import recommend_investment
from modules.forecast_engine import forecast_city_trends


st.set_page_config(
    page_title="India Climate Resilience Dashboard", 
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("Climate Resilience & Strategic Capital Allocation Platform")
st.caption("An empirical analytical framework for urban risk quantification and long-range infrastructure deployment optimization.")
st.divider()


@st.cache_data
def load_base_data():
    return pd.read_csv("data/city_data.csv")

raw_df = load_base_data()


st.sidebar.markdown("### Simulation Parameters")
target_year = st.sidebar.slider("Simulation Horizon (Year)", 2026, 2040, 2026, step=1)
budget = st.sidebar.slider("Adaptation Fund Pool (₹ Crores)", 100, 20000, 1000, step=50)
available_cities = sorted(raw_df["City"].unique())
selected_city = st.sidebar.selectbox("Target Metropolitan Area", available_cities)


if target_year > 2026:
    working_df = forecast_city_trends(raw_df, target_year)
else:
    working_df = calculate_indices(raw_df)

city_data = working_df[working_df["City"] == selected_city].iloc[0]


color_palette = {
    "Urban Cooling & Green Canopies": "#FB7185",       
    "Stormwater Drainage Infrastructure": "#38BDF8",   
    "Water Security & Grid Management": "#6EE7B7",      
    "Public Transit & Decentralization": "#FBBF24",    
    "Wastewater & Sewage Treatment Expansion": "#A78BFA" 
}


col1, col2 = st.columns(2, gap="large")

# --- VULNERABILITY ARCHITECTURE ---
with col1:
    st.subheader(f"{selected_city} Vulnerability Index ({target_year})")
    
    
    with st.container(border=True):
        kpi_sub1, kpi_sub2 = st.columns(2)
        with kpi_sub1:
            st.metric(
                label="Resilience Score", 
                value=f"{city_data['Climate_Resilience_Score']:.2f}",
                help="A consolidated rating from 0 (Critical) to 100 (Optimal) based on infrastructural and climatic vectors."
            )
        with kpi_sub2:
            st.metric(
                label="Vulnerability Status", 
                value=city_data["Resilience_Category"]
            )
            
    
    tier = city_data["Resilience_Category"].lower()
    if "high" in tier or "optimal" in tier:
        st.success(f"**Status Check:** {selected_city} demonstrates solid defensive urban metrics. Capital deployment should prioritize preventative maintenance and long-term optimization projects.")
    elif "moderate" in tier or "medium" in tier:
        st.info(f"**Status Check:** {selected_city} shows balanced resilience with moderate regional vulnerabilities. Capital allocation should focus on bridging systemic infrastructural gaps.")
    else:
        st.warning(f"**Alert:** {selected_city} is flagged under a highly vulnerable rating tier. Immediate capital deployment should target high-risk flood mitigation and thermal stress infrastructures.")

    
    metrics_labels = ["Heatwave Risk", "Flood Risk", "Water Stress", "Population Pressure", "Infrastructure Readiness"]
    metrics_values = [
        city_data["Heatwave_Risk_Index"],
        city_data["Flood_Risk_Index"],
        city_data["Water_Stress_Index"],
        city_data["Population_Pressure_Index"],
        city_data["Infrastructure_Readiness_Index"]
    ]
    chart_df = pd.DataFrame({"Metric": metrics_labels, "Index Rating": metrics_values})
    
    
    fig_bar = px.bar(
        chart_df, x="Metric", y="Index Rating", 
        range_y=[0, 100], text=chart_df["Index Rating"].apply(lambda x: f"{x:.1f}")
    )
    
    fig_bar.update_traces(
        marker_color="#334155", 
        marker_line=dict(width=1.5, color="#38BDF8"),
        textposition="outside"
    )
    
    fig_bar.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=30, b=10, l=0, r=0),
        xaxis=dict(title="", showgrid=False),
        yaxis=dict(title="Scale Configuration (0-100)", showgrid=True, gridcolor="#1E293B")
    )
    
    with st.container(border=True):
        st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})


# --- OPTIMIZED CAPITAL ALLOCATION ---
with col2:
    st.subheader(f"Optimized Capital Allocation Strategy")
    
    
    allocation_df = recommend_investment(city_data, budget)
    chart_colors = [color_palette.get(x, "#64748B") for x in allocation_df["Sector Framework"]]
    
    
    fig_donut = go.Figure(data=[go.Pie(
        labels=allocation_df["Sector Framework"],
        values=allocation_df["Recommended Investment (₹ Crores)"],
        hole=0.6,
        marker=dict(colors=chart_colors, line=dict(color='#0F172A', width=2)),
        textinfo="percent",
        hoverinfo="label+value"
    )])
    
    fig_donut.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=10, b=10, l=0, r=0),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        )
    )
    
    
    with st.container(border=True):
        st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
    
    
    display_df = allocation_df.copy()
    display_df = display_df.rename(columns={
        "Recommended Investment (₹ Crores)": "Allocation (₹ Cr)",
        "Allocation Percentage (%)": "Share (%)"
    })
    
    display_df = display_df[["Sector Framework", "Allocation (₹ Cr)", "Share (%)"]]
    
    
    st.write("##### Allocation Details & Portfolio Breakdown")
    st.dataframe(
        display_df,
        column_config={
            "Sector Framework": st.column_config.TextColumn("Sector / Framework"),
            "Allocation (₹ Cr)": st.column_config.ProgressColumn(
                "Allocation (₹ Cr)",
                help="Recommended capital deployment in ₹ Crores.",
                format="₹%d Cr",
                min_value=0,
                max_value=int(budget)
            ),
            "Share (%)": st.column_config.NumberColumn(
                "Share (%)",
                help="Percentage of the overall budget allocation.",
                format="%.1f%%"
            )
        },
        hide_index=True,
        use_container_width=True
    )


st.divider()
st.markdown("### Methodology & Analytical Framework")
st.caption("Detailed breakdown of index calculation formulas, weights, and categorical tier parameters utilized in this simulation.")

    
tab1, tab2, tab3 = st.tabs(["Score Tier Parameters", "Sub-Index Formulas", "Simulation Forecast Logic"])

with tab1:
    st.write("The **Climate Resilience Score** is categorized into four distinct performance bands based on absolute scaled scores:")
        
        
    tier_data = {
            "Resilience Category": ["🟢 High", "🟡 Moderate", "🟠 Vulnerable", "🔴 Critical"],
            "Score Threshold": ["≥ 80", "60 to 79.9", "40 to 59.9", "< 40"],
            "Strategic Assessment": [
                "Solid defensive urban infrastructure metrics. Focus on preventative optimization.",
                "Balanced framework with moderate systemic gaps. Target localized interventions.",
                "Significant risk vectors present. Requires active capital deployment.",
                "Severe structural vulnerability. Immediate emergency infrastructure adaptation required."
            ]
        }
    st.table(pd.DataFrame(tier_data))

with tab2:
    st.write("All raw indicators are standardized dynamically using a global **Min-Max Scaler (0-100)** before calculation. The indicators are combined via the following structural equations:")
        
        
    st.markdown("""
        * **Consolidated Climate Resilience Score:**
          $$\\text{Resilience Score} = 0.25 \\times (100 - \\text{Heatwave Risk}) + 0.25 \\times (100 - \\text{Flood Risk}) + 0.20 \\times (100 - \\text{Water Stress}) + 0.15 \\times (100 - \\text{Population Pressure}) + 0.15 \\times \\text{Infrastructure Readiness}$$
        
        ---
        
        * **Heatwave Risk Index:**
          $$\\text{Heatwave Risk} = (\\text{Summer Temp} \\times 0.4) + (\\text{Heatwave Days} \\times 0.4) + (\\text{Population Density} \\times 0.2)$$
          
        * **Flood Risk Index:**
          $$\\text{Flood Risk} = (\\text{Annual Rainfall} \\times 0.3) + (\\text{Extreme Rainfall Days} \\times 0.5) + (\\text{Inverted Road Density} \\times 0.2)$$
          
        * **Water Stress Index:**
          $$\\text{Water Stress} = (\\text{Groundwater Depletion} \\times 0.5) + (\\text{Water Demand-Supply Ratio} \\times 0.5)$$
          
        * **Population Pressure Index:**
          $$\\text{Population Pressure} = (\\text{Population Density} \\times 0.5) + (\\text{Population Growth Rate} \\times 0.5)$$
          
        * **Infrastructure Readiness Index:**
          $$\\text{Infrastructure Readiness} = (\\text{Sewage Coverage} \\times 0.4) + (\\text{Green Cover} \\times 0.3) + (\\text{Public Transport} \\times 0.3)$$
        """)

with tab3:
    st.write("When the simulation window scales beyond **2026**, the platform activates an empirical predictive layer:")
    st.markdown("""
        1. **Demographic Expansion**: Future population scales exponentially based on compound growth mechanics: 
           $$\\text{Population}_{\\text{future}} = \\text{Population}_{\\text{current}} \\times (1 + \\text{Growth Rate})^{\\Delta \\text{Years}}$$
        2. **Climate Metrics**: Target values for variables like *Average Summer Temperature* and *Heatwave Days* are generated using ordinary least squares (OLS) **Linear Regression** trends derived across historical decadal baselines.
        3. **Water Stress Drift**: The baseline *Water Demand-Supply Ratio* scales dynamically, moving up in parallel with proportional population expansion vectors.
        """)
