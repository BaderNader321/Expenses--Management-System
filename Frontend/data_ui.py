import streamlit as st
from datetime import datetime
import pandas as pd
import requests

API_URL = "http://localhost:8000"
def get_data_tab():
    response = requests.get(f"{API_URL}/expenses/")
    data_json = response.json()

    data = {
        "Id": [row['id'] for row in data_json],
        "Date": [row['expense_date'] for row in data_json],
        "Amount": [row['amount'] for row in data_json],
        "Category": [row['category'] for row in data_json],
        "Notes": [row['notes'] for row in data_json]
    }
    df = pd.DataFrame(data)
    df = df.set_index('Id')

    st.table(df)