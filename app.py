import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'go_playground'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

#creating new instance of PyMongo and adding the app object with constructor method
mongo = PyMongo(app)

@app.route('/')
@app.route('/find_playground')
def find_playground():
    return render_template("playground.html", 
                            playgrounds = mongo.db.playgrounds.find())
    
# @app.route('/add_playground')
# def add_playground():
#     _boroughs = mongo.db.boroughs.find()
#     borough_list = [borough for borough in _boroughs]
#     return render_template("addplayground.html", boroughs = borough_list) 
                            
@app.route('/add_playground')
def add_playground():
    return render_template("addplayground.html", 
                            boroughs = mongo.db.boroughs.find()) 
                            
@app.route('/insert_playground', methods=['POST'])
def insert_playground():
    playgrounds = mongo.db.tasks
    playgrounds.insert_one(request.form.to_dict())
    return redirect(url_for('show_playground'))                            

@app.route('/show_playground')
def show_playground():
    return render_template("showplayground.html", 
                            playgrounds = mongo.db.playgrounds.find())

# @app.route('/')
# @app.route('/browse_playground', methods=["GET", "POST"])
# def browse_playground():
#  data1 = mongo.db.parks.find()    data2 = mongo.db.parks.find()
#   if request.method == "POST":
# return render_template('browseplayground.html', 
#                             playgrounds = mongo.db.playgrounds.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
