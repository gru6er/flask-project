from flask import json, jsonify
from app import app
from app import db
from app.models import Menu
import os

@app.route('/')
def home():
	my_env_variable = os.environ.get('APP_ENV', 'Default Value')
	return jsonify({ "status": "ok", "env_variable": my_env_variable })
@app.route('/menu')
def menu():
    today = Menu.query.first()
    if today:
        body = { "today_special": today.name }
        status = 200
    else:
        body = { "error": "Sorry, the service is not available today." }
        status = 404
    return jsonify(body), status
