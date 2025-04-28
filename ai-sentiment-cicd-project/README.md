# AI Sentiment Analysis CI/CD Project

## Overview
This project deploys a simple AI-powered Sentiment Analysis API using FastAPI. It is fully automated with Docker, Kubernetes, and GitHub Actions for CI/CD.

---

## Project Structure

- `app/`: FastAPI application and AI model
- `helm-chart/`: Kubernetes deployment and service configs
- `github-actions/`: GitHub Actions workflow for CI/CD

---

## Tech Stack

- FastAPI
- Scikit-learn
- Docker
- Kubernetes
- GitHub Actions

---

## How to Use

1. Clone the repo:
```bash
git clone https://github.com/yourusername/ai-sentiment-cicd-project.git
cd ai-sentiment-cicd-project
```

2. Build Docker image and run locally:
```bash
cd app
docker build -t sentiment-app .
docker run -p 8000:8000 sentiment-app
```

3. Access API at `http://localhost:8000/predict/?text=I love this`

4. Use Kubernetes manifests to deploy on a cluster.

---

## Author
Vamsi Krishna Bhavana