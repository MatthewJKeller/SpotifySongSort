import json
from flask import Flask,jsonify,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/retrieve")
def retrieve():
    with open ('top_tracks_2023.json') as f:
        tracks = json.load(f)
        return jsonify(tracks)

@app.route("/search", methods = ['POST'])
def searchProcess():
    req = request.json
    filterType = req["select"]
    offensive = req["explicit"]
    sortBy = req["sortInput"]
    searchIn = req["searchInput"]
    
    return jsonify(searchResult)
    
if __name__ == "__main__":
    app.run(debug=True)
        