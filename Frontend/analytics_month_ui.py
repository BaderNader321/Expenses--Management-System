import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000"

def monthly_analytics_tab():
    response = requests.get(f"{API_URL}/monthly_analytics/")
    data_json = response.json()

    data = {
        "Month": [row['month'] for row in data_json],
        "Total": [row['total'] for row in data_json]
    }
    df = pd.DataFrame(data)
    df = df.set_index('Month')

    st.subheader("Expense Breakdown By Month")

    st.bar_chart(data=df, width=0, height=0, use_container_width=True, y_label="Total Expenses")
    df["Total"] = df["Total"].map("{:.2f}".format)

    st.table(df)