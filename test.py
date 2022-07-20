from tokenize import String
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import password

url = f'postgresql://postgres:{password}@localhost:5432/final_project'
# engine = create_engine(url)
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.debug = True
db = SQLAlchemy(app)

class matches(db.Model):
    __tablename__ = "matches_final"
    id = db.Column(db.Integer(), primary_key=True)
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


# @app.route("/data", methods=['GET'])
# def getMatchData():
#     alldata = matches_final.query.all()
#     output = []
#     for match in alldata:
#         curr