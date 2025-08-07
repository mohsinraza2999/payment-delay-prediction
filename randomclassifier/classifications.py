from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from db.database import user_collection,get_users
import schemas
p_data=pd.read_csv("default.csv")
p_data=p_data.drop(index=0,axis=0)
y=p_data['Y']
X=p_data.drop(columns='Y')

X_tr,X_t,y_tr,y_t=train_test_split(X,y,test_size=0.2,random_state=42)

r_c_model=RandomForestClassifier(n_estimators=50,random_state=42)
m_details=r_c_model.fit(X_tr,y_tr)
c_y_pre=r_c_model.predict(X_t)

def random_model(history):
    pre=r_c_model.predict(history)
    return int(pre[0])


def randomforest_model():
    user_details=[]
    #user=get_users()      for dummy database
    user=user_collection.find()
    for key in user.keys():
        numbers = list(user[key].values())
        c_numbers=np.array(numbers)
        c_numbers=c_numbers.reshape(1,-1)

        y=random_model(c_numbers)
        user_details.append(make_dict(y,numbers,key))


    return user_details


def make_dict(pre_y:int, num,name):
    u_dict=schemas.Predict(name=name,balance=num[1],gender="male" if num[4]==1 else "female",
                           age=num[5],default='yes' if pre_y==1 else 'no',
                           summary= f"On the predicted data the user may be { 'a' if pre_y== 1 else 'not a' } defaulter")
    return u_dict.dict()

