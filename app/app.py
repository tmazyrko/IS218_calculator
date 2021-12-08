""" Flask web app """
from flask import Flask, request
from flask import render_template
from calc.calculator import Calculator
app = Flask(__name__)

@app.route("/")
def index():
    """ index route response """
    return render_template('index.html')
