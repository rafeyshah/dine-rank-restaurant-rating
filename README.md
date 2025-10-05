# 🍽️ Dine Rank

This project is based on the [Restaurant Dataset](https://www.kaggle.com/datasets/mohdshahnawazaadil/restaurant-dataset) from Kaggle.
The ultimate goal of this project is to build a Restaurant Ratings Predictor
from **India, Pakistan, Indonesia & Bangladesh**

## 📂 Dataset Description
The dataset contains detailed information about restaurants across **141 cities**.  
Key features include:
- **Restaurant Name**  
- **City**  
- **Cuisines**  
- **Average Cost for Two**  
- **Currency**  
- **Has Table booking**  
- **Has Online delivery**  
- **Aggregate rating** (from customers)  
- **Votes** (from restaurants)

---

## 🛠️ Project Workflow

## 📊 Key Insights from My Analysis

1. **City-wise Cost**
   - The **average cost for two people** is **very high in the top 4 cities**:
     - Jakarta
     - Tangerang
     - Bogor
     - Bandung  
   - After these cities, the average cost **decreases significantly** and stays relatively constant for the rest of the 141 cities.

2. **Ratings vs Cost**
   - **Aggregate Ratings** are generally **higher where the Average Cost is lower**.  
   - Similarly, **Votes are higher** in restaurants where the Cost is lower.

3. **Zero Votes Observation**
   - In cases where restaurants reported **0 Votes (from restaurants)**, the **Aggregate Ratings (from customers)** mostly lie **between 3 to 5 stars**.  
   - This trend holds true for the **majority of the dataset**.

4. **Online Delivery**
   - A significant majority (about **3/4 of restaurants**) **do not offer online delivery**.

5. **Rating Distribution**
   - Most ratings are categorized as **Average**.  
   - **Excellent** and **Poor** ratings are comparatively rare.


## 📈 Feature Engineering and Model Preparation

After completing the exploratory data analysis, the next step involved **Feature Engineering** to prepare data for the predictive model.

### 🔹 Input Features (X)
For training, the following input features were selected based on their importance in influencing restaurant ratings:

1. **Average Cost for Two** – Represents the cost of dining; pricing directly impacts user satisfaction and hence ratings.  
2. **Has Table Booking** – Indicates whether users can book tables; lack of this option can negatively affect ratings.  
3. **Has Online Delivery** – Reflects delivery availability; restaurants without delivery often receive lower user satisfaction.  
4. **Price Range** – Categorized from cheapest to most expensive; influences both cost perception and overall experience.

### 🔹 Output Variable (y)
- **Aggregate Rating**  
  Since this is a **regression task**, the target variable is continuous, representing the average rating given by customers.

### 🔹 Encoding and Scaling
Out of the four input features:
- Two features (`Has Table Booking` and `Has Online Delivery`) are **categorical**, so they were **converted into numeric form** using `LabelEncoder`.  
- After encoding, **scaling** was applied to all features to bring them to a common range, ensuring better model performance.

This preprocessing step lays the foundation for training and evaluating the **Restaurant Ratings Predictor**.

## 📊 Model Performance Comparison

| Model Name | MAE ↓ | MSE ↓ | Remarks |
|:------------|:------:|:------:|:--------|
| Linear Regression | 0.399 | 0.5000 | Baseline model |
| Support Vector Regressor | 0.3877 | 0.4946 | Slight improvement with non-linear kernel |
| Decision Tree Regressor | 0.3610 | 0.4568 | Handles non-linear relations well |
| **Random Forest Regressor** | **0.3600** | **0.4552** | ✅ **Best performance overall** |
| K Nearest Neighbor | 0.3800 | 0.4830 | Performs decently on local similarity patterns |
| AdaBoost Regressor | 0.3700 | 0.4660 | Ensemble method, better than single trees |

### 🏆 Best Model: Random Forest Regressor

The **Random Forest Regressor** achieved the **lowest MAE (0.3600)** and **lowest MSE (0.4552)**, indicating it provides the most accurate and consistent predictions for restaurant ratings.  

Random Forest combines multiple decision trees, reducing overfitting and improving generalization — which explains its superior performance in this dataset.

### 🔍 Key Takeaways

- All models perform reasonably well, but **ensemble methods** (like Random Forest and AdaBoost) outperform single learners.  
- The **gap between MAE and MSE** across models is small, showing stable predictions without extreme errors.  
- Random Forest will be used as the **final model** for deployment and further fine-tuning.

---

## 📌 Current Progress
✔️ Data cleaning and exploratory analysis completed.  
✔️ Feature engineering and preprocessing completed.  
✔️ Model training and evaluation.
❌ Deployment in progress.

---

## 📒 Notebook
The complete analysis is available in [`Notebook.ipynb`](./Notebook.ipynb).

---
👨‍💻 Author: **Syed Abdul Rafey Ali**  
🎯 MSc Data Science @ FAU Erlangen, Germany  
