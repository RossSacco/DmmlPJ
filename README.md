# 🩺 Behavioral Drivers of Diabetes – Predicting Risk from Lifestyle Data
 
![Python](https://img.shields.io/badge/python-3.10+-blue)  
[📎 Project Report (PDF)](Sacco_dmml_documentation.pdf)

> A machine learning approach to early diabetes risk detection using real-world lifestyle and behavioral data.

---

## 🚀 Project Overview

Diabetes is a growing health crisis. What if we could predict a person’s diabetes risk based only on their lifestyle and behavioral habits?

This project leverages a large-scale health survey dataset to **predict diabetes risk** through:
- 🧠 **Machine learning models**
- 🧪 **Behavioral & clinical indicators**
- 🛠️ **Feature engineering**
- 🧬 **Explainable AI**
- 💻 A **user-friendly interface** to test risk in real time

> 📍 Dataset: [CDC BRFSS](https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system)

---

## 📊 Data & Features

The dataset contains over **430,000 records** and 300+ features, covering:

- **Demographics**: age, sex, education, income  
- **Health**: BMI, mental & physical health, chronic conditions  
- **Lifestyle**: smoking, alcohol, diet, physical activity  
- **Healthcare access**: insurance, cost barriers, check-ups

🧼 **Cleaning & Standardization**:
- Removed noisy/redundant columns
- Mapped response codes and fixed missing values
- Engineered interpretable features like `NutritionScore`, `Sedentary`, `LowAccess`, and `RiskyBehavior`

---

## 🤖 Modeling Approach

### ✅ Final Objective: **Binary Classification** (Diabetes vs No Diabetes)

Despite initial efforts for multiclass prediction (including PreDiabetes), class imbalance made it unreliable. Focus shifted to **early binary detection**.

### 🛠️ Pipeline Components:
- Imputation (median / most frequent)
- One-hot encoding (nominal), ordinal encoding (ranked features)
- StandardScaler normalization
- Custom feature engineering

### 🔍 Models Evaluated:
- Logistic Regression (**chosen for its high recall**)
- XGBoost, CatBoost
- Random Forest, KNN, Naive Bayes, AdaBoost

---

## 🧠 Key Results

| Model               | Accuracy | Precision | Recall | AUC     |
|--------------------|----------|-----------|--------|---------|
| **Logistic Regression** | 0.75     | 0.47      | **0.78** | 0.76    |
| XGBoost             | 0.82     | 0.66      | 0.47   | **0.86** |
| CatBoost            | 0.83     | 0.66      | 0.47   | **0.86** |

> 📌 **Recall was prioritized**: catching as many diabetic individuals as possible is critical for early intervention.

---

## 🧩 Feature Importance (Top 5)

1. **BMI Category**  
2. **General Health Rating**  
3. **Fruit & Veg Intake**  
4. **Physical Activity**  
5. **Smoking Status**

> 🔍 Full analysis and interpretation available in the [project report](Sacco_dmml_documentation.pdf).

---

## 🖥️ User Interface

A simple interactive web app was developed to allow users to:
- Input their health & lifestyle info
- Instantly receive a risk prediction (Diabetes / No Diabetes)

---

