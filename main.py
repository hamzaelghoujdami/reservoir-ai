# energyai-poc/main.py

from agents.data_monitor_agent import DataMonitorAgent
from agents.anomaly_detection_agent import AnomalyDetectionAgent
from agents.recommendation_agent import RecommendationAgent

def recommendation_callback(anomaly_result):
    # Pass anomaly results to the Recommendation Agent
    recommendation = recommendation_agent.generate_recommendation(anomaly_result)
    print(f"[Final Recommendation] {recommendation}")

def anomaly_detection_callback(data):
    # Pass data to the Anomaly Detection Agent
    result = anomaly_agent.detect_anomaly(data)
    print(f"[Anomaly Detection Result] {result}")
    recommendation_callback(result)

if __name__ == "__main__":
    data_source = "data/reservoir_data.csv"  # Path to the sample reservoir data
    monitor_agent = DataMonitorAgent(data_source)  # Initialize the Data Monitor Agent
    anomaly_agent = AnomalyDetectionAgent()        # Initialize the Anomaly Detection Agent with deepseek-r1:1.5b
    recommendation_agent = RecommendationAgent()   # Initialize the Recommendation Agent

    # Stream data every 2 seconds, sending it to the Anomaly Detection Agent
    monitor_agent.stream_data(anomaly_detection_callback, interval=2)
