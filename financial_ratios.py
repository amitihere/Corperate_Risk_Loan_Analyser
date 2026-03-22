def safe_divide(numerator: float, denominator: float, fallback: float = 0.0) -> float:
    if denominator == 0:
        return fallback
    return numerator / denominator
 
 
def compute_all_ratios(
    revenue: float,
    net_profit: float,
    total_debt: float,
    total_equity: float,
    current_assets: float,
    current_liabilities: float,
    interest_expense: float,
) -> dict:
    return {
        "debt_to_equity":    safe_divide(total_debt,  total_equity,        fallback=9999.0),
        "current_ratio":     safe_divide(current_assets, current_liabilities, fallback=0.0),
        "profit_margin":     safe_divide(net_profit,  revenue,              fallback=0.0),
        "interest_coverage": safe_divide(net_profit,  interest_expense,     fallback=0.0),
    }
 