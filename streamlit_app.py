import streamlit as st
import pandas as pd

st.title("Damascus Population Growth")

# 1. Set the starting numbers
p0 = 2922000      # Starting population
rate = 0.0436     # 4.36% growth rate
years = 20        # Timeline

population_list = []
current_pop = p0

# 2. Run the math loop
for year in range(0, years + 1):
    population_list.append({"Year": year, "Population": int(current_pop)})
    current_pop = current_pop * (1 + rate)

# 3. Create the data table and chart
df = pd.DataFrame(population_list)

st.line_chart(df.set_index("Year"))
st.dataframe(df.set_index("Year"))
