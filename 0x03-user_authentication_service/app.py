#!/usr/bin/env python3
"""Basic flask application module"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def message():
    """return a jsonified dictionary"""
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
