import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from financial_ratios import compute_all_ratios
from risk_scoring import compute_risk_score
from model import train_model, predict_probability
from decision_engine import make_decision, generate_ml_insight


st.set_page_config(
    page_title="Corporate Loan Risk Analyzer",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp {
    background: #0c0f18;
    color: #d4d8e2;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem; max-width: 1200px; }

.page-header {
    padding: 2rem 0 1.5rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 2rem;
}
.page-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #e8eaf0;
    margin: 0 0 0.3rem 0;
    letter-spacing: -0.01em;
}
.page-subtitle {
    font-size: 0.82rem;
    color: #4a5568;
    font-weight: 400;
    margin: 0;
}

.section-title {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #3a7bd5;
    margin-bottom: 1rem;
}

.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 6px !important;
    color: #d4d8e2 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.9rem !important;
}
.stNumberInput > div > div > input:focus {
    border-color: rgba(58, 123, 213, 0.5) !important;
    box-shadow: 0 0 0 2px rgba(58, 123, 213, 0.12) !important;
}

label {
    color: #7a8ba8 !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
}

.stButton > button {
    background: #1a3a6b !important;
    color: #a8c4f0 !important;
    border: 1px solid rgba(58,123,213,0.3) !important;
    border-radius: 6px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    width: 100% !important;
    padding: 0.6rem 1.5rem !important;
    transition: background 0.15s !important;
}
.stButton > button:hover {
    background: #1f4785 !important;
    border-color: rgba(58,123,213,0.55) !important;
}

.metric-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 8px;
    padding: 1.1rem 1.2rem;
    text-align: center;
}
.metric-number {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1.6rem;
    font-weight: 500;
    line-height: 1;
    margin-bottom: 0.35rem;
}
.metric-label {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #3d4f66;
}
.metric-hint {
    font-size: 0.62rem;
    color: #2a3a50;
    margin-top: 0.2rem;
}

.decision-block {
    border-radius: 8px;
    padding: 1.25rem 1.5rem;
    text-align: center;
    margin: 1rem 0 0.5rem 0;
}
.decision-label {
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}
.decision-description {
    font-size: 0.78rem;
    margin-top: 0.4rem;
    opacity: 0.7;
}
.decision-approve {
    background: rgba(16, 185, 129, 0.07);
    border: 1px solid rgba(16, 185, 129, 0.25);
    color: #34d399;
}
.decision-review {
    background: rgba(234, 179, 8, 0.07);
    border: 1px solid rgba(234, 179, 8, 0.25);
    color: #fbbf24;
}
.decision-reject {
    background: rgba(239, 68, 68, 0.07);
    border: 1px solid rgba(239, 68, 68, 0.25);
    color: #f87171;
}

.rule-flag {
    background: rgba(239, 68, 68, 0.05);
    border-left: 2px solid rgba(239, 68, 68, 0.35);
    padding: 0.55rem 0.9rem;
    margin: 0.35rem 0;
    font-size: 0.82rem;
    color: #f0a0a0;
    border-radius: 0 4px 4px 0;
}
.rule-pass {
    background: rgba(16, 185, 129, 0.05);
    border-left: 2px solid rgba(16, 185, 129, 0.3);
    color: #6ee7b7;
}

.insight-panel {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 1rem 1.1rem;
    font-size: 0.82rem;
    color: #8899b4;
    line-height: 1.7;
    margin-top: 0.75rem;
}
.insight-label {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #3a4d66;
    margin-bottom: 0.5rem;
}

.placeholder-panel {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 400px;
    border: 1px dashed rgba(255,255,255,0.05);
    border-radius: 8px;
    text-align: center;
}
.placeholder-text {
    font-size: 0.82rem;
    color: #2a3a50;
    line-height: 1.6;
}

.stProgress > div > div > div > div { border-radius: 2px !important; }

hr {
    border: none !important;
    border-top: 1px solid rgba(255,255,255,0.05) !important;
    margin: 2rem 0 1rem 0 !important;
}
</style>
""", unsafe_allow_html=True)


@st.cache_resource(show_spinner=False)
def load_model():
    return train_model()


st.markdown("""
<div class="page-header">
    <p class="page-title">Corporate Loan Risk Analyzer</p>
    <p class="page-subtitle">
        Rule-based scoring combined with logistic regression to assess corporate credit risk
    </p>
