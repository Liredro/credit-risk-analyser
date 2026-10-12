# 📊 Credit Risk Analyser

A beginner-friendly Python project for analysing loan portfolios, calculating credit risk metrics, and visualising default rates.

## 📌 Project Overview

This project demonstrates how Python can be used to perform basic credit risk analysis on a portfolio of loans.

Using **Pandas** and **Matplotlib**, the programme processes loan data, calculates key portfolio statistics, and generates visualisations to help understand default patterns.

## 🚀 Features

- Calculate total loans and outstanding portfolio balance
- Calculate overall loan default rates
- Identify the percentage of loans overdue by 30+ days
- Compare default rates across loan types
- Generate and save a bar chart of default rates

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Pandas** — Data processing and analysis
- **Matplotlib** — Data visualisation
- **CSV** — Dataset storage

## 📂 Project Structure

- `credit_risk.py` — Main Python analysis script
- `loans.csv` — Sample loan portfolio dataset
- `README.md` — Project documentation

## ▶️ How to Run

**1.** Download or clone this repository.

**2.** Open Terminal and navigate to the project folder.

**3.** Install the required libraries:

`python3 -m pip install pandas matplotlib`

**4.** Run the programme:

`python3 credit_risk.py`

**5.** The programme will display portfolio statistics and save a chart named `default_rates.png`.

## 📈 Example Results

Using the sample dataset:

| Metric | Result |
|---|---|
| Total Loans | 10 |
| Outstanding Balance | £502,000 |
| Default Rate | 30.00% |
| Loans 30+ Days Overdue | 50.00% |

## 📁 Dataset

The project currently uses a small synthetic dataset containing 10 loan records across personal, auto and mortgage lending.

The data is intended for educational purposes and does not represent actual banking portfolios or realistic default probabilities.

## 🔮 Future Improvements

- Expand the analysis using real-world credit datasets
- Introduce additional credit risk indicators
- Integrate SQL for data extraction and analysis
- Develop more advanced financial visualisations

---

*An introductory Python project focused on developing practical financial data analysis skills.*
