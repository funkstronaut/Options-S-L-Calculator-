import streamlit as st

st.title("Options Risk & Reward Calculator")

# User inputs
premium = st.number_input("Premium Paid ($)", min_value=0.00, value=1.00, step=0.01)
stop_pct = st.number_input("Stop Loss %", min_value=0, value=15, step=1)

# Core Math
stop_amount = premium * (stop_pct / 100)
stop_price = premium - stop_amount

target_30 = premium * 1.30
target_50 = premium * 1.50
target_75 = premium * 1.75

# Display results clearly
st.markdown("---")
st.error(f"🔴 **Stop Loss (at {stop_pct}%):** ${stop_price:.2f}")
st.success(f"🟢 **30% Profit Target:** ${target_30:.2f}")
st.success(f"🟢 **50% Profit Target:** ${target_50:.2f}")
st.success(f"🟢 **75% Profit Target:** ${target_75:.2f}")
