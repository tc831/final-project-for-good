from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle
import init_db

app = Flask(__name__)
app = Flask(__name__, static_folder="templates")

# Postgres connection

from sqlalchemy import create_engine
from config import password

url = f'postgresql://postgres:{password}@localhost:5432/final_project'
engine = create_engine(url)




# filename = 'finalized_model.sav'
# filename_le = 'label_encoder.sav'
# filename_minmax ='min_max_scalar.sav'

# def calculate_bmi(gender,height,weight):
#     labelEncoderFile = pickle.load(open(filename_le, 'rb'))
#     gender = labelEncoderFile.transform([[gender]]) 
#     gender = gender[0]

#     MinMaxScalerFile = pickle.load(open(filename_minmax, 'rb'))
#     height_weight = MinMaxScalerFile.transform([[height,weight]]) 
#     height = height_weight[0][0]
#     weight = height_weight[0][1]

#     loaded_model = pickle.load(open(filename, 'rb'))
#     result = loaded_model.predict([[gender,height,weight]])

#     return result[0]


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/fetch_data")
def fetch_files():
    matches_final = init_db.retrieve_file()

    return redirect("/")

@app.route("/dashboards")
def visuals():
    return render_template('dashboards.html')

@app.route("/machinelearning", methods=['GET', 'POST'])
def streambyte():
    # your file processing code is here...
    if request.method=='POST':
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        
        bmi = calculate_bmi(gender,height,weight)

        return render_template('machinelearning.html',  result = bmi)
    
    else:
        return render_template('machinelearning.html')


if __name__ == '__main__':
   app.run(debug = True)

