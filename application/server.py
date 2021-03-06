#!/usr/bin/python3

from flask import Flask, jsonify, request, render_template
from joblib import load
import pandas as pd
import numpy as np
import json

app = Flask(__name__)

def convert(o):
    if isinstance(o, np.int64): return int(o)  
    raise TypeError

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    body = request.json
    print(">> body")
    print(body);
    df = pd.DataFrame(body)
    model = load("../model/random_forest.joblib")
    pred = model.predict(df)
    prob = model.predict_proba(df)
    print("<< pred")
    print(list(pred))
    print("<< prob")
    print(list(prob[0]))
    return json.dumps({'pred': list(pred), 'prob': list(prob[0])}, default=convert)

if __name__ == "__main_":
    app.run()
