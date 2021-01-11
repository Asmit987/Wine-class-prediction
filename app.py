# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:12:21 2021

@author: Lenovo
"""


from flask import Flask, request
import pickle
import pandas as pd
import numpy as np
import flasgger
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)

pickle_file = open("Wine_GaussianNB.pkl", "rb")
Wine_quality = pickle.load(pickle_file)


@app.route('/')
def welcome():
    return "hello welcome all "

@app.route('/predict', methods=['Get'])
def predict_wine_quality():
    
    """Let's Predict the Wine Quality
    Here we are decorating ower frontend application.
    ---
    parameters:
      - name: alcohol
        in: query
        type: float64
        request: true
      - name: malic_acid
        in: query
        type: float64
        request: true
      - name:ash
        in: query
        type: float64
        request: true
      - name: alcalinity_of_ash
        in: query
        type: float64
        request: true
      - name: magnesium
        in: query
        type: float64
        request: true
      - name: total_phenols
        in: query
        type: float64
        request: true
      - name: flavanoids 
        in: query
        type: float64
        request: true
      - name: nonflavanoid_phenols
        in: query
        type: float64
        request: true
      - name: proanthocyanins
        in: query
        type: float64
        request: true
      - name: color_intensity
        in: query
        type: float64
        request: true
      - name: hue
        in: query
        type: float64
        request: true
      - name: diluted_wines 
        in: query
        type: float64
        request: true
      - name: proline 
        in: query
        type: float64
        request: true
    responses:
        200:
            description: The output values
            
    """
    alcohol           =            request.args.get("alcohol")
    malic_acid         =           request.args.get("malic_acid")
    ash           =                request.args.get("ash")
    alcalinity_of_ash     =        request.args.get("alcalinity_of_ash")
    magnesium           =          request.args.get("magnesium")
    total_phenols      =           request.args.get("total_phenols")
    flavanoids       =             request.args.get("flavanoids")
    nonflavanoid_phenols     =     request.args.get("nonflavanoid_phenols")
    proanthocyanins      =         request.args.get("proanthocyanins")
    color_intensity      =         request.args.get("color_intensity")
    hue            =               request.args.get("hue")
    diluted_wines          =       request.args.get("diluted_wines")
    proline          =             request.args.get("proline")
    prediction = Wine_quality.predict([[alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols,flavanoids,
                                     nonflavanoid_phenols, proanthocyanins, color_intensity, hue, diluted_wines, proline]])
    return "The predicted value is"+ str(prediction)




@app.route('/predict_file', methods=['POST'])
def predict_wine_quality_file():
    """Let's predict list data and check wine quality
    here we are using flasgger for frontend application.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: tyre
        
    responses:
        200:
            description: The output values
            
    """
    df_test = pd.read_csv(request.files.get('file'))
    print(df_test.head())
    prediction=Wine_quality.predict(df_test)
    return str(list(prediction))

  
    
if __name__=='__main__':
    app.run()