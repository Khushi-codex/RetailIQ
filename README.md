# 🛒 RetailIQ - End-to-End Retail Sales Prediction System

RetailIQ is a full-stack Machine Learning + Data Engineering project that predicts retail sales and provides analytics dashboards using FastAPI, Streamlit, PostgreSQL, and Docker.

---

## 🚀 Project Overview

This project demonstrates a complete production-like ML pipeline:

- Data ingestion (CSV → PostgreSQL)
- Feature engineering & ML model training
- REST API using FastAPI
- Interactive dashboard using Streamlit
- Containerized deployment using Docker

---

## 🧠 Machine Learning Model

- Algorithm: RandomForestRegressor
- Features:
  - store
  - item
  - date features (year, month, day, weekday, etc.)
- Target: sales

### Performance
- MAE: ~7–9
- RMSE: ~10–12
- R² Score: ~0.90+

---

## 🏗️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL

### ML
- Scikit-learn
- Pandas
- Joblib

### Frontend
- Streamlit

### DevOps
- Docker
- Docker Compose
  ---

## 📁 Project Structure


retailiq/
│
├── api/ # FastAPI backend
├── dashboard/ # Streamlit UI
├── database/ # PostgreSQL connection & models
├── data/ # Dataset (ignored in git)
├── model/ # Trained ML model (ignored in git)
├── notebooks/ # EDA + training notebooks
├── tests/ # API tests
├── test_connection.py # DB connectivity test
│
├── .devcontainer/ # Dev Container setup
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env (ignored)
├── .gitignore
└── README.md

---
# ⚙️ Setup Instructions

## 1️⃣ Clone Repository
```bash
git clone https://github.com/Khushi-codex/retailiq.git

cd retailiq
