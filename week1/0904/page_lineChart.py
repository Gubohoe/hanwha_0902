import streamlit as st
import numpy as np
import pandas as pd

st.markdown("# Line Chart")
st.sidebar.markdown("# ❄️ Line Chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)