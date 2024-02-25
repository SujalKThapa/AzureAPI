#This API will return a list of all the common food items that meet the specified food criteria.
import requests
import json
import pandas

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"message": "hello world"})


@app.route('/calories')
def calories():
    calorieCount = request.args.get('calories')
    return jsonify({"message": calorieCount})

if __name__ == "__main__":
    app.run()
