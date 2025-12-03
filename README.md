# 🛒 Amazon Product Recommendation System  

This project implements a **production-style Product Recommendation System** using collaborative filtering and matrix factorization (SVD). The system learns user behavior from historical ratings and recommends relevant products for any user. A real-time interactive web app is built using **Streamlit**.

The project follows an industry-style workflow including data cleaning, EDA, model training, evaluation, and deployment.

---

## 🧠 Problem Statement  
E-commerce platforms must personalize recommendations to retain users, increase engagement, and improve conversions. Manual filtering is not scalable.

This project solves:

> **"How to recommend relevant products for a user based only on past behavior?"**

---

## 🔹 Dataset Columns

| Column Name | Description |
|-------------|-------------|
| UserId | Unique user identifier |
| ProductId | Unique product identifier |
| Score | User rating (1–5) |
| Time | Review timestamp |
| Summary | Short review summary |
| Text | Full review text |

---

## 🎯 Objective

Build a recommendation engine that:

✅ Learns user preferences  
✅ Handles sparse data  
✅ Provides **Top-N product recommendations**  
✅ Works like real E-commerce systems (Amazon, Netflix)  

---

## ⚙️ Tech Stack

| Layer | Technologies |
|--------|-------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Recommendation Model | SVD |
| Matrix Computation | SciPy |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit |
| Version Control | Git, GitHub |
| Serialization | Joblib |

---

## 🔄 ML Workflow

### ✅ 1. Data Cleaning  
Performed in `01_data_cleaning.ipynb`

✔ Dropped null entries  
✔ Removed duplicates  
✔ Cleaned text fields  
✔ Standardized data  
✔ Filtered invalid values  
✔ Removed extreme text lengths  

---

### ✅ 2. Exploratory Data Analysis (EDA)  
Performed in `02_eda.ipynb`

Key insights:
- Rating imbalance 
- Highly sparse user–item matrix
- Long-tail distribution
- Few users generate most activity
- Strong temporal variation

---

### ✅ 3. Model Training (SVD)  
Performed in `03_model_training.ipynb`

### ✅ 4. Model Evaluation  
Performed in `04_evaluation.ipynb`

Metrics:
- RMSE  
- MAE  

Time-based split was used to avoid leakage.

---

### ✅ 5. Top-N Recommendation Demo  
Performed in `05_top_n_recommendations.ipynb`

Allows:
- Selecting a random user  
- Predicting unseen products  
- Ranking by score  
- Showing Top-N items

---

## 🌐 Streamlit Web App

An interactive recommendation system built using Streamlit.

### Features:
✅ Choose a user  
✅ Get real-time recommendations  
✅ Clean UI  
✅ Fast inference  

---

## 👨‍💻 Author
**Girish K S**

Data Scientists

