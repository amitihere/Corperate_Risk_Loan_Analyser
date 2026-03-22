# Corporate Loan Risk Analyzer

This project is a Fintech MVP application designed to assess corporate credit risk. It combines rule-based scoring with a logistic regression model to evaluate the financial health of a company and predict its probability of default.

## Key Features
- **Comprehensive Financial Analysis**: Evaluates key financial metrics including Revenue, Total Debt, Current Assets, Interest Expense, Net Profit, Total Equity, and Current Liabilities.
- **Real-time Ratio Computation**: Automatically calculates important financial ratios such as Debt-to-Equity (D/E), Current Ratio, Profit Margin, and Interest Coverage.
- **Dual Risk Assessment System**:
  1. **Rule-Based Engine**: Provides a transparent risk score (0-100) based on predefined financial thresholds.
  2. **Machine Learning Model**: Uses Logistic Regression to estimate the default probability of the company.
- **Automated Decision Output**: Offers an immediate Approve, Review, or Reject decision based on the combined analysis, with detailed risk flags for areas of concern.
- **Interactive Dashboard**: Built with Streamlit for a responsive, clean, and intuitive user interface.

## Setup & Installation
1. Ensure Python 3.8+ is installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Technologies Used
- Python
- Streamlit
- Scikit-Learn (Logistic Regression)
- Pandas / NumPy
