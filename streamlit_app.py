import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="Damascus Urban Model", layout="wide")

st.title("🏙️ Damascus Urban Growth & Resource Model")
st.write("An interactive mathematical simulation modeling exponential population growth and structural resource demands over a 20-year timeline.")

# Sidebar Configuration for Mathematical Inputs
st.sidebar.header("🔧 Model Parameters")
p0 = st.sidebar.number_input("Initial Population (P₀)", min_value=100000, max_value=10000000, value=2922000, step=50000)
growth_rate = st.sidebar.slider("Annual Growth Rate (r %)", min_value=0.0, max_value=10.0, value=4.36, step=0.1) / 100
years = st.sidebar.slider("Projection Timeline (Years)", min_value=5, max_value=50, value=20)

st.sidebar.markdown("---")
st.sidebar.subheader("🚰 Per-Capita Consumption Defaults")
water_per_capita = st.sidebar.slider("Daily Water (Liters/Person)", 50, 300, 120)
elec_per_capita = st.sidebar.slider("Daily Electricity (kWh/Person)", 2, 20, 6)

# Mathematical Modeling Calculations
data = []
current_pop = p0

for year in range(0, years + 1):
    # Geometric/Exponential Sequence: P_n = P_0 * (1 + r)^n
    daily_water = (current_pop * water_per_capita) / 1_000_000  # Millions of Liters
    daily_elec = (current_pop * elec_per_capita) / 1_000      # Megawatt-hours (MWh)
    
    data.append({
        "Year": year,
        "Population": int(current_pop),
        "Daily Water Demand (Million L)": round(daily_water, 2),
        "Daily Electricity Demand (MWh)": round(daily_elec, 2)
    })
    # Compute next element in sequence
    current_pop *= (1 + growth_rate)

df = pd.DataFrame(data)

# Layout: Display key metrics for final year
final_stats = df.iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("Projected Population (Year {})".format(years), f"{final_stats['Population']:,}")
col2.metric("Final Daily Water Need", f"{final_stats['Daily Water Demand (Million L)']} ML")
col3.metric("Final Daily Electricity Need", f"{final_stats['Daily Electricity Demand (MWh)']} MWh")

# Visual Data Charts
st.subheader("📈 Population Curve (Exponential Projection)")
st.line_chart(df.set_index("Year")["Population"])

st.subheader("⚡ Resource Infrastructure Resource Scaling")
resource_option = st.selectbox("Select Resource to Visualize:", ["Daily Water Demand (Million L)", "Daily Electricity Demand (MWh)"])
st.area_chart(df.set_index("Year")[resource_option])

# Show Raw Data Matrix
if st.checkbox("Show Raw Calculation Sequence Data Table"):
    st.dataframe(df)
