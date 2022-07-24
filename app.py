from tokenize import String
from flask import Flask, jsonify, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import password
import init_db
import pandas as pd
import os

url = f'postgresql://postgres:{password}@localhost:5432/final_project'
# engine = create_engine(url)
app = Flask(__name__)
app = Flask(__name__, static_folder="templates")

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.debug = True
db = SQLAlchemy(app)


class matches(db.Model):
    __tablename__ = "matches_final"
    index = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date(), nullable=False)
    time = db.Column(db.String(), nullable=False)
    comp = db.Column(db.String(), nullable=False)
    round = db.Column(db.String(), nullable=False)
    day = db.Column(db.String(), nullable=False)
    venue = db.Column(db.String(), nullable=False)
    result = db.Column(db.String(), nullable=False)
    gf = db.Column(db.Integer(), nullable=False) 
    ga = db.Column(db.Integer(), nullable=False)
    opponent = db.Column(db.String(), nullable=False)
    xg = db.Column(db.Float(), nullable=False)
    xga = db.Column(db.Float(), nullable=False)
    poss = db.Column(db.Float(), nullable=False)
    attendance = db.Column(db.Integer(), nullable=False)
    captain = db.Column(db.String(), nullable=False)
    formation = db.Column(db.String(), nullable=False)
    referee = db.Column(db.String(), nullable=False)
    match_report = db.Column(db.String(), nullable=False)
    sh = db.Column(db.Float(), nullable=False)
    sot = db.Column(db.Float(), nullable=False)
    dist = db.Column(db.Float(), nullable=False)
    fk = db.Column(db.Float(), nullable=False)
    pk = db.Column(db.Float(), nullable=False)
    pkatt = db.Column(db.Float(), nullable=False)
    season  = db.Column(db.Integer(), nullable=False)
    team = db.Column(db.String(), nullable=False)

    def __init__(self, date, time, comp, round, day, venue, result, gf, ga, opponent, xg, xga, poss, attendance, captain, formation, referee, match_report, sh, sot, dist, fk, pk, pkatt, season, team):
        self.date = date
        self.time = time
        self.comp = comp
        self.round = round
        self.day = day 
        self.venue = venue 
        self.result = result
        self.gf = gf
        self.ga = ga
        self.opponent = opponent 
        self.xg = xg 
        self.xga = xga
        self.poss = poss
        self.attendance = attendance 
        self.captain = captain
        self.formation = formation
        self.referee = referee
        self.match_report = match_report
        self.sh = sh
        self.sot = sot
        self.dist = dist
        self.fk = fk
        self.pk = pk 
        self.pkatt = pkatt
        self.season = season 
        self.team = team

# class upcoming_mataches(db.Model):
#     __tablename__ ="upcoming_matches_df"
#     index = db.Column(db.Integer(), primary_key=True)
#     wk = db.Column(db.Float(), nullable=False)
#     day = db.Column(db.String(), nullable=False)
#     date = db.Column(db.Date(), nullable=False)
#     time  = db.Column(db.String(), nullable=False)
#     home  = db.Column(db.String(), nullable=False)
#     away = db.Column(db.String(), nullable=False)
#     venue  = db.Column(db.String(), nullable=False)
#     mod1 = db.Column(db.String(), nullable=True)
#     mod2 = db.Column(db.String(), nullable=True)
#     mod3 = db.Column(db.String(), nullable=True)
#     mod4 = db.Column(db.String(), nullable=True)

#     def __init__(self_up, wk, day, date, time, home, away, venue, mod1, mod2, mod3, mod4):
#         self_up.wk = wk
#         self_up.day = day
#         self_up.date = date
#         self_up.time = time
#         self_up.home = home
#         self_up.away = away
#         self_up.venue = venue
#         self_up.mod1 = mod1
#         self_up.mod2 = mod2
#         self_up.mod3 = mod3
#         self_up.mod4 = mod4

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST', 'GET'])
def selection():
    if request.method=='POST':
        print(request.form)
        teamA = request.form['TeamA']
        teamB = request.form['TeamB']

        return render_template('index.html', result=teamA)
    else:
        return render_template('index.html')        

# @app.route("/", methods=['POST', 'GET'])
# def upcoming_results():
#     if request.mehod=='POST':
#         return render_template('index.html')
#     else:
#         return render_template ('index.html')

@app.route("/upcoming_matches")
def upcoming_matches():
    init_db.upcoming_matches()
    return redirect("/")

@app.route("/renew_data")
def renew_data():
    # init_db.scrape_data()
    init_db.retrieve_file()
    return redirect("/")

@app.route("/api", methods=['GET'])
def getMatchData():
    alldata = matches.query.all()
    output = []
    for match in alldata:
        dataoutput = {}
        dataoutput['date'] =  match.date
        dataoutput['time'] =  match.time
        dataoutput['comp'] =  match.comp
        dataoutput['round'] =  match.round
        dataoutput['day'] =  match.day 
        dataoutput['venue'] =  match.venue 
        dataoutput['result'] =  match.result
        dataoutput['gf'] =  match.gf
        dataoutput['ga'] =  match.ga
        dataoutput['opponent'] =  match.opponent 
        dataoutput['xg'] =  match.xg 
        dataoutput['xga'] =  match.xga
        dataoutput['poss'] =  match.poss
        dataoutput['attendance'] =  match.attendance 
        dataoutput['captain'] =  match.captain
        dataoutput['formation'] =  match.formation
        dataoutput['referee'] =  match.referee
        dataoutput['match_report'] =  match.match_report
        dataoutput['sh'] =  match.sh
        dataoutput['sot'] =  match.sot
        dataoutput['dist'] =  match.dist
        dataoutput['fk'] =  match.fk
        dataoutput['pk'] =  match.pk 
        dataoutput['pkatt'] =  match.pkatt
        dataoutput['season'] =  match.season 
        dataoutput['team'] =  match.team
        output.append(dataoutput)
    return jsonify(output)
