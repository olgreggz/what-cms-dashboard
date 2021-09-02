"""The App."""
import joblib
import pandas as pd
import streamlit as st
from resc.resc import make_sankey, make_market_share_bar  # pylint: disable=import-error

sankey_df = pd.read_csv("data/plot_data_sankey.csv")
sankey_labels = joblib.load("data/labels_sankey.joblib")

count_sankey_fig = make_sankey(sankey_df, sankey_labels, mode="count")
revenue_sankey_fig = make_sankey(sankey_df, sankey_labels, mode="revenue")

indy_df = pd.read_csv("data/indy_data.csv")
indy_fig = make_market_share_bar(indy_df, mode="indy")

public_df = pd.read_csv("data/public_data.csv")
public_fig = make_market_share_bar(public_df, mode="public")


st.title("Customer Acquisition and Loss")
st.plotly_chart(count_sankey_fig)
st.plotly_chart(revenue_sankey_fig)
st.title("Market Share Analysis")
st.plotly_chart(indy_fig)
st.plotly_chart(public_fig)
