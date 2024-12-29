import serial
import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    return jsonify({
        "data": "data"
    })