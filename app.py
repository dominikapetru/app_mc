from flask import Flask, request, jsonify
app = Flask(__name__)
# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Hola Laia!!</h1>"
