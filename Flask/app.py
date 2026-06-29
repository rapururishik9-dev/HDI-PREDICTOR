import numpy as np
import pandas as pd
import pickle

from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)

# Load trained model
model = pickle.load(open("HDI.pkl", "rb"))

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Prediction page
@app.route("/Prediction", methods=["GET", "POST"])
def prediction():
    return render_template("indexnew.html")

# Home button
@app.route("/Home", methods=["GET", "POST"])
def my_home():
    return render_template("home.html")

# Predict
@app.route("/predict", methods=["POST"])
def predict():

    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    features_name = [
        "Country",
        "Life expectancy",
        "Mean years of schooling",
        "Gross national income (GNI) per capita",
        "Internet users"
    ]

    df = pd.DataFrame(features_value, columns=features_name)

    output = model.predict(df)

    y_pred = round(float(output[0][0]), 2)

    if 0.3 <= y_pred <= 0.4:
        prediction = "Low HDI"

    elif 0.4 < y_pred <= 0.7:
        prediction = "Medium HDI"

    elif 0.7 < y_pred <= 0.8:
        prediction = "High HDI"

    elif 0.8 < y_pred <= 0.94:
        prediction = "Very High HDI"

    else:
        prediction = "Prediction Out of Range"

    return render_template(
        "resultnew.html",
        prediction_text=f"{prediction} : {y_pred}"
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)