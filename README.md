# 🛡️ Real-Time Credit Card Fraud Detection System (Live Demo) 

**Live Dashboard:** https://your-streamlit-app.streamlit.app  
**30-second Demo:**  
![demo](assets/demo.gif)

### 🚨 10 high-risk fraud transactions detected in the last 5 minutes

| Time                | Amount  | Probability | Action       |
|---------------------|---------|-------------|--------------|
| 2025-04-05 14:32:21 | $1,847 | 98.7%       | ⚠️ BLOCKED   |
| 2025-04-05 14:31:10 | $0.99  | 96.2%       | ⚠️ BLOCKED   |

### Architecture
![Architecture](assets/architecture.png)

### Features
- Real-time streaming with Kafka + Confluent Cloud (free)
- LightGBM model (F1 = 0.92 on test, AUC = 0.99)
- PySpark + Delta Lake on Databricks Community Edition
- Live dashboard with fraud alerts + Slack notifications
- Model drift detection + backtesting
- CI/CD + unit tests + Great Expectations
- 100% free forever

### Tech Stack (all free)
Databricks · Kafka · LightGBM · Streamlit · FastAPI · Redis · MLflow · GitHub Actions

---
⭐ Star this repo if you want more senior-level free projects!
