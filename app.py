import streamlit as st
import pandas as pd

# Import modules
from data_processing.preprocessing import load_user_data, clean_data
from data_processing.feature_engineering import create_features
from inference.predict_tilt import predict_tilt
from inference.interpret_results import interpret_tilt
from visualization.plots import plot_height_series

st.title("Underground Storage Tank Tilt Detection System")

st.write("Upload tank height measurements to determine whether the tank is tilted.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    # Load data
    df = load_user_data(uploaded_file)

    # Clean data
    df = clean_data(df)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Plot height trend
    st.subheader("Height Trend")
    plot_height_series(df)

    # Feature engineering
    features = create_features(df)

    # Predict tilt
    k = predict_tilt(features)

    # Interpret result
    status, severity = interpret_tilt(k)

    st.subheader("Tilt Detection Result")

    st.write("Estimated Tilt Factor:", float(k))
    st.write("Tank Status:", status)
    st.write("Severity Level:", severity)