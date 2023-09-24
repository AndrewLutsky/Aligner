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
    #gets alignment after reading file
    data = request.files['sequence'].stream.read().decode('UTF-8')

    #reads sequences into objects file
    objs = al.readsequences(data)

    #creates an array using dynamic programming and NW algorithm
    arr = al.align("NW", [objs[0].getSequence(), objs[1].getSequence()])

    #backtracing of the array
    path = al.pathTracing(arr)

    print(arr)
    #uses the path of the array, the array, and the two strings to generate two alignment strings
    al1, al2 = al.getAlignment(path, objs[0].getSequence(), objs[1].getSequence())    
    return render_template("results.html", alList = [al1, al2])


if __name__ == '__main__':
    app.run(debug = True)
