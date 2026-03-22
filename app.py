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
