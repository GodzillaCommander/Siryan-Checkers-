import streamlit as st
import pandas as pd

st.title("Damascus Population Calculator")
st.write("Move the sliders to see how fast the population grows.")

# 1. Interactive Sliders
rate = st.slider("Annual Growth Rate (%)", 0.0, 10.0, 4.36) / 100
years = st.slider("Number of Years to Predict", 5, 30, 20)

# 2. Starting Data
p0 = 2922000
population_list = []
current_pop = p0

# 3. Calculate Growth Loop
for year in range(0, years + 1):
    population_list.append({"Year": year, "Population": int(current_pop)})
    current_pop = current_pop * (1 + rate)

# 4. Display Chart and Total
df = pd.DataFrame(population_list)
final_population = df.iloc[-1]["Population"]

st.subheader(f"Projected Population: {final_population:,}")
st.line_chart(df.set_index("Year"))


import streamlit as st
import pandas as pd

# 1. Inject the Polyester Spider-Man background via HTML/CSS
# This uses a public, loopable background link that fills the screen behind the content
st.markdown(
    """
    <style>
    /* target the main container to make it see-through */
    .stApp {
        background: transparent;
    }
    
    /* insert a fixed background video behind everything */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1;
        background-image: url('https://giphy.com'); /* A placeholder classic spidey loop */
        background-size: cover;
        background-position: center;
        opacity: 0.25; /* Blends it into the background so you can still read text */
    }

    /* Make the text boxes and sliders easy to read over the video background */
    .stSlider, h1, h3, p {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 10px;
        border-radius: 8px;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Your Interactive Webpage Content
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
