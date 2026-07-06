from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open("model/loan_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)


with open("model/loan_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("model/loan_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = float(request.form["age"])
    income = float(request.form["income"])
    credit_score = float(request.form["credit_score"])
    loan_amount = float(request.form["loan_amount"])
    loan_term = float(request.form["loan_term"])

    employment_status = request.form["employment_status"]

    # Encode categorical value
    employment_status = encoder.transform([employment_status])[0]

    # Create input array
    features = np.array([[
        age,
        income,
        credit_score,
        loan_amount,
        loan_term,
        employment_status
    ]])

    # Scale input
    features = scaler.transform(features)

    prediction = model.predict(features)[0]

    return render_template("result.html", prediction=prediction)



if __name__ == "__main__":
    app.run(debug=True)