</div>
""", unsafe_allow_html=True)

with st.spinner("Loading model..."):
    model, scaler = load_model()


left_col, right_col = st.columns([1, 1.1], gap="large")

with left_col:
    st.markdown('<div class="section-title">Company Financials</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        revenue           = st.number_input("Revenue (Cr)",           min_value=0.0, value=500.0, step=10.0, format="%.1f")
        total_debt        = st.number_input("Total Debt (Cr)",        min_value=0.0, value=200.0, step=10.0, format="%.1f")
        current_assets    = st.number_input("Current Assets (Cr)",    min_value=0.0, value=150.0, step=10.0, format="%.1f")
        interest_expense  = st.number_input("Interest Expense (Cr)",  min_value=0.0, value=20.0,  step=1.0,  format="%.1f")

    with c2:
        net_profit         = st.number_input("Net Profit (Cr)",          value=60.0,  step=5.0,  format="%.1f")
        total_equity       = st.number_input("Total Equity (Cr)",  min_value=0.0, value=250.0, step=10.0, format="%.1f")
        current_liabilities = st.number_input("Current Liabilities (Cr)", min_value=0.0, value=120.0, step=10.0, format="%.1f")

    st.markdown("<br>", unsafe_allow_html=True)

    btn_col, reset_col = st.columns([3, 1])
    with btn_col:
        analyze = st.button("Run Analysis", use_container_width=True)
    with reset_col:
        st.button("Reset", use_container_width=True)

    if revenue == 0:
        st.warning("Revenue is zero. Profit margin cannot be computed accurately.")
    if total_equity == 0:
        st.warning("Total equity is zero. Debt-to-equity ratio will reflect maximum risk.")
    if interest_expense == 0:
        st.info("No interest expense entered. Interest coverage will default to zero.")


with right_col:
    if analyze:
        with st.spinner("Running analysis..."):

            ratios = compute_all_ratios(
                revenue=revenue,
                net_profit=net_profit,
                total_debt=total_debt,
                total_equity=total_equity,
                current_assets=current_assets,
                current_liabilities=current_liabilities,
                interest_expense=interest_expense,
            )

            scoring    = compute_risk_score(ratios)
            risk_score = scoring["score"]

            features = [
                ratios["debt_to_equity"],
                ratios["current_ratio"],
                ratios["profit_margin"],
                ratios["interest_coverage"],
            ]
            prob           = predict_probability(model, scaler, features)
            decision_result = make_decision(prob)
            insight        = generate_ml_insight(prob)

        # Computed Ratios
        st.markdown('<div class="section-title">Computed Ratios</div>', unsafe_allow_html=True)

        ratio_cols = st.columns(4)
        ratio_items = [
            ("D / E Ratio",       ratios["debt_to_equity"],   "> 2 is elevated"),
            ("Current Ratio",     ratios["current_ratio"],    "< 1 is a concern"),
            ("Profit Margin",     ratios["profit_margin"],    "< 10% is weak"),
            ("Interest Coverage", ratios["interest_coverage"], "< 2x is stressed"),
        ]

        for col, (label, value, hint) in zip(ratio_cols, ratio_items):
            with col:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-number" style="color:#5a8fd4">{value:.2f}</div>
                    <div class="metric-label">{label}</div>
                    <div class="metric-hint">{hint}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Risk Score and ML Probability
        st.markdown('<div class="section-title">Risk Assessment</div>', unsafe_allow_html=True)

        score_color = "#34d399" if risk_score <= 25 else ("#fbbf24" if risk_score <= 55 else "#f87171")
        prob_color  = "#34d399" if prob < 0.30      else ("#fbbf24" if prob <= 0.60      else "#f87171")

        score_col, prob_col = st.columns(2)

        with score_col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-number" style="color:{score_color}; font-size:2.8rem">{risk_score}</div>
                <div class="metric-label">Rule-Based Risk Score</div>
                <div class="metric-hint">0 — minimal &nbsp;·&nbsp; 100 — critical</div>
            </div>
            """, unsafe_allow_html=True)
            st.progress(risk_score / 100)

        with prob_col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-number" style="color:{prob_color}; font-size:2.8rem">{prob * 100:.1f}%</div>
                <div class="metric-label">Default Probability</div>
                <div class="metric-hint">Logistic Regression estimate</div>
            </div>
            """, unsafe_allow_html=True)
            st.progress(prob)

        st.markdown("<br>", unsafe_allow_html=True)

        # Final Decision
        dec       = decision_result["decision"]
        css_class = {"APPROVE": "decision-approve", "REVIEW": "decision-review", "REJECT": "decision-reject"}[dec]

        st.markdown(f"""
        <div class="decision-block {css_class}">
            <div class="decision-label">{dec}</div>
            <div class="decision-description">{decision_result["description"]}</div>
        </div>
        """, unsafe_allow_html=True)

        # Risk Flags
        st.markdown('<div class="section-title" style="margin-top:1.5rem">Risk Flags</div>', unsafe_allow_html=True)

        if scoring["triggered"]:
            for condition in scoring["triggered"]:
                st.markdown(f'<div class="rule-flag">{condition}</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                '<div class="rule-flag rule-pass">All rule-based checks passed. No risk flags triggered.</div>',
                unsafe_allow_html=True,
            )

        # Model Insight
        st.markdown(f"""
        <div class="insight-panel">
            <div class="insight-label">Model Insight</div>
            {insight}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="placeholder-panel">
            <div class="placeholder-text">
                Enter company financials and click <strong>Run Analysis</strong><br>to generate the risk report.
            </div>
        </div>
        """, unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<p style="text-align:center; color:#1e2a3a; font-size:0.68rem; letter-spacing:0.06em; text-transform:uppercase;">
    Corporate Loan Risk Analyzer &nbsp;·&nbsp; Logistic Regression + Rule Engine &nbsp;·&nbsp; Fintech MVP
</p>
""", unsafe_allow_html=True)
