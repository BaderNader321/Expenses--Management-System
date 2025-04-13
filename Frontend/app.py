from add_or_update_ui import add_update_tab
from analytics_category_ui import analytics_tab
from analytics_month_ui import monthly_analytics_tab
from data_ui import get_data_tab
import streamlit as st

st.set_page_config(layout="wide")

st.title("Expense Management System")

tab1, tab2, tab3, tab4 = st.tabs([
    "Add/Update", "Analytics By Category", "Analytics By Month", "Expense Data"
])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    monthly_analytics_tab()

with tab4:
    get_data_tab()
