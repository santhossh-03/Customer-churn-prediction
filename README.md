# Customer Churn Prediction

A Machine Learning web application that predicts whether a telecom customer is likely to **churn (leave the service)** based on customer information, services, contract details, and billing information.

The project uses **Logistic Regression** with a Scikit-learn preprocessing pipeline and provides a **Flask web interface** for making predictions.

---

## 🚀 Project Overview

Customer churn is an important problem for telecom companies. Identifying customers who are likely to leave can help businesses take action early and improve customer retention.

This project takes customer information as input and predicts:

* **Yes** → Customer is likely to churn
* **No** → Customer is likely to stay

The application also displays the **churn probability**.

---

## 🧠 Machine Learning Model

The project uses:

* **Logistic Regression**
* **StandardScaler** for numerical features
* **OneHotEncoder** for categorical features
* **ColumnTransformer** for preprocessing
* **Pipeline** to combine preprocessing and model

The complete trained pipeline is saved using `joblib` as:

```text
customer_churn_model.pkl
```

---

## 📊 Dataset

The project uses the **Telco Customer Churn dataset**.

The model uses customer information such as:

* Customer ID
* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

The target variable is:

```text
Churn
```

---

## 📈 Model Performance

The Logistic Regression model achieved approximately:

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 82.19% |
| Precision | 68.71% |
| Recall    | 60.05% |
| F1 Score  | 64.09% |

---

## 🏗️ Project Structure

```text
Customer-churn-prediction/
│
├── app.py
├── model_saving.py
├── customer_churn_model.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 🔄 Project Workflow

```text
Customer Input
      ↓
Flask Web Interface
      ↓
Pandas DataFrame
      ↓
Saved ML Pipeline
      ↓
Data Preprocessing
      ↓
Logistic Regression
      ↓
Churn Prediction
      ↓
Churn Probability
      ↓
Result displayed on Web Page
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Flask
* Joblib
* HTML
* CSS

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Customer-churn-prediction.git
```

### 2. Go into the project directory

```bash
cd Customer-churn-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Create the Machine Learning Model

If `customer_churn_model.pkl` is not already available, run:

```bash
python model_saving.py
```

This trains the model and creates:

```text
customer_churn_model.pkl
```

---

## ▶️ Run the Flask Application

Run:

```bash
python app.py
```

The application will start locally.

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🔮 Making a Prediction

Enter the customer's:

* Personal information
* Service information
* Contract information
* Billing information

Then click:

```text
Predict Customer Churn
```

The application displays:

```text
Customer is likely to CHURN
```

or

```text
Customer is likely to STAY
```

along with the estimated churn probability.

---

## 📌 Example

Example customer:

```text
Customer ID: TEST001
Gender: Male
Senior Citizen: No
Partner: Yes
Dependents: No
Tenure: 12 months
Phone Service: Yes
Internet Service: DSL
Contract: Month-to-month
Monthly Charges: 60
Total Charges: 720
```

The trained model predicts the customer's churn status and probability.

---

## 🎯 Project Objective

The main objective of this project is to build an end-to-end Machine Learning application that demonstrates:

1. Data preprocessing
2. Feature transformation
3. Machine Learning model training
4. Model evaluation
5. Model serialization
6. Flask integration
7. Web-based prediction

---

## 🔑 Key Features

* ✅ Machine Learning based churn prediction
* ✅ Logistic Regression model
* ✅ Automated preprocessing pipeline
* ✅ Churn probability
* ✅ Flask web application
* ✅ Responsive frontend
* ✅ Easy local deployment
* ✅ GitHub-ready project structure

---

## 👨‍💻 Author

**Santhosh**

---

## ⭐ Future Improvements

Possible future improvements include:

* Add multiple ML models
* Compare model performance
* Add interactive charts
* Add customer prediction history
* Add database integration
* Deploy the application online
* Add authentication
* Add a customer analytics dashboard

---

## 📄 License

This project is created for learning and portfolio purposes.
