import matplotlib.pyplot as plt
import streamlit as st

def plot_height_series(df):

    fig, ax = plt.subplots()

    ax.plot(df["height"])

    ax.set_title("Tank Height Measurements")
    ax.set_xlabel("Measurement Index")
    ax.set_ylabel("Height")

    st.pyplot(fig)