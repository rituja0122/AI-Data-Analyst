"""
chart_generator.py
Builds Plotly figures from the DataFrame + profile dict.
Every function returns a plotly figure object — app.py just calls st.plotly_chart() on it.
"""

import plotly.express as px
import pandas as pd


def missing_values_chart(missing_df: pd.DataFrame):
    if missing_df.empty:
        return None
    fig = px.bar(
        missing_df.reset_index(),
        x="index", y="missing_pct",
        title="Missing Values by Column (%)",
        labels={"index": "Column", "missing_pct": "% Missing"}
    )
    return fig


def numeric_distribution_chart(df: pd.DataFrame, column: str):
    fig = px.histogram(df, x=column, title=f"Distribution: {column}", nbins=30)
    return fig


def correlation_heatmap(corr_df: pd.DataFrame):
    if corr_df.empty:
        return None
    fig = px.imshow(
        corr_df, text_auto=True, aspect="auto",
        title="Correlation Heatmap", color_continuous_scale="RdBu_r"
    )
    return fig


def categorical_bar_chart(df: pd.DataFrame, column: str, top_n: int = 10):
    counts = df[column].value_counts().head(top_n).reset_index()
    counts.columns = [column, "count"]
    fig = px.bar(counts, x=column, y="count", title=f"Top {top_n} values: {column}")
    return fig


def scatter_chart(df: pd.DataFrame, x_col: str, y_col: str):
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}", trendline="ols")
    return fig