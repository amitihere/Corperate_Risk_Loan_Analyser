import numpy as np
import pandas as pd


def generate_loan_dataset(n_samples: int = 100, random_state: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(random_state)

    debt_to_equity    = rng.uniform(0.2, 5.0, n_samples)
    current_ratio     = rng.uniform(0.5, 3.5, n_samples)
    profit_margin     = rng.uniform(-0.05, 0.40, n_samples)
    interest_coverage = rng.uniform(0.5, 8.0, n_samples)

    risk = (
          (debt_to_equity   > 2.5).astype(float) * 0.35
        + (current_ratio    < 1.0).astype(float) * 0.25
        + (profit_margin    < 0.05).astype(float) * 0.25
        + (interest_coverage < 1.5).astype(float) * 0.25
    )
    noise     = rng.uniform(0, 0.2, n_samples)
    defaulted = ((risk + noise) > 0.45).astype(int)

    return pd.DataFrame({
        "debt_to_equity":    debt_to_equity,
        "current_ratio":     current_ratio,
        "profit_margin":     profit_margin,
        "interest_coverage": interest_coverage,
        "defaulted":         defaulted,
    })