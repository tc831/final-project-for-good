from tokenize import String
from flask import Flask, jsonify, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

import pandas as pd
import os


# engine = create_engine(url)
app = Flask(__name__)
app = Flask(__name__, static_folder="templates")



@app.route("/", methods=['POST', 'GET'])
def index():

    return render_template("index.html")
