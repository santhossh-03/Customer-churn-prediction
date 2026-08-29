from flask import Flask, render_template, request
import pandas as pd
import joblib


# ============================================
# Create Flask application
# ============================================

app = Flask(__name__)


# ============================================
# Load trained model
# ============================================

model = joblib.load(
    "customer_churn_model.pkl"
)


# ============================================
# Home page
# ============================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ============================================
# Prediction route
# ============================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ------------------------------------
        # Get form values
        # ------------------------------------

        customerID = request.form["customerID"]
        gender = request.form["gender"]
        SeniorCitizen = int(
            request.form["SeniorCitizen"]
        )

        Partner = request.form["Partner"]
        Dependents = request.form["Dependents"]

        tenure = int(
            request.form["tenure"]
        )

        PhoneService = request.form["PhoneService"]
        MultipleLines = request.form["MultipleLines"]

        InternetService = request.form["InternetService"]

        OnlineSecurity = request.form["OnlineSecurity"]
        OnlineBackup = request.form["OnlineBackup"]

        DeviceProtection = request.form["DeviceProtection"]
        TechSupport = request.form["TechSupport"]

        StreamingTV = request.form["StreamingTV"]
        StreamingMovies = request.form["StreamingMovies"]

        Contract = request.form["Contract"]

        PaperlessBilling = request.form["PaperlessBilling"]

        PaymentMethod = request.form["PaymentMethod"]

        MonthlyCharges = float(
            request.form["MonthlyCharges"]
        )

        TotalCharges = float(
            request.form["TotalCharges"]
        )


        # ------------------------------------
        # Create DataFrame
        # ------------------------------------

        new_customer = pd.DataFrame({

            "customerID": [customerID],

            "gender": [gender],

            "SeniorCitizen": [SeniorCitizen],

            "Partner": [Partner],

            "Dependents": [Dependents],

            "tenure": [tenure],

            "PhoneService": [PhoneService],

            "MultipleLines": [MultipleLines],

            "InternetService": [InternetService],

            "OnlineSecurity": [OnlineSecurity],

            "OnlineBackup": [OnlineBackup],

            "DeviceProtection": [DeviceProtection],

            "TechSupport": [TechSupport],

            "StreamingTV": [StreamingTV],

            "StreamingMovies": [StreamingMovies],

            "Contract": [Contract],

            "PaperlessBilling": [PaperlessBilling],

            "PaymentMethod": [PaymentMethod],

            "MonthlyCharges": [MonthlyCharges],

            "TotalCharges": [TotalCharges]
        })


        # ------------------------------------
        # Prediction
        # ------------------------------------

        prediction = model.predict(
            new_customer
        )[0]


        # ------------------------------------
        # Probability
        # ------------------------------------

        probability = model.predict_proba(
            new_customer
        )[0][1]


        probability_percentage = round(
            probability * 100,
            2
        )


        # ------------------------------------
        # Result message
        # ------------------------------------

        if prediction == "Yes":

            result = "Customer is likely to CHURN"

            result_class = "danger"

        else:

            result = "Customer is likely to STAY"

            result_class = "success"


        # ------------------------------------
        # Send result to HTML
        # ------------------------------------

        return render_template(
            "index.html",

            prediction=prediction,

            probability=probability_percentage,

            result=result,

            result_class=result_class,

            customerID=customerID
        )


    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


# ============================================
# Run Flask
# ============================================

if __name__ == "__main__":

    app.run(
        debug=True
    )