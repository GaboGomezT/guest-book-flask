from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
load_dotenv()

APP_URL = os.getenv('APP_URL')

app = Flask(__name__)
CORS(app)

cors = CORS(app, resources={
    r"/*":{
        "origin": APP_URL
    }
})
messages = []

@app.route('/messages', methods = ['GET', 'POST'])
def get_post():
    if request.method == 'GET':
        return jsonify(messages)
    if request.method == 'POST':
        text = request.get_json()
        messages.append(text)
        return text, 201


app.run(port=5000, debug=True)