from pydantic import BaseModel

class Predict(BaseModel):
    name:str
    balance:float
    gender:str
    age:int
    default: str
    summary: str
