# AI Data Analyst 
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
<img width="1811" height="735" alt="image" src="https://github.com/user-attachments/assets/e47ad0f1-e529-4992-a6d3-022c270166e2" />
<img width="1797" height="670" alt="image" src="https://github.com/user-attachments/assets/38291a44-2c54-455e-aa09-ffb447fac699" />
<img width="1775" height="735" alt="image" src="https://github.com/user-attachments/assets/ccd907f1-a598-4c26-9b73-bd08f0548f96" />

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

## Dataset Used
This project was tested using the **IBM HR Analytics Employee Attrition & Performance** dataset from Kaggle, which contains employee-level data including department, job level, tenure, salary, performance ratings, and attrition status.

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

## Author
Built by Rituja kine as part of a hands-on Data Analytics portfolio, focused on Python, SQL, and dashboarding skills.
