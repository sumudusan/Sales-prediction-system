# 📊 Smart Sales Prediction System

## 🚀 Overview

This project is a **Machine Learning-based web application** that predicts product sales and provides insights for better business decisions.

It allows users to:

* Predict future sales
* Upload their own data
* View trends using charts

---

## 🎯 Features

### 🔹 1. Sales Prediction

* Predict sales based on:

  * Price
  * Date
  * Product type

---

### 🔹 2. Smart Date Handling

* User enters only **date**
* System automatically extracts:

  * Day
  * Month
  * Day of week

---

### 🔹 3. 30-Day Forecast 🔮

* Predict sales for the **next 30 days**
* Helps businesses plan inventory

---

### 🔹 4. Data Visualization 📈

* Displays predictions using **charts (Chart.js)**
* Easy to understand trends

---

### 🔹 5. File Upload (CSV) 📁

* Users can upload their own dataset
* System:

  * Reads data
  * Trains model automatically
  * Provides insights

---

### 🔹 6. Business Insights 📊

* Shows:

  * Average sales
  * Product performance

---

## 🛠 Technologies Used

* Python
* Flask (Web Framework)
* Pandas & NumPy (Data Processing)
* Scikit-learn (Machine Learning)
* Chart.js (Visualization)
* HTML (Frontend)

---

## 🤖 Machine Learning Model

* Model: **Linear Regression**
* Input Features:

  * Price
  * Day
  * Month
  * Day of Week
  * Product (encoded)
* Output:

  * Predicted quantity sold

---

## 📁 Project Structure

```
sales-prediction/
│
├── app.py
├── sales_data.csv
├── requirements.txt
└── templates/
    └── index.html
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone <your-repo-link>
cd sales-prediction
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 📄 CSV Format (for Upload)

```
date,product,quantity_sold,price
2024-01-01,A,10,100
2024-01-02,B,8,200
```

---

## ⚠️ Limitations

* Uses small dataset (for demo)
* Model can be improved with more data
* No user authentication (yet)

---

## 🔮 Future Improvements

* Add login system
* Deploy online (Render / AWS)
* Use advanced models (Random Forest, XGBoost)
* Add dashboard with more analytics
* Multi-product support

---

## 💰 Business Potential

This system can be used for:

* Small shops
* Online sellers
* Inventory planning

Possible monetization:

* SaaS (monthly subscription)
* Freelance service

---

## 👨‍💻 Author

* Developed as a Machine Learning project
* Focused on real-world business use

---

## ⭐ Final Note

This project demonstrates:

* End-to-end ML workflow
* Real-world problem solving
* Full-stack AI development

---
