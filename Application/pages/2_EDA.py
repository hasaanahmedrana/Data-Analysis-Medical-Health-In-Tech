import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
    page_title="Mental Health in Tech - EDA App",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)
df = pd.read_csv(r"C:\Users\PMLS\Desktop\SEM-5\Mental Health in Tech\data.csv")
report = ProfileReport(df, title="Results", explorative=True)
st_profile_report(report)

