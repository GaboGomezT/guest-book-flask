from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/messages', methods = ['GET', 'POST'])
def get_post():
    if request.method == 'GET':
        return jsonify(messages)
    if request.method == 'POST':
        text = request.get_json()
        messages.append(text)
        return text, 201
