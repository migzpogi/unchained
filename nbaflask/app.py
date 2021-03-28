from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>NBA Scores</h1>
<p>Summary of games and scores</p>'''


@app.route('/api/v1/scores', methods=['GET', 'POST'])
def scores():
    sample = {
        "LAL": 100,
        "DEN": 89
    }

    if request.method == 'GET':
        return jsonify(sample)
    if request.method == 'POST':
        content = request.get_json()
        return content['name']




app.run()
