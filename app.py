# Import Streamlit
import streamlit as st

# Import pandas
import pandas as pd

# Import joblib
import joblib


# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(

    # Browser tab title
    page_title="Forest Cover Prediction",

    # Forest emoji icon
    page_icon="🌲",

    # Wide layout
    layout="wide"
)


# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

# Load trained model
model = joblib.load("forest_cover_model.pkl")

# Load label encoder
label_encoder = joblib.load("label_encoder.pkl")


# ---------------------------------------------------
# CUSTOM CSS STYLING
# ---------------------------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #f4f9f4;
}

/* Title styling */
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #1b4332;
    text-align: center;
}

/* Subtitle styling */
.sub-title {
    font-size: 18px;
    color: #2d6a4f;
    text-align: center;
    margin-bottom: 30px;
}

/* Prediction box */
.prediction-box {
    background-color: #d8f3dc;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 28px;
    color: #081c15;
    font-weight: bold;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #d8f3dc;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# APP TITLE
# ---------------------------------------------------

st.markdown(
    '<p class="main-title">🌲 Forest Cover Type Prediction</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Machine Learning App using Random Forest Classifier</p>',
    unsafe_allow_html=True
)


# ---------------------------------------------------
# SIDEBAR INPUTS
# ---------------------------------------------------

st.sidebar.header("🌿 Enter Forest Features")


# Elevation
Elevation = st.sidebar.number_input(
    "Elevation",
    value=2800
)

# Aspect
Aspect = st.sidebar.number_input(
    "Aspect",
    value=45
)

# Slope
Slope = st.sidebar.number_input(
    "Slope",
    value=15
)

# Horizontal Distance To Hydrology
Horizontal_Distance_To_Hydrology = st.sidebar.number_input(
    "Horizontal Distance To Hydrology",
    value=120
)

# Vertical Distance To Hydrology
Vertical_Distance_To_Hydrology = st.sidebar.number_input(
    "Vertical Distance To Hydrology",
    value=30
)

# Horizontal Distance To Roadways
Horizontal_Distance_To_Roadways = st.sidebar.number_input(
    "Horizontal Distance To Roadways",
    value=1500
)

# Hillshade 9am
Hillshade_9am = st.sidebar.number_input(
    "Hillshade 9am",
    value=220
)

# Hillshade Noon
Hillshade_Noon = st.sidebar.number_input(
    "Hillshade Noon",
    value=240
)

# Hillshade 3pm
Hillshade_3pm = st.sidebar.number_input(
    "Hillshade 3pm",
    value=180
)

# Horizontal Distance To Fire Points
Horizontal_Distance_To_Fire_Points = st.sidebar.number_input(
    "Horizontal Distance To Fire Points",
    value=1200
)
# ---------------------------------------------------
# DISPLAY METRICS
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Elevation",
    Elevation
)

col2.metric(
    "Slope",
    Slope
)

col3.metric(
    "Aspect",
    Aspect
)


# ---------------------------------------------------
# CREATE INPUT DATAFRAME
# ---------------------------------------------------

input_data = pd.DataFrame({

    "Elevation": [Elevation],
    "Aspect": [Aspect],
    "Slope": [Slope],
    "Horizontal_Distance_To_Hydrology": [Horizontal_Distance_To_Hydrology],
    "Vertical_Distance_To_Hydrology": [Vertical_Distance_To_Hydrology],
    "Horizontal_Distance_To_Roadways": [Horizontal_Distance_To_Roadways],
    "Hillshade_9am": [Hillshade_9am],
    "Hillshade_Noon": [Hillshade_Noon],
    "Hillshade_3pm": [Hillshade_3pm],
    "Horizontal_Distance_To_Fire_Points": [Horizontal_Distance_To_Fire_Points]
})


# ---------------------------------------------------
# PREDICTION BUTTON
# ---------------------------------------------------

st.write("")

predict_button = st.button(
    "🌲 Predict Forest Cover Type"
)


# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------

if predict_button:

    # Predict forest type
    prediction = model.predict(input_data)

    # Decode prediction
    predicted_label = label_encoder.inverse_transform(
        prediction
    )

    # Display prediction
    st.markdown(
        f"""
        <div class="prediction-box">
        🌳 Predicted Forest Type:<br><br>
        {predicted_label[0]}
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.write("")

st.markdown("---")

st.markdown(
    """
    <center>
    Developed using ❤️ with Streamlit & Machine Learning
    </center>
    """,
    unsafe_allow_html=True
)