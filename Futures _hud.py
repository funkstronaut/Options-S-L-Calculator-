import streamlit as st

# Set page config for a cleaner look
st.set_page_config(page_title="Futures HUD", layout="centered")

# CSS to generate the CBOE background and the Glowing Spaceship Console
st.markdown("""
<style>
    /* Background Image */
    .stApp {
        background-image: url("https://www.optionstrategist.com/sites/default/files/trading-pit-3-courtesy-of-cboe-global-markets-2.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Glowing HUD Container */
    .hud-container {
        background-color: rgba(10, 20, 35, 0.65); /* Translucent Blue */
        border: 2px solid #00FFFF;
        box-shadow: 0 0 15px #00FFFF, inset 0 0 10px #00FFFF;
        border-radius: 10px;
        padding: 25px;
        font-family: 'Courier New', Courier, monospace;
        color: #00FFFF;
        margin-top: 20px;
    }
    
    /* Text Styling and Drop Shadows */
    .hud-title {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 20px;
        border-bottom: 1px solid #00FFFF;
        padding-bottom: 10px;
    }
    .data-row {
        font-size: 18px;
        font-weight: bold;
        margin: 10px 0;
        text-shadow: 2px 2px 4px #000000;
    }
    
    /* Glowing Colors for Targets and Risk */
    .risk { color: #FF3333; text-shadow: 0 0 8px #FF3333, 2px 2px 4px #000000; }
    .target { color: #33FF33; text-shadow: 0 0 8px #33FF33, 2px 2px 4px #000000; }
    
    /* Streamlit Input Overrides */
    label { color: #00FFFF !important; font-weight: bold; font-family: 'Courier New', Courier, monospace; }
</style>
""", unsafe_allow_html=True)

st.title("🛰️ Futures Tactical HUD")

# Input Section
position_type = st.radio("Select Position Type:", ["Long", "Short"])
entry_price = st.number_input("Enter Fill Price:", min_value=0.0, value=100.0, step=0.25)

# Math Logic
if entry_price > 0:
    if position_type == "Long":
        stop_price = entry_price - (entry_price * 0.15)
        tp_30 = entry_price + (entry_price * 0.30)
        tp_50 = entry_price + (entry_price * 0.50)
        tp_75 = entry_price + (entry_price * 0.75)
    else:
        # Short Logic: Stop is above, Targets are below
        stop_price = entry_price + (entry_price * 0.15)
        tp_30 = entry_price - (entry_price * 0.30)
        tp_50 = entry_price - (entry_price * 0.50)
        tp_75 = entry_price - (entry_price * 0.75)

    # Output Section (No indentation in HTML strings to avoid code block rendering)
    st.markdown(f"""
<div class="hud-container">
<div class="hud-title">MISSION BRIEFING: {position_type.upper()}</div>
<div class="data-row">ENTRY PRICE: {entry_price:,.2f}</div>
<div class="data-row risk">15% HARD STOP: {stop_price:,.2f}</div>
<div class="data-row target">30% TARGET 1: {tp_30:,.2f}</div>
<div class="data-row target">50% TARGET 2: {tp_50:,.2f}</div>
<div class="data-row target">75% TARGET 3: {tp_75:,.2f}</div>
</div>
    """, unsafe_allow_html=True)
