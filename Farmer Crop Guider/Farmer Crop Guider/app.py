from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# ==========================
# LOAD CROP MODEL
# ==========================

crop_model = pickle.load(open("model/Crop_recommend_RandomForest", "rb"))
crop_scaler = pickle.load(open("model/Crop_scaler.pkl", "rb"))
crop_encoder = pickle.load(open("model/Crop_recommend_encoder.pkl", "rb"))

# ==========================
# LOAD FERTILIZER MODEL
# ==========================

fert_model = pickle.load(open("model/fertilizer_RandomForestClassifier", "rb"))
fert_scaler = pickle.load(open("model/fertilizer_scaler.pkl", "rb"))
encoders = pickle.load(open("model/fertilizer_encoder.pkl", "rb"))

soil_encoder = encoders["soil_encoder"]
fert_crop_encoder = encoders["crop_encoder"]
fert_encoder = encoders["encoder"]

# ==========================
# LOAD HOME PAGE
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# CROP PAGE
# ==========================

@app.route("/crop")
def crop():
    return render_template("crop.html")


# ==========================
# CROP PREDICTION
# ==========================

@app.route("/predict_crop", methods=["POST"])
def predict_crop():

    N = float(request.form["Nitrogen"])
    P = float(request.form["Phosphorus"])
    K = float(request.form["Potassium"])
    temp = float(request.form["Temperature"])
    humidity = float(request.form["Humidity"])
    ph = float(request.form["Ph"])
    rainfall = float(request.form["Rainfall"])

    data = np.array([[N, P, K, temp, humidity, ph, rainfall]])

    data = crop_scaler.transform(data)

    prediction = crop_model.predict(data)

    crop_name = crop_encoder.inverse_transform(prediction)[0]

    return render_template(
        "result.html",
        title="🌾 Crop Recommendation",
        prediction=crop_name
    )


# ==========================
# FERTILIZER PREDICTION
# ==========================
@app.route("/fertilizer", methods=["GET", "POST"])
def fertilizer():

    if request.method == "POST":

        temperature = float(request.form["temperature"])
        moisture = float(request.form["moisture"])
        rainfall = float(request.form["rainfall"])
        ph = float(request.form["ph"])
        nitrogen = float(request.form["nitrogen"])
        phosphorous = float(request.form["phosphorous"])
        potassium = float(request.form["potassium"])
        carbon = float(request.form["carbon"])
        soil = soil_encoder.transform([request.form["soil"]])[0]
        crop = fert_crop_encoder.transform([request.form["crop"]])[0]

        data = np.array([[temperature, moisture, rainfall, ph, nitrogen,
                           phosphorous, potassium, carbon, soil, crop]])

        data = fert_scaler.transform(data)
        prediction = fert_model.predict(data)
        fert_name = fert_encoder.inverse_transform(prediction)[0]

        return render_template(
            "fertilizer.html",
            prediction=fert_name,
            soils=soil_encoder.classes_,
            crops=fert_crop_encoder.classes_,
        )

    return render_template(
        "fertilizer.html",
        soils=soil_encoder.classes_,
        crops=fert_crop_encoder.classes_,
    )


# ==========================
# MAIN
# ==========================

if __name__ == "__main__":
    app.run(debug=True)