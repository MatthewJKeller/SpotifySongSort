import json
from flask import Flask,jsonify,request,render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
 
@app.route('/')
def home():
    return render_template('task.html')
 
@app.route("/retrieve")
def retrieve():
    with open ('top_tracks_2023.json') as f:
        tracks = json.load(f)
        return jsonify(tracks)
 
@app.route("/search", methods = ['POST'])
def searchProcess():
    req = request.json
    filterType = req["select"]
    explicit = req["explicit"]
    sortBy = req["sortBy"]
    searchQuery = req["searchQuery"].lower()
 
    with open ('top_tracks_2023.json') as f:
        tracks = json.load(f)
 
    #Filtering title - string search
    if filterType == "title":
        searchResults = [title for title in tracks if searchQuery in title[filterType].lower()]
        return jsonify(searchResults)
   
    #Filtering genres and artists requires filtering a list
    if filterType in ("genres", "artists"):
        searchResults = [title for title in tracks if searchQuery in title[filterType].lower()]
        return jsonify(searchResults)
 
if __name__ == "__main__":
    app.run(debug=True)