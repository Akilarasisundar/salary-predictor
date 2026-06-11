import streamlit as st
import numpy as np
import pickle
from time import sleep

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Salary Predictor Pro", page_icon="💼", layout="wide")

# ---------------- LOAD MODEL ----------------
model = pickle.load(open(r"C:\Users\akila\OneDrive\Desktop\project 1\model.pkl", "rb"))

# ---------------- CSS (ANIMATED UI) ----------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Glass card */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
    animation: fadeIn 1s ease-in-out;
}

/* Title */
.title {
    font-size: 45px;
    font-weight: bold;
    text-align: center;
    color: #22c55e;
    animation: slideDown 1s ease;
}

.subtitle {
    text-align: center;
    color: #cbd5f5;
    margin-bottom: 40px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: white;
    height: 50px;
    width: 100%;
    border-radius: 12px;
    font-size: 18px;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
}

/* Result */
.result-box {
    background: linear-gradient(90deg, #22c55e, #4ade80);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 26px;
    color: white;
    margin-top: 20px;
    animation: popUp 0.6s ease;
}

/* Animations */
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

@keyframes slideDown {
    from {transform: translateY(-40px); opacity:0;}
    to {transform: translateY(0); opacity:1;}
}

@keyframes popUp {
    from {transform: scale(0.8); opacity:0;}
    to {transform: scale(1); opacity:1;}
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>💼 Salary Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered salary prediction based on experience</div>", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📊 Enter Details")

    experience = st.slider("Years of Experience", 0, 40, 1)

    predict = st.button("🚀 Predict Salary")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("💰 Result")

    if predict:
        with st.spinner("Analyzing..."):
            sleep(1.5)
            result = model.predict([[experience]])

        st.markdown(
            f"<div class='result-box'>₹ {result[0]:,.2f}</div>",
            unsafe_allow_html=True
        )
    else:
        st.info("Enter details and click predict")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EXTRA SECTION ----------------
st.markdown("---")
st.markdown("### 📈 Why this model?")
st.write("""
- Uses Machine Learning  
- Predicts based on real patterns  
- Fast & accurate  
""")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("© 2026 Salary Predictor Pro | Designed with ❤️")