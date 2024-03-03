#This API will return a list of all the common food items that meet the specified food criteria.
import requests
import simplejson as json
import pandas as pd

from flask import Flask, jsonify, request

app = Flask(__name__)
df = pd.read_csv("calories.csv")
calList = df["Cals_per100grams"].tolist()
foodList = df["FoodItem"].tolist()
calList = [string.replace(" cal", "") for string in calList]
calList = list(map(int, calList))

NoteDict = {"A1": {"Title": "Hello World"}}

@app.route('/')
def index():
    return jsonify({"message": "hello world"})


#@app.route('/calories')
#def calories():
#    calorieCount = int(request.args.get('calories'))
#    healthyFoods = {"Food name": "Calories"}
#    for i  in range(len(calList)):
#        if(calList[i] <= calorieCount):
#            healthyFoods.update({foodList[i]:calList[i]})
#    return jsonify(healthyFoods)


@app.route('/getNote')
def getNote():
    noteID = request.args.get('noteID')
    return jsonify(NoteDict.get(noteID))


@app.route('/putNote')
def putNote():
    noteID = request.args.get('noteID')
    noteTitle = request.args.get('noteTitle')
    noteText = request.args.get('noteText')
    output = {noteID: {noteTitle : noteText}}
    NoteDict.update(output)
    return "Added Note"



if __name__ == "__main__":
    app.run()
