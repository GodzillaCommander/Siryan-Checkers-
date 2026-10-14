import streamlit as st
import pandas as pd

# 1. Force the background to clear out Streamlit's dark theme
st.markdown(
    """
    <style>
    /* This overrides the default black background */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: rgba(0,0,0,0) !important;
        background: none !important;
    }
    
    /* This places the animated loop completely behind your site */
    body {
        background-image: url('https://giphy.com') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }

    /* Make the text and sliders stand out clearly so you can read them */
    h1, h3, p, label, .stSlider {
        background-color: rgba(15, 15, 15, 0.75);
        padding: 12px;
        border-radius: 8px;
        color: #ffffff !important;
    }
    div[data-testid="stWidgetLabel"] p {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Your Webpage Content
st.title("🏙️ Damascus Population Calculator")
st.write("Adjust the parameters below to project the exponential population growth sequence.")

# Interactive Controls
rate = st.slider("Annual Growth Rate (%)", 0.0, 10.0, 4.36) / 100
years = st.slider("Number of Years to Predict", 5, 30, 20)

# Mathematical Logic
p0 = 2922000
population_list = []
current_pop = p0

for year in range(0, years + 1):
    population_list.append({"Year": year, "Population": int(current_pop)})
    current_pop = current_pop * (1 + rate)

df = pd.DataFrame(population_list)
final_population = df.iloc[-1]["Population"]

st.subheader(f"Projected Population: {final_population:,}")
st.line_chart(df.set_index("Year"))
