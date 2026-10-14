import streamlit as st
import pandas as pd

# 1. Page Configuration (Must be the very first Streamlit command)
st.set_page_config(page_title="Damascus Population Calculator", layout="centered")

# 2. Strict CSS Injection to force the Spider-Man background through Streamlit's core theme
st.markdown(
    """
    <style>
    /* Completely strip away Streamlit's default dark/light solid backgrounds */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: transparent !important;
        background: none !important;
    }
    
    /* Apply the animated background directly to the base window HTML container */
    html, body {
        background-image: url('https://giphy.com') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        background-repeat: no-repeat !important;
    }

    /* Wrap text blocks and inputs in a dark frosted-glass box for readability */
    h1, h3, p, label, .stSlider {
        background-color: rgba(15, 15, 15, 0.85);
        padding: 12px;
        border-radius: 8px;
        color: #ffffff !important;
    }
    
    /* Force inner widget label text to stay white */
    div[data-testid="stWidgetLabel"] p {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Interactive Webpage Interface
st.title("Damascus Population Calculator")
st.write("Adjust the parameters below to project the exponential population growth sequence.")

# Control Sliders
rate = st.slider("Annual Growth Rate (%)", 0.0, 10.0, 4.36) / 100
years = st.slider("Number of Years to Predict", 5, 30, 20)

# 4. Mathematical Modeling Sequence Logic
p0 = 2922000
population_list = []
current_pop = p0

for year in range(0, years + 1):
    population_list.append({"Year": year, "Population": int(current_pop)})
    current_pop = current_pop * (1 + rate)

# Build Data Pipeline
df = pd.DataFrame(population_list)
final_population = df.iloc[-1]["Population"]

# 5. Output Render
st.subheader(f"Projected Population: {final_population:,}")
st.line_chart(df.set_index("Year"))
