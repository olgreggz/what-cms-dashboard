"""The App."""
import joblib
import pandas as pd
import streamlit as st
from resc.resc import make_sankey  # pylint: disable=import-error

df = pd.read_csv("data/plot_data.csv")
labels = joblib.load("data/labels.joblib")

count_sankey_fig = make_sankey(df, labels, mode="count")
revenue_sankey_fig = make_sankey(df, labels, mode="revenue")

st.title("CMS Competitor Intel")
st.plotly_chart(count_sankey_fig)
st.plotly_chart(revenue_sankey_fig)
