import json,jsonify
from flask import Flask

app = Flask(__name__)


@app.route("/retrieve")
function retrieve():
    with open ('top_tracks_2023.json') as f:
        tracks = json.load(f)
        return jsonify(tracks)
        