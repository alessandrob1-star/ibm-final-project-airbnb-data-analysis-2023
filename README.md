# Airbnb New York City - Exploratory Data Analysis

![Airbnb](https://img.shields.io/badge/Airbnb-%23FF5A5F.svg?style=for-the-badge&logo=Airbnb&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

**Final Capstone Project** | IBM Programme in Data Analytics 

---

## 📋 Project Overview

This project presents a complete **Exploratory Data Analysis (EDA)** of the Airbnb market in New York City. Starting from a raw dataset, the analysis includes data cleaning, preprocessing, visualization, and the extraction of meaningful business insights regarding pricing patterns, room types, and neighbourhood performance.

---

## 🎯 Objectives

- Assess data quality and perform thorough cleaning (missing values, duplicates, inconsistencies)
- Standardize column names and data formats
- Analyze pricing dynamics across room types and boroughs
- Identify the most active and profitable neighbourhoods
- Extract actionable insights for hosts and market stakeholders

---

## 🛠 Tools & Technologies

- **Python**
- **Pandas** & **NumPy** — Data manipulation
- **Matplotlib** & **Seaborn** — Data visualization
- **Jupyter Notebook**

---

## Reproducing the notebook

The saved notebook was created with Python 3.12. Install the analysis and notebook dependencies:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m notebook
```

Open `ibm-final-project-airbnb-data-analysis.ipynb`. The input CSV is not included
in this repository. Supply `Airbnb_Open_Data.csv` from the dataset used for the
project and change `data_path` in the first code cell to your local file path
before running all cells. The saved outputs can be inspected without the CSV.
The dependency ranges are not a lockfile and do not reproduce the original environment exactly.

---

## 📈 Key Insights

- **Queens** surprisingly shows the highest average listing price, followed by Bronx and Brooklyn.
- Price differences across boroughs are relatively small, so this result should be interpreted with caution and may reflect dataset limitations rather than actual market pricing.
- **Entire homes/apartments** are significantly more expensive than private and shared rooms.
- Extremely strong positive correlation (**~0.99**) between `price` and `service_fee`.
- Listings are heavily concentrated in a few popular neighbourhoods (Williamsburg, Bedford-Stuyvesant, Harlem, etc.).
- The dataset was relatively clean after preprocessing, with no extreme price outliers detected.

---


## 📜 Certification

**IBM Programme Data Analytics** - Final Project

![IBM Certificate](certificate.png)

[View Credly Badge](https://www.credly.com/badges/94cd09c5-fbca-466d-b6a5-b38ac423fbeb/linked_in?t=s3wbqe)

---

## 👤 Author

**Alessandro Benevelli**

---

**Feel free to explore the notebook and reach out if you have any questions!**
