#Example of fetching data from OpenAI API
from openAI 
import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"message": "hello world"})

if __name__ == "__main__":
    app.run()
