# 🌍 Human Development Index (HDI) Predictor

A Machine Learning web application that predicts the Human Development Index (HDI) of a country using socio-economic indicators such as Life Expectancy, Mean Years of Schooling, Gross National Income (GNI) per Capita, and Internet Users.

## 📌 Project Overview

The Human Development Index (HDI) is a statistical measure developed by the United Nations to assess the overall development of countries. This project uses a Linear Regression Machine Learning model to predict the HDI score based on key development indicators.

The application is built using Python, Flask, Scikit-learn, Pandas, and NumPy.

---

## 🚀 Features

- Predicts Human Development Index (HDI)
- User-friendly Flask web interface
- Machine Learning model using Linear Regression
- Data preprocessing and visualization
- Displays HDI category:
  - Low HDI
  - Medium HDI
  - High HDI
  - Very High HDI

---

## 🛠 Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Pickle
- HTML
- CSS

---

## 📂 Project Structure

```
HDI-PREDICTOR
│
├── Dataset
│   └── HDI.csv
│
├── Flask
│   ├── app.py
│   ├── HDI.pkl
│   └── templates
│       ├── home.html
│       ├── indexnew.html
│       └── resultnew.html
│
├── Training
│   └── HumDevIndex.ipynb
│
├── requirements.txt
└── README.md
```

---

## 📊 Input Features

- Country
- Life Expectancy
- Mean Years of Schooling
- Gross National Income (GNI) per Capita
- Internet Users

---

## 🎯 Output

The application predicts:

- HDI Score
- HDI Category
  - Low HDI
  - Medium HDI
  - High HDI
  - Very High HDI

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/rapururishik9-dev/HDI-PREDICTOR.git
```

Move into the project folder

```bash
cd HDI-PREDICTOR
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
cd Flask
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

## 📈 Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Exploratory Data Analysis
4. Handle Missing Values
5. Train-Test Split
6. Train Linear Regression Model
7. Save Model using Pickle
8. Build Flask Web Application
9. Predict HDI

---

## 📌 Future Improvements

- Improve prediction accuracy using advanced ML algorithms
- Deploy on Render or Railway
- Add interactive charts
- Improve UI/UX
- Add more socio-economic indicators

---

## 👨‍💻 Author

**Rishik R**

GitHub:
https://github.com/rapururishik9-dev

---

## 📜 License

This project is developed for educational purposes as part of the SmartBridge Machine Learning program.