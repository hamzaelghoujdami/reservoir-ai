import streamlit as st
import pandas as pd
import random
import plotly.express as px
from agents.anomaly_detection_agent import AnomalyDetectionAgent
from agents.recommendation_agent import RecommendationAgent

# Streamlit UI Setup
st.set_page_config(page_title="EnergyAI Anomaly Detector", layout="wide")

st.title("💡 EnergyAI Reservoir Monitoring")

# Initialize storage for simulated data
if "data" not in st.session_state:
    st.session_state.data = []

# Function to generate random reservoir data (normal or anomalous)
def generate_data(anomaly=False):
    pressure = random.randint(1150, 1250)
    temperature = random.randint(80, 90)
    flow_rate = random.randint(280, 320)

    if anomaly:
        pressure += random.randint(50, 100)  # Introduce a pressure anomaly

    return {
        "timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pressure": pressure,
        "temperature": temperature,
        "flow_rate": flow_rate
    }

# Sidebar controls
st.sidebar.header("🔧 Test Data Input")
add_normal = st.sidebar.button("Add Normal Data")
add_anomaly = st.sidebar.button("Add Anomaly Data")

if add_normal:
    st.session_state.data.append(generate_data(anomaly=False))
if add_anomaly:
    st.session_state.data.append(generate_data(anomaly=True))

# Convert session data to DataFrame
df = pd.DataFrame(st.session_state.data)

if not df.empty:
    # Display raw data
    st.subheader("📊 Reservoir Data")
    st.dataframe(df)

    # Plot reservoir data trends
    fig = px.line(df, x="timestamp", y=["pressure", "temperature", "flow_rate"], markers=True, title="Reservoir Data Over Time")
    st.plotly_chart(fig, use_container_width=True)

    # Initialize AI agents
    anomaly_agent = AnomalyDetectionAgent(model_name="deepseek-r1:1.5b")
    recommendation_agent = RecommendationAgent()

    # Run anomaly detection & recommendations
    st.subheader("🚨 Anomaly Detection & Recommendations")
    results = []

    for _, row in df.iterrows():
        anomaly_result = anomaly_agent.detect_anomaly(row)
        recommendation = recommendation_agent.generate_recommendation(anomaly_result)

        result_entry = {
            "timestamp": row["timestamp"],
            "status": anomaly_result["status"],
            "details": anomaly_result["details"],
            "recommendation": recommendation
        }
        results.append(result_entry)

        # Display results dynamically in UI
        if anomaly_result["status"] == "Anomaly":
            st.error(f"⚠️ {result_entry['details']}")
            st.warning(f"🔹 Recommendation: {result_entry['recommendation']}")
        else:
            st.success(f"✅ {result_entry['details']}")

    # Display all results in a table
    if results:
        results_df = pd.DataFrame(results)
        st.dataframe(results_df)

# Sidebar instructions
st.sidebar.markdown("""
### ℹ️ Instructions:
- Click "Add Normal Data" to simulate normal readings.
- Click "Add Anomaly Data" to test anomaly detection.
- View results in real-time below.
""")
