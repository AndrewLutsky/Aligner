from flask import Flask, render_template, request
import faread
import pandas as pd
import json


app = Flask(__name__)

#app route to main page
@app.route("/")
def welcome():
    return render_template("index.html")

#app route to results page
@app.route("/results", methods = ['POST'])
def getalign():
    data = request.files['sequence']
    strdata = data.read()
    print(strdata)
    align = 0
    return render_template("results.html")


if __name__ == '__main__':
    app.run(debug = True)
