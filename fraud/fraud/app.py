from flask import Flask,render_template,request

import pickle
with open("model/scaler.pkl","rb") as f:
   encoder=pickle.load(f)

with open("model/encoders.pkl","rb") as f:
   encoder=pickle.load(f)

with open("model/kmeans.pkl","rb") as f:
   encoder=pickle.load(f)
 
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Read form values
        branch = request.form["branch"]
        time_of_day = request.form["time_of_day"]
        acct_type = request.form["Acct_type"]
        trans_type = request.form["type"]
        amount = float(request.form["amount"])

        # Prediction code here
        prediction = "Fraud"

        return render_template("index.html", prediction=prediction)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
