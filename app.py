import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Sidebar controls
st.sidebar.title("Settings")
capital = st.sidebar.number_input("Capital per Trade (₹)", value=25000, step=5000)
sma_window = st.sidebar.slider("SMA Window", 3, 20, 5)
stop_loss_pct = st.sidebar.slider("Stop-Loss %", 1, 10, 3)
take_profit_pct = st.sidebar.slider("Take-Profit %", 1, 20, 8)

# Simulated AI pick
today_pick = {
    "symbol": "ADANIPORTS.NS",
    "name": "Adani Ports",
    "buy_price": 825.50
}

# Quantity calculation
quantity = int(capital // today_pick["buy_price"])

# Display snapshot
st.header("📅 Today's AI Pick")
st.subheader(f"{today_pick['name']} ({today_pick['symbol']})")
st.write(f"Buy Signal: ₹{today_pick['buy_price']:.2f}")
st.write(f"Quantity: {quantity} shares")
st.write(f"Target: ₹{today_pick['buy_price'] * (1 + take_profit_pct/100):.2f}")
st.write(f"Stop-Loss: ₹{today_pick['buy_price'] * (1 - stop_loss_pct/100):.2f}")

# Fetch and plot data
data = yf.download(today_pick["symbol"], period="1mo", progress=False)
data["SMA"] = data["Close"].rolling(window=sma_window).mean()

fig, ax = plt.subplots()
ax.plot(data.index, data["Close"], label="Close Price")
ax.plot(data.index, data["SMA"], label=f"{sma_window}-Day SMA", linestyle="--")
ax.legend()
st.pyplot(fig)