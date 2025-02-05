# energyai-poc/agents/recommendation_agent.py

class RecommendationAgent:
    def __init__(self):
        # Initialize the Recommendation Agent
        pass

    def generate_recommendation(self, anomaly_result):
        status = anomaly_result["status"]
        details = anomaly_result["details"]

        if status == "Anomaly":
            recommendation = f"ALERT: Anomaly detected! Investigate immediately. Details: {details}"
        else:
            recommendation = "System is operating normally. No immediate action required."
        
        print(f"[RecommendationAgent] Recommendation: {recommendation}")
        return recommendation