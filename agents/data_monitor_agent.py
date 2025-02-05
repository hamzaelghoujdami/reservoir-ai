# energyai-poc/agents/data_monitor_agent.py

import time
import pandas as pd

class DataMonitorAgent:
    def __init__(self, data_source):
        # Initialize the DataMonitorAgent with the data source (CSV file path)
        self.data_source = data_source

    def fetch_data(self):
        # Simulate reading data from a CSV file using pandas
        data = pd.read_csv(self.data_source)
        return data

    def stream_data(self, callback, interval=5):
        # Simulate streaming data periodically
        data = self.fetch_data()  # Fetch the entire dataset
        for index, row in data.iterrows():
            print(f"[DataMonitorAgent] Sending data: {row.to_dict()}")
            callback(row.to_dict())  # Send data to the next agent via the callback
            time.sleep(interval)    # Wait for the specified interval before sending the next data
