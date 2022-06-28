from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import HouseSerializer
from .models import House
import requests

# Create your views here.
"""
What I wanna do:
    - receiving data of a house settings from the frontend ( method : GET)
    - use these data to predict a price of the house
    - post the price to the frontend (POST)
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from django.templatetags.static import static
from django.conf import settings
import os

@api_view(['POST','GET'])
def PredictView(request):
#receiving data of a house settings from the frontend
    if request.method == 'GET':
        return Response('')
    data = request.data
#make prediction
    price = MakePrediction(data)
    #price = 100
#return the price predicted to frontend
    return Response(price)

    
def MakePrediction(X):
    file = 'train_attempt.csv'
    fpath = os.path.join(
        settings.BASE_DIR,
        'api',
        file
    )
    data = pd.read_csv(fpath, sep=',')
    data = data[data.price != 0]
    print(data.shape)
    #data.drop(columns=['Unnamed: 0'], inplace=True)
    X_train = data.drop(columns=['price'])
    y_train =data['price']
    y_train = y_train.apply(np.log)

    #make model
    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)

    #make prediction
    print(X)
    new_list = list(X.values())
    X = np.array(new_list)
    X = X.reshape(1,-1)
    print(X)
    y_pred = model.predict(X)

    return y_pred[0] 



@api_view(['GET', 'POST'])
def SendData(request):
    print("here")
    data = {
        "add": "true", 
        "obj":{
        "result": "true",
        "test" : "true"
        }
    }
    return Response(data)
