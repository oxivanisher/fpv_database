#!/usr/bin/env python3

# Sources Temp
# https://pythonhosted.org/Flask-JSON/
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
# https://dev.to/hackersandslackers/manage-database-models-with-flask-sqlalchemy-22n8
# https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
# https://github.com/zalando/connexion

# from flask import Flask, request
# from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask_cors import CORS
import connexion


from models import db, User, Shop, ShopInventory, Club, YTChannel

import time


app = connexion.App(__name__, specification_dir='swagger/', resolver=RestyResolver('api'))
app.add_api('fpv_db_api.yaml')

# config
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# enable connexion

# enable FlaskJson
# FlaskJSON(app)
# enable CORS
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def get_time():
    return json_response(time=time.time())


@app.route('/increment_value', methods=['POST'])
def increment_value():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force=True)
    try:
        value = int(data['value'])
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')
    return json_response(value=value + 1)


@app.route('/get_value')
@as_json
def get_value():
    return dict(value=12)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
