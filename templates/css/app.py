from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle


app = Flask(__name__)
app = Flask(__name__, static_folder="templates")

filename = 'finalized_model.sav'
filename_minmax ='min_max_scalar.sav'
encoder.classes_ = 'team.npy'
encoder.classes_2 = 'opponent.npy'

def calculate_outcomes(day, venue, xg, xga, team, opponent):
    labelEncoderFile = np.load(open(encoder.classes_, 'rb'))
    team = labelEncoderFile.transform([[team]]) 
    team = team[0]

    labelEncoderFile = np.load(open(encoder.classes_2, 'rb'))
    opponent = labelEncoderFile.transform([[opponent]]) 
    opponent = opponent[0]

    MinMaxScalerFile = pickle.load(open(filename_minmax, 'rb'))
    otherFeatures = MinMaxScalerFile.transform([[day, venue, xg, xga]]) 
    day = otherFeatures.day[0][0]
    venue = otherFeatures.venue[0][1]
    xg = otherFeatures.xg[0][2]
    xga = otherFeatures.xga[0][3]

    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict([[day, venue, xg, xga, team, opponent]])

    return result[0]


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/dashboards")
def visuals():
    return render_template('dashboards.html')

@app.route("/machinelearning", methods=['GET', 'POST'])
def streambyte():
    # your file processing code is here...
    if request.method=='POST':
        team = request.form['team']
        opponent = request.form['opponent']
        venue = request.form['venue'] 
        day = request.form['day']
        xg = request.form['xg']
        xga = request.form['xga']
        
        bmi = calculate_outcomes(day, venue, xg, xga, team, opponent)

        return render_template('machinelearning.html',  result = bmi)
    
    else:
        return render_template('machinelearning.html')


if __name__ == '__main__':
   app.run(debug = True)