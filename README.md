# ReservoirAI

## Overview
The **ReservoirAI** is an AI-driven system designed to monitor reservoir data, detect anomalies using DeepSeek LLM (via Ollama), and generate actionable recommendations. The solution is built using **Python**, leveraging **AG2**, **Ollama**, and **Azure AI services**.

## Architecture
The system consists of three core agents:
1. **Data Monitor Agent** - Reads and streams reservoir data periodically.
2. **Anomaly Detection Agent** - Uses DeepSeek LLM to analyze data and detect anomalies.
3. **Recommendation Agent** - Provides recommendations based on detected anomalies.

### Data Flow
1. The **Data Monitor Agent** reads reservoir data from a CSV file.
2. The data is streamed to the **Anomaly Detection Agent**, which runs anomaly detection using **DeepSeek-r1:1.5b** via Ollama.
3. If an anomaly is detected, the **Recommendation Agent** suggests actions.

### System Architecture Diagram

```mermaid
graph TD
    CSV((Reservoir CSV)) --> DMA[Data Monitor Agent]
    DMA --> ADA[Anomaly Detection Agent]
    ADA --> RA[Recommendation Agent]
    ADA <--> OLLAMA[Ollama Server]
    OLLAMA <--> DS[DeepSeek-r1:1.5b]
    
    subgraph Local["Local Environment"]
        DOCKER[Docker Container]
    end
    
    subgraph Azure["Azure Cloud"]
        AKS[Azure Kubernetes]
        BLOB[Blob Storage]
        AIF[Azure AI Foundry]
    end
    
    DMA -.-> DOCKER
    ADA -.-> DOCKER
    RA -.-> DOCKER
    
    DMA -.-> AKS
    ADA -.-> AKS
    RA -.-> AKS
    CSV -.-> BLOB
    ADA -.-> AIF
    
    style DMA fill:#FF6B6B,color:white
    style ADA fill:#FF6B6B,color:white
    style RA fill:#FF6B6B,color:white
    style OLLAMA fill:#4ECDC4,color:black
    style DS fill:#4ECDC4,color:black
    style DOCKER fill:#2C5F2D,color:white
    style Azure fill:#0078D4,color:white
    style AKS fill:#0078D4,color:white
    style BLOB fill:#0078D4,color:white
    style AIF fill:#0078D4,color:white
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- **Python 3.9+**
- **Ollama** ([Download Ollama](https://ollama.ai/download))
- **DeepSeek LLM models** (installed via Ollama)
- **AG2 framework**
- **Azure CLI** (optional, for Azure deployment)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/reservoirai.git
cd reservoirai
```

### Step 2: Set Up Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate  # Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Ollama and DeepSeek
```bash
ollama pull deepseek-r1:1.5b
ollama serve &  # Start the Ollama server
```

## Running the PoC Locally
```bash
python main.py
```
Expected output:
```
[DataMonitorAgent] Sending data: { ... }
[AnomalyDetectionAgent] LLM Response: Anomaly Detected! Pressure spike.
[Anomaly Detection Result] {'status': 'Anomaly', 'details': 'Anomaly Detected! Pressure spike.'}
[RecommendationAgent] Recommendation: ALERT: Anomaly detected! Investigate immediately.
```

## Testing the System
### 1. Test Ollama and DeepSeek Manually
```bash
ollama run deepseek-r1:1.5b "Analyze the following reservoir data for anomalies: Pressure: 1200 PSI, Temperature: 85°C, Flow Rate: 300 L/min"
```
If this returns a valid response, Ollama is working correctly.

### 2. Validate Data Flow
- Modify `data/reservoir_data.csv` with new values.
- Run `python main.py` to see if anomalies are detected and recommendations are generated.

### 3. Run the Web App for Interactive Testing
The Streamlit web app provides a UI to:
- Add normal or anomalous data.
- View reservoir trends and anomalies visually.
- Receive recommendations dynamically.

Start the Web App:
```bash
streamlit run webapp.py
```

This will launch a browser-based UI where you can:
- Click "Add Normal Data" to simulate normal reservoir conditions.
- Click "Add Anomaly Data" to introduce anomalies.
- See real-time anomaly detection results and recommendations.

## Next Steps: Deploying to Azure
- Use **Azure AI Foundry** for LLM inference instead of local Ollama.
- Store data in **Azure Blob Storage**.
- Deploy as a **containerized service** with **Azure Functions** or **Azure Kubernetes Service (AKS)**.

## Contributors
- [Hamza El-Ghoujdami]

## License
This project is licensed under the MIT License.