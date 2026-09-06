import streamlit as st

page_df = st.Page("page_dataFrame.py", title="Data Frame & Table", icon="🎈")
page_lc = st.Page("page_lineChart.py", title="Line Chart", icon="❄️")
page_mp = st.Page("page_map.py", title="Map", icon="🎉")

pg = st.navigation([page_df, page_lc, page_mp])

pg.run()