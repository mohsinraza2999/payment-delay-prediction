 <h1>📊 Payment Delay Prediction API</h1>

  <p>
    This project predicts whether a credit card client will <strong>default on payment next month</strong>, 
    using a machine learning model trained on the <strong>"Default of Credit Card Clients"</strong> dataset. 
    The model is served as an API using <strong>FastAPI</strong> and deployed with <strong>Uvicorn</strong>, 
    while <strong>MongoDB Cloud</strong> is used for storing client data and prediction results.
  </p>

  <hr>

  <h2>🚀 Tech Stack</h2>
  <ul>
    <li><strong>Dataset:</strong> Default of Credit Card Clients</li>
    <li><strong>ML Model:</strong> Random Forest Classifier (for binary classification)</li>
    <li><strong>API Framework:</strong> FastAPI</li>
    <li><strong>Server:</strong> Uvicorn (ASGI server)</li>
    <li><strong>Database:</strong> MongoDB Cloud (for prediction and request storage)</li>
  </ul>

  <hr>

  <h2>📂 Project Structure</h2>
  <pre>
payment-delay-prediction/
├── db/
│   ├── config.py            # database configration
│   ├── database.py          # MongoDB connection & storage logic
│ 
├── dataset/
│   └── default.csv          # Dataset file (optional)
|
├── main.py                  # FastAPI entry point
├── model.py                 # Model training & loading logic
├── schemas.py               # Pydantic schemas for request/response
├── requirements.txt         # Python dependencies
└── README.md                # Project description
  </pre>

  <hr>

  <h2>🔍 Features</h2>
  <ul>
    <li>Train and save a <strong>Random Forest</strong> model for payment default prediction</li>
    <li>Predict default status via <strong>REST API</strong></li>
    <li><strong>Log predictions</strong> and input data to <strong>MongoDB Cloud</strong></li>
    <li>Simple and fast deployment with <strong>Uvicorn</strong></li>
  </ul>

  <hr>

  <h2>📈 Model Details</h2>
  <ul>
    <li><strong>Target:</strong> default.payment.next.month (1 = default, 0 = not)</li>
    <li><strong>Features:</strong> 23 financial and demographic variables</li>
    <li><strong>Preprocessing:</strong> Handled internally before model training</li>
  </ul>

  <hr>

  <h2>📡 API Endpoints</h2>
  <h3><code>POST /predict</code></h3>
  <p>Predict default status of a credit card client.</p>

  <p><strong>Sample Request:</strong></p>
  <pre>
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
  </pre>

  <p><strong>Sample Response:</strong></p>
  <pre>
{
   name: "jamie"
   balance: 20000
   gender : male
   age : 34
  "default": "no",
  "summary": "On the predicted data the user may be not a defaulter"
}
  </pre>

  <hr>

  <h2>🛠 Setup Instructions</h2>

  <h3>1. Clone the Repository</h3>
  <pre>
git clone https://github.com/mohsinraza2999/payment-delay-prediction.git
cd payment-delay-prediction
  </pre>

  <h3>2. Install Dependencies</h3>
  <pre>
pip install -r requirements.txt
  </pre>

  <h3>3. Train the Model (if not already trained)</h3>
  <pre>
python app/model.py
  </pre>

  <h3>4. Start the API Server</h3>
  <pre>
uvicorn app.main:app --reload
  </pre>

  <hr>

  <h2>☁️ MongoDB Cloud Setup</h2>
  <ol>
    <li>Create a MongoDB Atlas account.</li>
    <li>Set up a new cluster and create a database + collection.</li>
    <li>Obtain your connection string (Mongo URI).</li>
    <li>Add it to your environment or use a <code>.env</code> file:</li>
  </ol>
  <pre>
MONGO_URI=mongodb+srv://&lt;username&gt;:&lt;password&gt;@cluster0.mongodb.net/dbname
  </pre>

  <hr>

  <h2>✅ Future Improvements</h2>
  <ul>
    <li>Add model versioning</li>
    <li>Implement user authentication</li>
    <li>Add logging and monitoring</li>
    <li>Develop a front-end dashboard</li>
  </ul>

  <hr>

  <h2>📄 License</h2>
  <p>This project is licensed under the MIT License.</p>

  <hr>

  <h2>👨‍💻 Author</h2>
  <p><strong>Mohsin Raza</strong><br>
  Open to contributions, feedback, and improvements!</p>
