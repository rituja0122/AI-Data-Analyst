"""
report_writer.py
Only file that talks to the LLM API. Takes the profile dict, builds the prompt,
returns plain text summary.
Uses Google Gemini (free tier) instead of OpenAI.
"""

import os
import google.generativeai as genai
from utils.prompts import SYSTEM_PROMPT, build_user_prompt


def generate_report(profile: dict) -> str:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    user_prompt = build_user_prompt(profile)

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT,
    )
    response = model.generate_content(user_prompt)
    return response.text