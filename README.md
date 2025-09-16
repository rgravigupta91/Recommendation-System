# pes_mtech_group_3
 
## 🔮 Customer360: Turning Data into Insights for Digital Excellence using Recommendation System

A machine learning-powered recommendation engine combining collaborative, content-based, and deep learning techniques to deliver highly personalized results. This project supports hybrid strategies using traditional ML and state-of-the-art NLP models like BERT, with a full-stack deployment pipeline.

---

## 📌 Project Overview

This system is designed to provide personalized recommendations to users based on both their behavior and item attributes. It uses:

- 📊 Collaborative Filtering (KNN, SVD)
- 🧾 Content-Based Filtering (TF-IDF + Cosine)
- 🧠 Deep Learning (Neural Collaborative Filtering, BERT Embeddings)
- 🔄 Hybrid Models combining traditional and deep learning approaches

---

## 🏗 Architecture

```
📂 1. Data Sources
   ├─ User Logs
   ├─ Item Metadata
   ├─ User Profiles
   └─ External Datasets (Kaggle, OpenML)

🔄 2. Data Ingestion
   ├─ CSV / SQL Loaders
   ├─ Real-time Collectors (Firebase / Kafka)
   └─ Python ETL Scripts

💾 3. Data Storage
   ├─ Raw Storage (AWS S3, Google Drive)
   ├─ Structured DB (PostgreSQL / MongoDB)
   └─ Feature Store (for model training & inference)

🧹 4. Preprocessing
   ├─ Data Cleaning & Null Handling
   ├─ Encoding Categorical Variables
   ├─ TF-IDF Vectorization, Word Embeddings (Word2Vec/BERT)
   └─ Train-Test Splits

🧠 5. Modeling
   ├─ User-Based KNN
   ├─ Matrix Factorization (SVD)
   ├─ TF-IDF + Cosine Similarity
   ├─ Neural Collaborative Filtering (NCF)
   ├─ BERT + FAISS Retrieval
   └─ Hybrid Fusion (NCF + BERT)

🧪 6. Evaluation
   ├─ RMSE for error measurement
   ├─ Precision@K & Recall@K for ranking quality
   └─ Offline Testing + Real-time Logging

🌐 7. Backend API
   ├─ Built with FastAPI / Flask
   ├─ Exposes endpoints for predictions & feedback
   └─ Connects models to frontend

💻 8. Frontend UI
   ├─ Built with React.js
   ├─ Interactive Dashboard
   └─ View Top-N Recommendations

🔁 9. Feedback Loop
   ├─ Collects user interaction data (clicks, purchases)
   ├─ Updates dataset periodically
   └─ Triggers retraining pipelines
```

---

## 📈 Model Performance Summary

| Model                      | RMSE | Precision@10 | Recall@10 |
|---------------------------|------|---------------|------------|
| User-Based KNN            | 1.12 | 0.21          | 0.14       |
| Matrix Factorization (SVD)| 0.98 | 0.28          | 0.19       |
| Content-Based (TF-IDF)    | 1.05 | 0.25          | 0.18       |
| Neural CF (NCF)           | 0.89 | 0.33          | 0.24       |
| BERT + FAISS              | 0.85 | 0.36          | 0.26       |
| Hybrid (NCF + BERT)       | **0.81** | **0.39** | **0.28**   |

> ✅ Hybrid models consistently outperform individual ones in both accuracy and personalization.

---

## ⚙️ Tech Stack

- **Python** (Pandas, Scikit-learn, Surprise, PyTorch/TensorFlow)
- **NLP**: BERT, HuggingFace Transformers
- **Retrieval**: FAISS for fast similarity search
- **Backend**: FastAPI / Flask
- **Frontend**: React.js
- **Database**: PostgreSQL, MongoDB, Firebase (optional)
- **Deployment**: Docker, Render, Firebase Hosting

---

## 📁 Project Structure

```
📦 recommendation-system/
├── data/                  # Raw and processed data
├── models/                # Trained models and embeddings
├── notebooks/             # Exploratory Jupyter notebooks
├── api/                   # FastAPI/Flask backend
├── frontend/              # React frontend app
├── utils/                 # Preprocessing, evaluation tools
└── requirements.txt       # Python dependencies
```

---

## 🚀 Getting Started

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/recommendation-system.git
   cd recommendation-system
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the models** (optional pre-trained models included):
   ```bash
   python train.py --model knn
   ```

4. **Run the backend**:
   ```bash
   uvicorn api.main:app --reload
   ```

5. **Launch the frontend**:
   ```bash
   cd frontend
   npm install && npm start
   ```

---

## 📬 Feedback & Improvements

We value feedback! Please [open an issue](https://github.com/your-username/recommendation-system/issues) or submit a pull request if you'd like to contribute.
