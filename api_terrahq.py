import pandas as pd
from flask import Flask, jsonify,request
from flask import render_template
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
import os
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>API para TERRAHQ</h1><p>Ésta es una API.</p>"


if __name__ == '__main__':
    app.run(debug=True)
