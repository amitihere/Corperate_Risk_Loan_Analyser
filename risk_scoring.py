def compute_risk_score(ratios: dict) -> dict:
    """
    Compute a rule-based risk score from financial ratios.

    Each rule contributes a fixed weight to the total score.
    Score is capped at 100. Higher scores indicate greater credit risk.

    Returns:
        score     - integer from 0 to 100
        triggered - list of plain-language descriptions for each fired rule
    """
    score     = 0
    triggered = []

    if ratios["debt_to_equity"] > 2:
        score += 30
        triggered.append("High debt relative to equity (D/E ratio above 2)")

    if ratios["current_ratio"] < 1:
        score += 25
        triggered.append("Low liquidity — current ratio is below 1")

    if ratios["profit_margin"] < 0.10:
        score += 20
        triggered.append("Weak profitability — profit margin is under 10%")

    if ratios["interest_coverage"] < 2:
        score += 25
        triggered.append("Poor interest coverage — earnings cover interest less than 2 times")

    return {
        "score":     min(score, 100),
        "triggered": triggered,
    }