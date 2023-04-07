#!usr/bin/python3
"""Endpoint to return the status of the Api"""
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from Backend import Storage
from API.v1.views import app_views
from os import environ as env

app = Flask(__name__)
app.register_blueprint(app_views)
cors= CORS(app, origins=["0.0.0.0"])

@app.teardown_appcontext
def teardown_app(exception):
    """ closes the database request after requests"""
    Storage.close()


@app.errorhandler(404)
def error_notfound(error):
    """returns an error code 404 if wrong url"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    host = env.get("APP_API_HOST", "0.0.0.0")
    port = int(env.get("APP_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)

