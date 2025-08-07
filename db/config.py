import os
#from dotenv import load_dotenv

#load_dotenv()

class Settings:
    PROJECT_NAME: str = "Payment Prediction App"
    MONGO_URI=os.getenv("MONGO_URI")

settings = Settings()