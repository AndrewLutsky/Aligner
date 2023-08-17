from flask import Flask, render_template, request
import faread as fr
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
    objs = fr.readsequences(data.read())
    for seq in objs:
        print(seq.seq)
    return render_template("results.html")


if __name__ == '__main__':
    app.run(debug = True)
