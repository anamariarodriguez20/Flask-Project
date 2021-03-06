# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
@author: Ana Maria Rodriguez
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("home.html")

#only for testing, not relevant to website
@app.route("/1006")
def test():
    return render_template("index.html")

#classes page
@app.route("/classes")
def classes():
    return render_template("classes.html")

#assignments page
@app.route("/assignments")
def assign():
    return render_template("assignments.html")

#start the server
if __name__ == "__main__":
    app.run()