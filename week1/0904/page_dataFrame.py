import streamlit as st
import numpy as np
import pandas as pd

st.markdown("# Data Frame & Table")
st.sidebar.markdown("# 🎈 Data Frame & Table")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        np.random.randn(10, 20),
        columns=('col %d' % i for i in range(20))
    )

dataframe = st.session_state.df

st.dataframe(dataframe)
st.table(dataframe)
