# AI Data Analyst 📊

An automated Exploratory Data Analysis (EDA) tool that turns raw CSV/Excel files into interactive visualizations and AI-generated business insights — in seconds, not hours.

## What This Project Does

Manually exploring a new dataset usually takes a lot of repetitive work: checking for missing values, calculating summary statistics, plotting distributions, and then writing up what it all means in plain English for stakeholders.

This app automates that entire workflow. Upload any CSV or Excel file, and it will:

1. Automatically detect column types (numeric, categorical, datetime)
2. Calculate missing value counts and percentages
3. Generate descriptive statistics (mean, median, std, min, max) for numeric columns
4. Show top values for categorical columns
5. Build a correlation heatmap between numeric fields
6. Create interactive Plotly charts (distributions, bar charts, heatmaps)
7. Use Google's Gemini AI to write a short executive summary — covering key observations, data quality issues, and suggested next steps — based only on the real statistics calculated from your data (no made-up numbers)

## Live Demo

🔗 [Try the live app here](https://ai-data-analyst-bhrvpqsq64dqfjoyyvztuq.streamlit.app)

## Screenshots

*(Add screenshots of the app here — dashboard preview, charts, and generated report)*

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Streamlit** | Web app framework for the interactive dashboard |
| **Pandas** | Data loading, cleaning, and statistical calculations |
| **Plotly** | Interactive charts (histograms, heatmaps, bar charts) |
| **Google Gemini API** | Generates the natural-language executive summary |
| **python-dotenv** | Loads API keys securely from a local `.env` file |

## Project Structure

```
ai-data-analyst/
│
├── app.py                      # Main Streamlit app — connects everything together
├── requirements.txt            # Python packages needed to run the project
├── .env                        # Stores the Gemini API key (not uploaded to GitHub)
├── .gitignore                  # Tells Git to ignore .env and cache files
│
├── analytics/
│   ├── eda_engine.py           # Pure Pandas logic: missing values, stats, correlations
│   └── chart_generator.py      # Builds all Plotly charts
│
└── utils/
    ├── prompts.py               # Instructions given to the Gemini model
    └── report_writer.py         # Calls the Gemini API and returns the summary text
```

This structure keeps things organized: statistical logic, chart-building, and AI-report-writing are each in their own file, rather than one giant script. This makes the code easier to read, test, and extend.

## How It Works (Step by Step)

1. **User uploads a file** through the Streamlit interface.
2. **`eda_engine.py`** reads the file into a Pandas DataFrame and calculates a full statistical profile — column types, missing values, numeric summaries, categorical breakdowns, and a correlation matrix.
3. **`chart_generator.py`** takes that same DataFrame and profile, and builds interactive Plotly visualizations.
4. **`prompts.py`** formats the statistical profile into a clean text block, along with instructions telling the AI model exactly how to write the summary (stick to the facts, keep it under 250 words, structure it into three sections).
5. **`report_writer.py`** sends that formatted text to the Gemini API and returns the AI-written summary.
6. **`app.py`** ties all of this together into a single-page dashboard, so the user just uploads a file and sees everything — data preview, charts, and AI summary — without needing to write a single line of code.

## Dataset Used

This project was tested using the **IBM HR Analytics Employee Attrition & Performance** dataset from Kaggle, which contains employee-level data including department, job level, tenure, salary, performance ratings, and attrition status.

The tool is dataset-agnostic — it will work with any tabular CSV or Excel file, automatically adapting its analysis to whatever columns are present.

## Running This Project Locally

1. Clone this repository:
   ```
   git clone https://github.com/rituja0122/AI-Data-Analyst.git
   cd AI-Data-Analyst
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your free Gemini API key (get one at [aistudio.google.com](https://aistudio.google.com/app/apikey)):
   ```
   GEMINI_API_KEY=your_key_here
   ```

4. Run the app:
   ```
   streamlit run app.py
   ```

5. Open the local URL shown in the terminal (usually `http://localhost:8501`) and upload a CSV or Excel file to get started.

## Key Design Decisions

- **Statistics are calculated with Pandas, not the AI model.** The AI is only used to write the narrative summary — all numbers it references come directly from the data, which avoids hallucinated statistics.
- **Prompts are kept in a separate file** (`prompts.py`) so the tone and structure of the AI-written report can be adjusted without touching any of the app's core logic.
- **Free-tier Gemini API** was used instead of a paid API, making this project fully reproducible by anyone without needing to pay for API credits.

## Future Improvements

- Add support for automatically detecting and flagging outliers
- Let users download the generated report as a PDF
- Add a "compare two time periods" mode for time-series datasets
- Cache uploaded files so users don't need to re-upload after refreshing

## Author

Built by Ritu as part of a hands-on Data Analytics portfolio, focused on Python, SQL, and dashboarding skills.
