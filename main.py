from fastapi import FastAPI
from randomclassifier.classifications import randomforest_model

app=FastAPI()

@app.get("/")
def get():
    return "welcome to payment prediction"

@app.post("/predict/")
def get_history():
    
    all=randomforest_model()
    return {"Customers":all}
