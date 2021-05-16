from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from . import db
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)
basicauth = HTTPBasicAuth()

users = {
        'john': generate_password_hash("hello")
    }

@basicauth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/api/v1/stub', methods=['GET', 'POST'])
@basicauth.login_required
def stub():
    sample = {
        "LAL": 100,
        "DEN": 89
    }

    if request.method == 'GET':
        return jsonify(sample)
    else:
        return jsonify(sample)