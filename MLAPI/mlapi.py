#Lets create a light weight apis and dependencies

from fastapi import FastAPI
# we need to send informatin to oru api

from pydantic import BaseModel

import pickle

import pandas as pd

app = FastAPI()


class ScoringItem(BaseModel):
    # this is the type item
    # we are grabbing each fields from the ML model
    # we have four colums in the sklearn model
    # structure this in the format
    YearsAtCompany:float
    EmployeeSatisfaction: float
    Position: str
    Salary: int
    # we will send in this structure

with open( 'rfmodel.pkl', 'rb'):
    model = pickle.load(f)

@app.post('/')

#async def
#@app.get('/')
async def scoring_endpoint(item:ScoringItem):
    df = pd.DataFrmae([item.dict().values()], columns = item.dict().keys())
    yhat = model.predict(df)
    return {"prediction": int(yhat)}



