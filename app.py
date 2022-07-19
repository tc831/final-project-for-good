import psycopg2
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
con = psycopg2.connect(database="final_project", user="postgres", password="My2F6VUd4jb", host="localhost", port="5432")
cursor = con.cursor()

@app.route("/", methods=['post', 'get'])
def index():  
    cursor.execute("select * from matches_final")
    results = cursor.fetchall()
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

