# 📊 Sentiment Analysis Dashboard for International Students

This project provides an interactive visualization dashboard for analyzing sentiment data collected from international students in the U.S. It uses `Pandas`, `Matplotlib`, and `Seaborn` to explore patterns in student feedback categorized by sentiment, gender, age, academic level, and more.

---

## 📁 Project Structure
📦 sentiment-analysis-dashboard/
├── sentimentanalysis.csv # Input data file (collected feedback)
├── sentiment_dashboard.py # Python script for data cleaning & plotting
├── README.md # Project documentation
└── ...## 🚀 Features

- **Visualizes sentiment distribution** (Very Positive to Very Negative)
- Breaks down sentiments by:
  - Gender
  - Age
  - Country
  - Major (grouped infrequent ones as "Other")
  - Academic level (Graduate/Undergraduate)
  - Time (Trend over dates)
- Custom color palette for consistent visuals
- Clean, structured layout using subplots
- Legend dynamically positioned in the top-right corner

---



## 🛠️ Technologies Used

- **Python**
- **Pandas** for data wrangling
- **Seaborn & Matplotlib** for data visualization
- VS Code= for development

---

## 📂 Dataset Description

| Column Name             | Description                                  |
|-------------------------|----------------------------------------------|
| `StudentId`             | Unique identifier for each student           |
| `Gender`                | Gender of the student                        |
| `Major`                 | Student's major                              |
| `Age`                   | Age of the student                           |
| `Country`               | Country of origin                            |
| `Dates`                 | Date when feedback was submitted             |
| `Topic`                 | Topic of concern (e.g., Housing, Visa)       |
| `Sentiment`             | Labeled sentiment (Very Positive → Negative) |
| `Feedback`              | Student's written feedback                   |
| `Graduate_Count`        | Graduate count running total (from Excel)    |
| `Undergraduate_Count`   | Undergrad count running total (from Excel)   |

---

## ✅ How to Run
1. Clone the repo:
   ```bash
   git clone: git clone https://github.com/sandhya8109/Sentiment_Analysis.git
   cd Sentiment_Analysis
