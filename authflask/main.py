from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/api/v1/stub', methods=['GET', 'POST'])
@login_required
def stub():
    sample = {
        "LAL": 100,
        "DEN": 89
    }

    if request.method == 'GET':
        return jsonify(sample)
    else:
        return jsonify(sample)