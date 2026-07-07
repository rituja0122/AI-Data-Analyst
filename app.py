"""
app.py
Main coordinator. No stats logic and no LLM calls live here directly —
it just wires uploads -> eda_engine -> chart_generator -> report_writer -> UI.
"""

import streamlit as st
from dotenv import load_dotenv

from analytics.eda_engine import load_file, build_full_profile
from analytics import chart_generator as charts
from utils.report_writer import generate_report

load_dotenv()

st.set_page_config(page_title="AI Data Analyst", layout="wide")
st.title("📊 AI Data Analyst")
st.caption("Upload a CSV or Excel file to get automated EDA + an AI-written executive summary.")

uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])

if uploaded_file:
    df = load_file(uploaded_file)
    st.subheader("Preview")
    st.dataframe(df.head(20))

    profile = build_full_profile(df)

    st.subheader("Dataset Overview")
    st.write(f"**Rows:** {profile['shape'][0]}  |  **Columns:** {profile['shape'][1]}")
    st.write("**Column types:**", profile["column_types"])

    # --- Missing values ---
    if not profile["missing_summary"].empty:
        st.subheader("Missing Values")
        st.dataframe(profile["missing_summary"])
        fig = charts.missing_values_chart(profile["missing_summary"])
        if fig:
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.success("No missing values detected.")

    # --- Numeric summary + distribution ---
    if not profile["numeric_summary"].empty:
        st.subheader("Numeric Summary")
        st.dataframe(profile["numeric_summary"])

        numeric_cols = profile["numeric_summary"].index.tolist()
        selected_col = st.selectbox("Pick a numeric column to view distribution", numeric_cols)
        st.plotly_chart(charts.numeric_distribution_chart(df, selected_col), use_container_width=True)

    # --- Correlation heatmap ---
    if not profile["correlation_matrix"].empty:
        st.subheader("Correlation Heatmap")
        st.plotly_chart(charts.correlation_heatmap(profile["correlation_matrix"]), use_container_width=True)

    # --- Categorical breakdown ---
    if profile["categorical_summary"]:
        st.subheader("Categorical Breakdown")
        cat_col = st.selectbox("Pick a categorical column", list(profile["categorical_summary"].keys()))
        st.plotly_chart(charts.categorical_bar_chart(df, cat_col), use_container_width=True)

    # --- AI-generated executive summary ---
    st.subheader("🧠 AI Executive Summary")
    if st.button("Generate Report"):
        with st.spinner("Analyzing data and writing summary..."):
            report = generate_report(profile)
        st.markdown(report)
else:
    st.info("Upload a file to get started.")