# 🌾 Farmer Guide - Crop & Fertilizer Recommendation System

A simple Machine Learning web application built using **Python, Flask, HTML, CSS, Scikit-learn, and Pandas**.

The application helps farmers by recommending:

- 🌾 Suitable Crop
- 🌱 Best Fertilizer

based on soil and weather conditions.

---

## 📌 Features

- Crop Recommendation
- Fertilizer Recommendation
- Simple User Interface
- Machine Learning Prediction
- Flask Backend
- Easy to Use

---

## 📂 Project Structure

```
FarmerGuide/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── Crop_recommend_random_model.pkl
│   ├── Crop_recommend_scaler.pkl
│   ├── Crop_recommend_encoder.pkl
│   ├── fertilizer_model.pkl
│   ├── fertilizer_scaler.pkl
│   └── fertilizer_encoder.pkl
│
├── templates/
│   ├── index.html
│   ├── crop.html
│   ├── fertilizer.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── dataset/
    ├── Crop_recommendation.csv
    └── fertilizer_recommendation.csv
```

---

## 💻 Technologies Used

- Python
- Flask
- HTML5
- CSS3
- NumPy
- Pandas
- Scikit-learn
- Pickle

---

## 📊 Machine Learning Models

### Crop Recommendation

Input Features:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH
- Rainfall

Output:

- Recommended Crop

---

### Fertilizer Recommendation

Input Features:

- Temperature
- Moisture
- Rainfall
- pH
- Nitrogen
- Phosphorous
- Potassium
- Carbon
- Soil Type
- Crop Type

Output:

- Recommended Fertilizer

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/FarmerGuide.git
```

### Move into project folder

```bash
cd FarmerGuide
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

---

## 🌐 Open in Browser

```
http://127.0.0.1:5000
```

---

## 📷 Application Pages

- Home Page
- Crop Recommendation
- Fertilizer Recommendation
- Prediction Result

---

## 🎯 Future Improvements

- Disease Prediction
- Weather Forecast Integration
- Multiple Language Support
- Market Price Prediction
- Soil Health Analysis

---

## 👩‍💻 Author

**Ishika Mehta**

Computer Science Student

---

## 📄 License

This project is developed for educational and learning purposes.