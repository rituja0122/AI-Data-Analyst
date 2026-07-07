"""
prompts.py
Keeps LLM instructions separate from logic, so you can tweak tone/structure
without touching report_writer.py.
"""

SYSTEM_PROMPT = """You are a senior data analyst writing an executive summary.
You will be given statistical metadata about a dataset (shape, missing values,
numeric summaries, categorical top values, correlations).

Rules:
- Do NOT invent numbers that aren't in the provided data.
- Write in plain business language, no jargon.
- Structure your answer in three sections: Key Observations, Data Quality Notes,
  and Suggested Next Steps.
- Keep it under 250 words.
"""


def build_user_prompt(profile: dict) -> str:
    """Formats the profile dict into a readable text block for the LLM."""
    lines = []
    lines.append(f"Dataset shape: {profile['shape'][0]} rows, {profile['shape'][1]} columns")

    if not profile["missing_summary"].empty:
        lines.append("\nMissing values:")
        lines.append(profile["missing_summary"].to_string())

    if not profile["numeric_summary"].empty:
        lines.append("\nNumeric summary:")
        lines.append(profile["numeric_summary"].to_string())

    if profile["categorical_summary"]:
        lines.append("\nTop categorical values:")
        for col, vals in profile["categorical_summary"].items():
            lines.append(f"{col}: {vals}")

    if not profile["correlation_matrix"].empty:
        lines.append("\nCorrelation matrix:")
        lines.append(profile["correlation_matrix"].to_string())

    return "\n".join(lines)