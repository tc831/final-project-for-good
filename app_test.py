from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template,request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:My2F6VUd4jb@localhost:5432/final_project"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class match_data(db.Model):
    __tablename__ = 'matches_final'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String())
    time = db.Column(db.String())
    comp = db.Column(db.Integer())


    def __init__(self, date, time, comp):
        self.date = date
        self.time = time
        self.comp = comp

    def __repr__(self):
        return f"<match date {self.date}>"
    
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)