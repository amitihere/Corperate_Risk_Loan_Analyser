def make_decision(probability: float) -> dict:
    """
    Translate a default probability into a lending decision.
 
    Thresholds:
        below 0.30  -> Approve
        0.30 to 0.60 -> Review
        above 0.60  -> Reject
    """
    if probability < 0.30:
        return {
            "decision":    "APPROVE",
            "description": "Default risk is within acceptable limits. The financials meet baseline lending criteria.",
        }
    elif probability <= 0.60:
        return {
            "decision":    "REVIEW",
            "description": "Moderate risk detected. A manual underwriting review is recommended before proceeding.",
        }
    else:
        return {
            "decision":    "REJECT",
            "description": "Default risk is above the acceptable threshold. The application does not meet minimum lending criteria.",
        }
 
 
def generate_ml_insight(probability: float) -> str:
    if probability > 0.60:
        return (
            "The model identifies a high probability of default. "
            "Weak financial ratios — particularly leverage, liquidity, and earnings — "
            "are the primary drivers of this assessment."
        )
    elif probability > 0.30:
        return (
            "The model detects mixed signals. Some financial indicators are within range, "
            "but others suggest potential stress under adverse conditions. "
            "A detailed credit review is advisable."
        )
    else:
        return (
            "The model indicates a low probability of default. "
            "The company demonstrates solid debt serviceability, adequate liquidity, "
            "and stable profitability relative to the training distribution."
        )
 