# energyai-poc/agents/anomaly_detection_agent.py

import subprocess
import json

class AnomalyDetectionAgent:
    def __init__(self, model_name="deepseek-r1:1.5b"):
        # Initialize the AnomalyDetectionAgent with a specific LLM model
        self.model_name = model_name

    def detect_anomaly(self, data):
        # Format the data as a prompt for DeepSeek LLM
        prompt = f"""
        Analyze the following reservoir data for anomalies:
        Timestamp: {data['timestamp']}
        Pressure: {data['pressure']} PSI
        Temperature: {data['temperature']} °C
        Flow Rate: {data['flow_rate']} L/min

        Identify if there's an anomaly based on sudden spikes/drops in values.
        Respond with 'Anomaly Detected' or 'Normal', and explain briefly.
        """

        # Use Ollama CLI to send the prompt to DeepSeek LLM
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_name],
                input=prompt,  # Send prompt as input
                text=True,
                capture_output=True
            )
            response = result.stdout.strip()
        except Exception as e:
            response = f"Error in LLM response: {e}"

        print(f"[AnomalyDetectionAgent] LLM Response: {response}")

        # Basic parsing to identify anomalies (adjust based on LLM responses)
        if "Anomaly Detected" in response:
            return {"status": "Anomaly", "details": response}
        else:
            return {"status": "Normal", "details": response}

# energyai-poc/main.py

from agents.data_monitor_agent import DataMonitorAgent
from agents.anomaly_detection_agent import AnomalyDetectionAgent

def anomaly_detection_callback(data):
    # Pass data to the Anomaly Detection Agent
    result = anomaly_agent.detect_anomaly(data)
    print(f"[Anomaly Detection Result] {result}")

if __name__ == "__main__":
    data_source = "data/reservoir_data.csv"  # Path to the sample reservoir data
    monitor_agent = DataMonitorAgent(data_source)  # Initialize the Data Monitor Agent
    anomaly_agent = AnomalyDetectionAgent()        # Initialize the Anomaly Detection Agent with deepseek-r1:1.5b

    # Stream data every 2 seconds, sending it to the Anomaly Detection Agent
    monitor_agent.stream_data(anomaly_detection_callback, interval=2)