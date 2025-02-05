# energyai-poc/agents/recommendation_agent.py
import subprocess

class RecommendationAgent:
    def __init__(self, model_name="deepseek-r1:1.5b"):
        self.model_name = model_name

    def generate_recommendation(self, anomaly_result):
        # If no anomaly, return a normal message
        if anomaly_result["status"] == "Normal":
            return "System is operating normally. No action required."

        # Prepare the prompt for DeepSeek LLM
        prompt = f"""
        Based on the detected anomaly, suggest a mitigation action:

        Anomaly Details:
        {anomaly_result["details"]}

        Provide a recommended action in a clear and concise manner.
        """

        # Send prompt to DeepSeek LLM via Ollama
        try:
            result = subprocess.run(
                ["ollama", "run", self.model_name],
                input=prompt,
                text=True,
                capture_output=True
            )
            response = result.stdout.strip()
        except Exception as e:
            response = f"Error in LLM response: {e}"

        print(f"[RecommendationAgent] LLM Recommendation: {response}")
        return response
