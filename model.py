import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from loan_data import generate_loan_dataset
 
FEATURE_COLUMNS = ["debt_to_equity", "current_ratio", "profit_margin", "interest_coverage"]
 
 
def train_model():
    df = generate_loan_dataset()
 
    X = df[FEATURE_COLUMNS].values
    y = df["defaulted"].values
 
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
 
    scaler  = StandardScaler()
    X_train = scaler.fit_transform(X_train)
 
    model = LogisticRegression(random_state=42, max_iter=500)
    model.fit(X_train, y_train)
 
    return model, scaler
 
 
def predict_probability(model, scaler, input_features: list) -> float:
    """Return the probability of default for a single company."""
    X = np.array(input_features).reshape(1, -1)
    X = scaler.transform(X)
    return float(model.predict_proba(X)[0][1])