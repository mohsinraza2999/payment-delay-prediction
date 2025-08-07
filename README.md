# 📊 Payment Delay Prediction API

This project predicts whether a credit card client will **default on payment next month**, using a machine learning model trained on the **"Default of Credit Card Clients"** dataset. The model is served as an API using **FastAPI** and deployed with **Uvicorn**, while **MongoDB Cloud** is used for storing client data and prediction results.

---

## 🚀 Tech Stack

- **Dataset**: Default of Credit Card Clients
- **ML Model**: Random Forest Classifier (for binary classification)
- **API Framework**: FastAPI
- **Server**: Uvicorn (ASGI server)
- **Database**: MongoDB Cloud (for prediction and request storage)

---

## 📂 Project Structure

payment-delay-prediction/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── model.py # Model training & loading logic
│ ├── schemas.py # Pydantic schemas for request/response
│ ├── db.py # MongoDB connection & storage logic
│ └── utils.py # Helper functions
│
├── data/
│ └── default_credit.csv # Dataset file (optional)
│
├── model/
│ └── rf_model.pkl # Trained Random Forest model
│
├── requirements.txt # Python dependencies
└── README.md # Project description



---

## 🔍 Features

- Train and save a **Random Forest** model for payment default prediction
- Predict default status via **REST API**
- **Log predictions** and input data to **MongoDB Cloud**
- Simple and fast deployment with **Uvicorn**

---

## 📈 Model Details

- **Target**: `default.payment.next.month` (1 = default, 0 = not)
- **Features**: 23 financial and demographic variables
- **Preprocessing**: Handled internally before model training

---

## 📡 API Endpoints

### `POST /predict`

Predict default status of a credit card client.

**Sample Request:**
json
{
  "LIMIT_BAL": 20000,
  "SEX": 2,
  "EDUCATION": 2,
  "MARRIAGE": 1,
  "AGE": 24,
  "PAY_0": 2,
  "PAY_2": 2,
  "PAY_3": -1,
  "PAY_4": -1,
  "PAY_5": -2,
  "PAY_6": -2,
  "BILL_AMT1": 3913,
  "BILL_AMT2": 3102,
  "BILL_AMT3": 689,
  "BILL_AMT4": 0,
  "BILL_AMT5": 0,
  "BILL_AMT6": 0,
  "PAY_AMT1": 0,
  "PAY_AMT2": 689,
  "PAY_AMT3": 0,
  "PAY_AMT4": 0,
  "PAY_AMT5": 0,
  "PAY_AMT6": 0
}

## Sample Response:

json

{
  "name": 0,
  "LIMIT_BAL": 20000,
  "SEX": male,
  "AGE": 24,
}


## 🛠 Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/yourusername/payment-delay-prediction.git
cd payment-delay-prediction


2. Install Dependencies
bash
pip install -r requirements.txt
3. Train the Model (if not already trained)
bash
python app/model.py
4. Start the API Server
bash
uvicorn app.main:app --reload


## ☁️ MongoDB Cloud Setup
Create a MongoDB Atlas account.

Set up a new cluster and create a database + collection.

Obtain your connection string (Mongo URI).

Add it to your environment or use a .env file:

.env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/dbname

## ✅ Future Improvements
Add model versioning

Implement user authentication

Add logging and monitoring

Develop a front-end dashboard

## 📄 License
This project is licensed under the MIT License.

## 👨‍💻 Author
Mohsin Raza
Open to contributions, feedback, and improvements!

yaml
---

Let me know if you'd like a `requirements.txt` sample or boilerplate FastAPI code to go with this!
