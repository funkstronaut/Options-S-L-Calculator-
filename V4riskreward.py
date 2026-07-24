import streamlit as st

# MUST be the first Streamlit command
st.set_page_config(layout="wide", page_title="Options Risk HUD", initial_sidebar_state="collapsed")

# --- Custom CSS Injection ---
# Pulling the CBOE pit image directly from the web
BACKGROUND_IMAGE_URL = 'https://www.optionstrategist.com/sites/default/files/trading-pit-3-courtesy-of-cboe-global-markets-2.jpg' 

style_config = f"""
<style>
    .stApp {{
        background-color: #000; 
        background-image: url("{BACKGROUND_IMAGE_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Courier New', Courier, monospace; 
        color: #fff;
    }}
    [data-testid="stMainBlockContainer"] {{
        background: rgba(0, 5, 20, 0.85); 
        border: 2px solid #00ffff; 
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.5); 
        border-radius: 10px;
        padding: 2rem !important;
        max-width: 900px;
        margin: 5rem auto; 
    }}
    .stNumberInput div[data-baseweb="input"] {{
        background-color: transparent !important;
        border: 2px solid #00ccff !important; 
        color: #fff !important;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 204, 255, 0.4); 
    }}
    .stNumberInput input {{
        color: #fff !important;
        font-size: 1.2rem;
        text-align: center;
    }}
    .stNumberInput label {{
        color: #00ffff !important; 
        font-weight: bold;
        letter-spacing: 1px;
    }}
    .cyber-hud {{
        border: 1px solid rgba(0, 255, 255, 0.3);
        background: rgba(0, 255, 255, 0.03); 
        padding: 1.5rem;
        margin-top: 1rem;
        border-radius: 8px;
    }}
    .briefing-header {{
        color: #fff;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-weight: bold;
        font-size: 1.4rem;
        margin-bottom: 2rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.3);
        padding-bottom: 10px;
    }}
    .hud-line {{
        display: flex;
        align-items: center;
        justify-content: space-between; 
        font-size: 1.6rem; 
        margin-bottom: 15px;
    }}
    .risk-price {{ color: #ff0033; font-weight: bold; text-shadow: 0 0 15px rgba(255, 0, 51, 0.8); }} 
    .target-price {{ color: #00ff66; font-weight: bold; text-shadow: 0 0 15px rgba(0, 255, 102, 0.8); }} 
    .target-pct {{ color: #fff; font-size: 1.3rem; margin-right: 15px; }} 

    .icon-red {{ color: #ff0033; margin-right: 10px; }}
    .icon-green {{ color: #00ff66; margin-right: 10px; }}
</style>
"""
st.markdown(style_config, unsafe_allow_html=True)

# --- Calculator Core Logic ---
col1, col2 = st.columns(2)
with col1:
    premium = st.number_input("PREMIUM PAID ($)", min_value=0.00, value=1.00, step=0.01)
with col2:
    stop_pct = st.number_input("STOP LOSS (%)", min_value=0, value=15, step=1, disabled=False) 

# Core Calculations
stop_amount = premium * (stop_pct / 100)
stop_price = premium - stop_amount

target_30 = premium * 1.30
target_50 = premium * 1.50
target_75 = premium * 1.75

# --- Output ---
results_col1, results_col2, results_col3 = st.columns([1, 6, 1]) 
with results_col2:
    # Formatting the HTML flush to the left removes the code block rendering issue
    html_output = f"""<div class="cyber-hud">
<div class="briefing-header">OPTIONS RISK & REWARD BRIEFING</div>
<div class="hud-line">
<span><span class="icon-red">🔴</span> <span class="target-pct">STOP LOSS PRICE</span></span>
<span class="risk-price">${stop_price:.2f}</span>
</div>
<div class="hud-line">
<span><span class="icon-green">🟢</span> <span class="target-pct">30% PROFIT TARGET</span></span>
<span class="target-price">${target_30:.2f}</span>
</div>
<div class="hud-line">
<span><span class="icon-green">🟢</span> <span class="target-pct">50% PROFIT TARGET</span></span>
<span class="target-price">${target_50:.2f}</span>
</div>
<div class="hud-line">
<span><span class="icon-green">🟢</span> <span class="target-pct">75% PROFIT TARGET</span></span>
<span class="target-price">${target_75:.2f}</span>
</div>
</div>"""
    
    st.markdown(html_output, unsafe_allow_html=True)
