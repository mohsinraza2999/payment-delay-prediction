from pymongo import MongoClient
from config import settings

client = MongoClient(settings.MONGO_URI)
db = client["payment_prediction"]
user_collection = db["users"]




# dummy database
db=[['tywin',1,20000,	2	,2,	1,	24,	2,	2,	-1,	-1,	-2,	-2,	3913,	3102,	689,	0,	0,	0,	0,	689,	0,	0,	0,	0],
    ['jon',2,120000,	2,	2,	1,	26,	-1,	2,	0,	0,	0,	2,	2682,	1725,	2682,	3272,	3455,	3261,	0,	1000,	1000,	1000,	0,	2000],
    ['jamie',3,90000,	2,	2,	1,	34,	0,	0,	0,	0,	0,	0,	29239,	14027,	13559,	14331,	14948,	15549,	1518,	1500,	1000,	1000,	1000,	5000]]

f_db={}
a={}
def get():
    for dbs in db:
        for count in range(0,24):
            a[f'x{count+1}']=dbs[count+1]
        f_db[dbs[0]]=a.copy()
        a.clear()
    return f_db
def get_users():
    return get()