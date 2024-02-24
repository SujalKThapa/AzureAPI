#Will require an OpenAI API key, which you can get from the website itself.
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
