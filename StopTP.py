import streamlit as st

# MUST be the first Streamlit command
st.set_page_config(layout="wide", page_title="Options Risk HUD", initial_sidebar_state="collapsed")

# --- Custom CSS Injection ---
# We inject custom CSS to override Streamlit's default appearance and
# achieve the glowing, futuristic control panel look.

# (Assuming you have an image 'CBOE_Pit_BG.jpg' in the same GitHub repo folder)
# If you don't have this asset, the code will default to a dark background.
BACKGROUND_IMAGE_URL = 'CBOE_Pit_BG.jpg' 

style_config = f"""
<style>
    /* 1. Page Background (The "Outside" CBOE Pit View) */
    .stApp {{
        background-color: #000; /* Backup black background */
        background-image: url("{BACKGROUND_IMAGE_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Courier New', Courier, monospace; /* Old school / Retro font */
        color: #fff;
    }}

    /* 2. Style the main content block to look like the central console panel */
    [data-testid="stMainBlockContainer"] {{
        background: rgba(0, 5, 20, 0.85); /* Deep space blue, translucent */
        border: 2px solid #00ffff; /* Glowing cyan border around the console */
        box-shadow: 0 0 30px rgba(0, 255, 255, 0.5); /* Primary cyan glow */
        border-radius: 10px;
        padding: 2rem !important;
        max-width: 900px;
        margin: 5rem auto; /* Centered on screen, like the foreground console */
    }}

    /* 3. Style the interactive inputs to have that high-tech blue glow */
    .stNumberInput div[data-baseweb="input"] {{
        background-color: transparent !important;
        border: 2px solid #00ccff !important; /* Lighter cyan border */
        color: #fff !important;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 204, 255, 0.4); /* Glow on the input boxes */
    }}
    .stNumberInput input {{
        color: #fff !important;
        font-size: 1.2rem;
        text-align: center;
    }}
    .stNumberInput label {{
        color: #00ffff !important; /* Specific cyan color for labels */
        font-weight: bold;
        letter-spacing: 1px;
    }}

    /* 4. Custom Styling for the Output "Briefing" Section */
    .cyber-hud {{
        border: 1px solid rgba(0, 255, 255, 0.3);
        background: rgba(0, 255, 255, 0.03); /* Subtle internal cyan tint */
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
        justify-content: space-between; /* Keeps values aligned, matching the image density */
        font-size: 1.6rem; /* Large, glowing output text */
        margin-bottom: 15px;
    }}

    /* Style for the colored icons and large glowing results */
    .risk-price {{ color: #ff0033; font-weight: bold; text-shadow: 0 0 15px rgba(255, 0, 51, 0.8); }} /* RED Risk Glow */
    .target-price {{ color: #00ff66; font-weight: bold; text-shadow: 0 0 15px rgba(0, 255, 102, 0.8); }} /* GREEN Target Glow */
    .target-pct {{ color: #fff; font-size: 1.3rem; margin-right: 15px; }} /* Text before the $ amount */

    .icon-red {{ color: #ff0033; margin-right: 10px; }}
    .icon-green {{ color: #00ff66; margin-right: 10px; }}

</style>
"""
st.markdown(style_config, unsafe_allow_html=True)

# --- Calculator Core Logic (Remains simple) ---
# Inputs: Using layout columns to center the interactive inputs like the console cluster
st.markdown("<div style='text-align: center; color: #00ffff; font-size: 1rem; margin-bottom: 0.5rem;'>FINRA LICENSED SYSTEM (SIE/SERIES 7/63)</div>", unsafe_allow_html=True) # Added the atmospheric license note from the image

col1, col2 = st.columns(2)
with col1:
    premium = st.number_input("PREMIUM PAID ($)", min_value=0.00, value=1.00, step=0.01)
with col2:
    # 15% is the user's explicit simple formula request from the very first prompt. We hardcode it like the initial example.
    stop_pct = st.number_input("STOP LOSS (%)", min_value=0, value=15, step=1, disabled=False) 

# Core Calculations
stop_amount = premium * (stop_pct / 100)
stop_price = premium - stop_amount

target_30 = premium * 1.30
target_50 = premium * 1.50
target_75 = premium * 1.75

# --- Output: Recreating the Specific HUD Briefing Layout via HTML/CSS ---
# Using columns to create dense data density similar to the image's "HUD Analysis"
results_col1, results_col2, results_col3 = st.columns([1, 6, 1]) # Large central column for the main Briefing
with results_col2:
    st.markdown(f"""
    <div class="cyber-hud">
        <div class="briefing-header">OPTIONS RISK & REWARD BRIEFING</div>
        
        <!-- STOP LOSS LINE (Red/Risk) -->
        <div class="hud-line">
            <span><span class="icon-red">🔴</span> <span class="target-pct">STOP LOSS PRICE</span></span>
            <span class="risk-price">${stop_price:.2f}</span>
        </div>

        <!-- TARGET LINES (Green/Profit) -->
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
        
        <!-- Add the subtle FINRA licenses text at the bottom, matching the image -->
        <div style="font-size: 0.8rem; color: rgba(0, 255, 255, 0.4); text-align: center; margin-top: 2rem; text-transform: uppercase;">FINRA SIE/SERIES 7/63 LICENSED ANALYST</div>
    </div>
    """, unsafe_allow_html=True)
