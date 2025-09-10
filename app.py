import streamlit as st
import pandas as pd
import joblib

# Load data and model
data = pd.read_csv("Cleaned_data.csv")
with open("Model.joblib", "rb") as f:
    model = joblib.load("Model.joblib")

st.markdown("""
    <style>
    html, body {
        background: linear-gradient(to right, #dfe9f3, #ffffff);
        font-family: 'Segoe UI', sans-serif;
    }
    .header {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 10px;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 10px;
    }
    .section {
        background-color: rgba(255, 255, 255, 0.6);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .predict-btn {
        background-color: #ff6f61;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 6px;
        padding: 10px;
        width: 100%;
        border: none;
    }
    .result-card {
        background: linear-gradient(to right, #e0f7fa, #e8f5e9);
        color: #004d40;
        font-size: 24px;
        font-weight: bold;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔍 Bengaluru HomeScope")
st.sidebar.markdown("""
Welcome to **HomeScope** — your smart assistant for estimating house prices in Bengaluru.

✅ Choose your preferences  
✅ Click **Estimate Now**  
✅ Get instant insights  
""")
st.sidebar.caption("Crafted with precision by Priya Gupta 💻")

# Header
st.markdown('<div class="header"><h1>🏡 Bengaluru HomeScope</h1><p>Smart Price Estimator for Your Dream Home</p></div>', unsafe_allow_html=True)

# Input Section
with st.container():
    st.markdown('<div class="section"><h4>📊 Property Details</h4>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        location = st.selectbox("📍 Select Location", sorted(data['location'].unique()))
        bhk = st.number_input("🛏️ Bedrooms (BHK)", 1, 10, 3)
    with col2:
        total_sqft = st.number_input("📐 Total Area (sq ft)", min_value=300.0, max_value=10000.0, value=1000.0)
        bath = st.number_input("🛁 Bathrooms", 1, 10, 2)
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction Button
if st.button("🚀 Estimate Now", key="predict"):
    input_df = pd.DataFrame([[location, total_sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction = model.predict(input_df)[0]
    st.markdown(f'<div class="result-card">💰 Estimated Price: ₹ {prediction:.2f} Lakhs</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr style="margin-top:20px;">
    <div style="text-align:center; font-size:14px; color:#666;">
        © 2025 HomeScope by Priya Gupta | Powered by Streamlit
    </div>
""", unsafe_allow_html=True)