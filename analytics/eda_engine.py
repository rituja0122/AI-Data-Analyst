"""
eda_engine.py
Pure Pandas logic — no LLM here. Computes dataset profile:
column types, missing values, basic stats, correlations.
"""

import pandas as pd
import numpy as np


def load_file(uploaded_file):
    """Reads a CSV or Excel file into a DataFrame."""
    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file)


def get_column_types(df: pd.DataFrame) -> dict:
    """Classifies each column as numeric, categorical, or datetime."""
    types = {}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            types[col] = "numeric"
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            types[col] = "datetime"
        else:
            types[col] = "categorical"
    return types


def get_missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Returns count + percentage of missing values per column."""
    missing_count = df.isnull().sum()
    missing_pct = (missing_count / len(df) * 100).round(2)
    summary = pd.DataFrame({
        "missing_count": missing_count,
        "missing_pct": missing_pct
    })
    return summary[summary["missing_count"] > 0].sort_values("missing_count", ascending=False)


def get_numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Basic descriptive stats for numeric columns: mean, median, std, min, max."""
    numeric_df = df.select_dtypes(include=np.number)
    if numeric_df.empty:
        return pd.DataFrame()
    return numeric_df.describe().T.round(2)


def get_categorical_summary(df: pd.DataFrame, top_n: int = 5) -> dict:
    """Top N value counts for each categorical column."""
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    summary = {}
    for col in cat_cols:
        summary[col] = df[col].value_counts().head(top_n).to_dict()
    return summary


def get_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Correlation matrix for numeric columns only."""
    numeric_df = df.select_dtypes(include=np.number)
    if numeric_df.shape[1] < 2:
        return pd.DataFrame()
    return numeric_df.corr().round(2)


def build_full_profile(df: pd.DataFrame) -> dict:
    """Bundles everything into one dict — this is what gets passed to
    the report writer / chart generator downstream."""
    return {
        "shape": df.shape,
        "column_types": get_column_types(df),
        "missing_summary": get_missing_summary(df),
        "numeric_summary": get_numeric_summary(df),
        "categorical_summary": get_categorical_summary(df),
        "correlation_matrix": get_correlation_matrix(df),
    }