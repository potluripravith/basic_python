# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def greet():
    return jsonify({"message": "Hello,TDD!"})
@app.route('/greet/<name>', methods=['GET'])
def greet_person(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run()