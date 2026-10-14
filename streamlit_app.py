import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Damascus Population Model", layout="centered")

st.title("📈 Damascus Population Growth Sequence Model")
st.write("An interactive mathematical simulation modeling pure exponential population growth over time.")

# Sidebar parameters for math sequence variables
st.sidebar.header("🔢 Sequence Variables")
p0 = st.sidebar.number_input("Initial Population (P₀)", min_value=100000, max_value=10000000, value=2922000, step=50000)
growth_rate = st.sidebar.slider("Annual Growth Rate (r %)", min_value=0.0, max_value=10.0, value=4.36, step=0.1) / 100
years = st.sidebar.slider("Timeline (Years)", min_value=5, max_value=50, value=20)

# Computing the mathematical sequence: P_n = P_0 * (1 + r)^n
population_sequence = []
current_pop = p0

for year in range(0, years + 1):
    population_sequence.append({
        "Year": year,
        "Projected Population": int(current_pop)
    })
    # Apply geometric compounding multiplier
    current_pop *= (1 + growth_rate)

# Convert into a structured table format
df = pd.DataFrame(population_sequence)

# Render live key metrics and chart
final_pop = df.iloc[-1]["Projected Population"]
st.metric(label=f"Projected Population at Year {years}", value=f"{final_pop:,}")

st.subheader("Exponential Growth Curve")
st.line_chart(df.set_index("Year")["Projected Population"])

# Show raw mathematical output table
if st.checkbox("Show Raw Sequence Table"):
    st.dataframe(df.set_index("Year"))
