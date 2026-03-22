# 🏦 Corporate Risk Loan Analyzer

![Hackathon](https://img.shields.io/badge/Hackathon-Project-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)

**Corporate Risk Loan Analyzer** is an end-to-end Fintech MVP built for corporate credit risk assessment. It dynamically blends a **Deterministic Rule-Based Engine** with a **Machine Learning Model** (Logistic Regression) to evaluate a company's financial health, calculate key ratios, and estimate default probabilities instantly.

---

## 🎯 Problem Statement
In corporate lending, assessing the risk of loan default relies heavily on synthesizing massive amounts of financial data. Traditional methods are either entirely manual (which is slow) or rely purely on black-box ML models (which lack interpretability). This project brings the best of both worlds:
- **Interpretability** using deterministic financial ratios and risk scoring.
- **Predictive Power** using a Logistic Regression model trained on historical commercial loan data.

---

## 🧠 The Approach: Logistic Regression Model
We utilize **Logistic Regression** for the machine learning component of our assessment. 
- **Why Logistic Regression?** In the highly regulated financial industry, model explainability is critical. Logistic Regression provides clear coefficients, allowing us to see *exactly* how much features like the *Debt-to-Equity Ratio* or *Profit Margin* affect the probability of default.
- **How it works:** The algorithm takes computed financial ratios (features) from the user input, scales them, and applies the sigmoid function to map the output to a probability between `0` and `1`. 
- **Output:** A strict percentage representing the likelihood that the corporation will default on the loan.

---

## 📂 Project Structure & File Descriptions

Here represents the core architecture of our system:

- **📄 `app.py`**
  The main entry point of the application. Built with Streamlit, this file handles the interactive UI, capturing user input for company financials, coordinating the backend logic, and displaying the Dual Risk Assessment (Ratios, Rule-Based Score, and ML Default Probability) in a rich dashboard.

- **📄 `model.py`**
  Houses the machine learning pipeline. It handles the instantiation, training, and scaling of the `Logistic Regression` model. The `predict_probability` function takes live inputs, scales the features, and infers the final default probability.

- **📄 `loan_data.py`**
  Manages the data layer. Creates, processes, and structures the historical corporate loan data used to train our ML model.

- **📄 `financial_ratios.py`**
  The financial calculator module. Takes raw numbers (Revenue, Total Debt, Equity, etc.) and performs strict accounting computations to output critical business metrics (e.g., *Debt-to-Equity Range, Current Ratio, Interest Coverage*).

- **📄 `risk_scoring.py`**
  The deterministic Rule-Based Engine. It evaluates the outputs from `financial_ratios.py` against industry-standard benchmarks (e.g., D/E > 2 is risky) and assigns a transparent penalty score from 0 (Safe) to 100 (Critical).

- **📄 `decision_engine.py`**
  The final orchestrator. It synthesizes the ML probability and the rule-based score to generate a definitive business decision (**APPROVE**, **REVIEW**, or **REJECT**) alongside human-readable insights.

- **📄 `requirements.txt`**
  Contains all the Python dependencies required to deploy the application.

---

## 🚀 Setup & Installation

Follow these steps to run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/amitihere/Corperate_Risk_Loan_Analyser.git
   cd Corperate_Risk_Loan_Analyser
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.8+ installed. Run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Application:**
   ```bash
   streamlit run app.py
   ```
