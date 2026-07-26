<!--
  README for: Digital Detox: Intelligent Insights for Digital Well-being
  Ready for direct copy to GitHub
-->
# Digital Detox: Intelligent Insights for Digital Well-being

[![Project Banner Placeholder](assets/banner-placeholder.png)](assets/banner-placeholder.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-orange.svg)]()
[![Status](https://img.shields.io/badge/Status-Complete-green.svg)]()

Digital Detox: Intelligent Insights for Digital Well-being is an interactive data exploration dashboard built with Streamlit that helps users, researchers, and organizations understand digital behavior patterns and make informed decisions to promote healthier digital habits. This project focuses on exploratory data analysis (EDA) and interactive visualizations — no machine learning models are included.

## 🚀 Project Overview

- Title: Digital Detox: Intelligent Insights for Digital Well-being
- Type: Data Science (Exploratory Analysis + Interactive Dashboard)
- Tech Stack: Python, Streamlit, Pandas, NumPy, Matplotlib, Seaborn, Plotly Express
- Dataset: Digital Wellness Dataset (CSV)

## 🎯 Objectives

- Provide an executive summary and data-driven insights into digital wellness.
- Perform data cleaning, missing value analysis, and statistical summaries.
- Explore usage patterns with interactive visualizations.
- Build a Streamlit dashboard for non-technical stakeholders to explore results.

## ✨ Features

- Dataset preview and schema overview
- Missing value analysis and summary statistics
- Interactive univariate and bivariate visualizations
- Time-series analysis of digital device usage
- Correlation heatmaps and cross-tab analysis
- Downloadable cleaned dataset (optional)
- Insights, conclusions, and future scope in a professional report

## 📂 Project Workflow

1. Data ingestion (CSV)
2. Data cleaning & missing value analysis
3. Statistical summaries
4. Exploratory data analysis (EDA)
5. Interactive visualization & dashboarding
6. Insights & conclusions
7. Documentation & packaging

## 🗂 Folder structure

- assets/                → UI assets, banners, icons, logos
- dataset/               → Raw dataset (digital_wellness.csv) and sample data
- images/                → Screenshots for README and dashboard
- notebooks/             → Exploratory notebooks (EDA)
- report/                → Final report, executive summary, insights
- src/                   → Streamlit app and helper modules
- .github/               → Issue/pr templates (optional)
- LICENSE
- README.md
- requirements.txt

## 📁 Files included (templates)

- README.md (this file)
- requirements.txt
- LICENSE (MIT)
- .gitignore
- src/app.py — Streamlit dashboard
- src/utils.py — helper functions
- dataset/digital_wellness_sample.csv — example data
- dataset/README.md — dataset description
- notebooks/EDA.md — notebook plan & structure
- report/Final_Report.md — report skeleton & templates
- COMMIT_MESSAGES.md — suggested commit messages

## 📥 Dataset information

- Expected filename: dataset/digital_wellness.csv
- Sample file included: dataset/digital_wellness_sample.csv
- Typical columns (suggested schema — adapt to your actual dataset):
  - user_id (str/int)
  - date (YYYY-MM-DD)
  - total_screen_time_minutes (float)
  - sessions_count (int)
  - avg_session_length_minutes (float)
  - social_media_minutes (float)
  - productivity_minutes (float)
  - entertainment_minutes (float)
  - device (categorical — Mobile/Tablet/Desktop)
  - sleep_hours (float)
  - mood_score (1-10 scale) — optional
  - focus_minutes (float)

See dataset/README.md for details.

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/digital-detox-analysis.git
   cd digital-detox-analysis
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your real dataset:
   - Place your CSV as `dataset/digital_wellness.csv`. Ensure the header matches the schema or adjust `src/utils.py` accordingly.

## ▶️ How to run locally

From project root:
```bash
streamlit run src/app.py
```
Open the URL printed by Streamlit (usually http://localhost:8501).

## ☁️ Deployment (Streamlit Cloud)

1. Push repository to GitHub.
2. Go to https://streamlit.io/cloud and connect your GitHub account.
3. Click "New app", choose the repository and branch, set the main file to `src/app.py`.
4. Deploy. (If the dataset is large, consider hosting it externally and updating the app to read from a URL or Git LFS.)

## 🖼️ Screenshots

Replace these placeholders with real screenshots in `images/`:

- images/screenshot-dashboard.png
- images/screenshot-eda.png
- images/screenshot-missing-values.png

## 📊 Results & Insights (example placeholders)

- High average daily screen time concentrated in younger age brackets.
- Strong positive correlation between social_media_minutes and total_screen_time.
- Reduced sleep_hours correlate with higher late-night usage (20:00–02:00).
- Productivity apps usage inversely proportional to entertainment_minutes for weekday sessions.

Add your real insights in `report/Final_Report.md`.

## 🔮 Future Scope

- Add segmentation analysis (age, occupation, geography).
- Add time-of-day clustering and session pattern mining.
- Incorporate passive sensing data (notifications, app events).
- Build intervention recommendations and A/B testing dashboards.
- Extend to a web service with user authentication and personalized recommendations.

## 📚 References

- [Streamlit Documentation](https://docs.streamlit.io/)
- Pandas, NumPy, Matplotlib, Seaborn, Plotly Express official docs
- Publications on digital wellbeing and screen time research (list your references here)

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🙋 Author

Karan Toor (Karan-toor5)  
GitHub: https://github.com/Karan-toor5

---

Repository description (one-liner to set on GitHub):
Digital Detox — Interactive Streamlit dashboard for exploratory analysis of digital wellness and screen-time behavior insights.

Suggested GitHub topics/tags:
digital-wellness, data-science, streamlit, eda, data-visualization, python, pandas, plotly, seaborn, matplotlib, exploratory-data-analysis
