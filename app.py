import streamlit as st

st.set_page_config(
    page_title="Airline Satisfaction Dashboard",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# GLOBAL CSS
# =========================
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"] {
    font-family: 'Poppins', poppins;
}

.stApp {
    font-family: 'Poppins';
    background: linear-gradient(
        180deg,
        #F8FAFC 0%,
        #EFF6FF 100%
    );
}
/* SIDEBAR */
[data-testid="stSidebar"] {
    font-family: 'Poppins';
    background:
    linear-gradient(
        180deg,
        #081F5C 0%,
        #0F52BA 45%,
        #2563EB 100%
    );
    padding-top: 20px;
}

[data-testid="stSidebar"] * {
    color: white;
}
.sidebar-logo {
    font-family: 'Poppins';
    background: rgba(255,255,255,0.10);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    margin-bottom: 25px;
}

.main-title {
    font-family: 'Poppins', poppins;
    font-size: 48px;
    font-weight: 800;
    color: #0F172A;
}

.subtitle {
    font-family: 'Poppins';
    font-size: 18px;
    color: #475569;
    margin-bottom: 35px;
}

.primary-card {
font-family: 'Poppins';
    background: linear-gradient(
        135deg,
        #081F5C 0%,
        #1E3A8A 100%
    );
    border-radius: 22px;
    padding: 28px;
    color: white;
}

.secondary-card {
font-family: 'Poppins';
    background: linear-gradient(
        135deg,
        #DBEAFE 0%,
        #EFF6FF 100%
    );
    border-left: 5px solid #2563EB;
    border-radius: 18px;
    padding: 22px;
}

.section-title {
    font-family: 'Poppins';
    font-size: 28px;
    font-weight: 800;
    color: #1E3A8A;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================
st.sidebar.markdown("""
<div class="sidebar-logo">
    <h2>✈ AirInsight</h2>
    <p>Passenger Analytics System</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

st.sidebar.subheader("Navigation")

st.sidebar.info(
    "Explore analytical insights, compare machine learning models, and simulate passenger satisfaction predictions."
)

st.markdown("""
<div class="main-title">✈ Airline Passenger Satisfaction Dashboard</div>
<div class="subtitle">
Comprehensive analytics for customer behavior, model comparison, and predictive insights.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="primary-card">
<h3>Dashboard Overview</h3>
<p>
Analyze airline passenger satisfaction using interactive visual analytics,
machine learning model evaluation, and prediction simulation.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="section-title">Dashboard Modules</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

modules = [
    ("📊 Dashboard Analysis", "Explore passenger demographics and service quality."),
    ("📉 Model Evaluation", "Compare model performance and feature importance."),
    ("🔮 Prediction", "Predict satisfaction in real-time.")
]

for col, (title, desc) in zip([col1, col2, col3], modules):
    with col:
        st.markdown(f"""
        <div class="secondary-card">
        <h4>{title}</h4>
        <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)
