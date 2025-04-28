# AI Sentiment Analysis CI/CD Project

## 📚 Overview
This project demonstrates an end-to-end MLOps and DevOps pipeline where a simple AI model for sentiment analysis is deployed via FastAPI, containerized using Docker, orchestrated with Kubernetes, and automated using GitHub Actions.

It combines AI, MLOps, and DevOps practices in one clean workflow — perfect for real-world deployment!

---

## 🛠 Tech Stack
- **FastAPI** – Web framework for serving the AI model
- **Scikit-learn** – ML model training (Naive Bayes classifier)
- **Docker** – Containerization
- **Kubernetes** – Deployment and service orchestration
- **GitHub Actions** – CI/CD automation

---

## 📂 Project Structure

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-sentiment-cicd-project.git
cd ai-sentiment-cicd-project
cd app/
docker build -t sentiment-app .
docker run -p 8000:8000 sentiment-app
http://localhost:8000/predict/?text=I love this!
{
  "text": "I love this!",
  "sentiment": "positive"
}
kubectl apply -f helm-chart/deployment.yaml
kubectl apply -f helm-chart/service.yaml

---
