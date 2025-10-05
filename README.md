# 🍽️ Dine Rank

This project is based on the [Restaurant Dataset](https://www.kaggle.com/datasets/mohdshahnawazaadil/restaurant-dataset) from Kaggle.  
The ultimate goal of this project is to build a **Restaurant Ratings Predictor**, but at the current stage, I have completed the **Exploratory Data Analysis (EDA)**.

---

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

---

## 📌 Current Progress
✔️ Data cleaning and exploratory analysis completed.  
❌ Model building not yet started.  

The next steps will involve feature engineering and building the **Restaurant Ratings Predictor** using machine learning models.

---

## 📒 Notebook
The complete analysis is available in [`Notebook.ipynb`](./Notebook.ipynb).

---
👨‍💻 Author: **Syed Abdul Rafey Ali**  
🎯 MSc Data Science @ FAU Erlangen, Germany  
