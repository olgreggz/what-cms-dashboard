"""The App."""
import joblib
import pandas as pd
import streamlit as st
from resc.resc import make_sankey  # pylint: disable=import-error

df = pd.read_csv("data/plot_data.csv")
labels = joblib.load("data/labels.joblib")

sankey_fig = make_sankey(df, labels)

st.title("What CMS Competitor Intel")
st.plotly_chart(sankey_fig)
