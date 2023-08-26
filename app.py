from flask import Flask, render_template, request
import alignment as al
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
    data = request.files['sequence'].stream.read().decode('UTF-8')
    objs = al.readsequences(data)
    arr = al.align("NW", [objs[0].getSequence(), objs[1].getSequence()])
    path = al.pathTracing(arr)

    print(arr, path)
    return render_template("results.html")


if __name__ == '__main__':
    app.run(debug = True)
