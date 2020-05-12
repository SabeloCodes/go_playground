import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Reading the environment vairable set on the .bash hidden file with Mongo Collection Name and Connection 
app.config["MONGO_DBNAME"] = 'go_playground'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

#creating new instance of PyMongo and adding the app object with constructor method
mongo = PyMongo(app)

@app.route('/')
# Function for displaying the playground.html page
@app.route('/find_playground')
def find_playground():
    # print(dir (mongo.db.playgrounds.find()))
    return render_template("playground.html", 
                            playgrounds = mongo.db.playgrounds.find(),
                            boroughs = mongo.db.boroughs.find())
 
# Function for displaying the addplayground.html page
@app.route('/add_playground')
def add_playground():
    return render_template("addplayground.html", 
                            playgrounds = mongo.db.playgrounds.find(),
                            boroughs = mongo.db.boroughs.find()) 

# Function for adding a playground to the database                            
@app.route('/insert_playground', methods=['POST'])
def insert_playground():
    playgrounds = mongo.db.playgrounds
    playgrounds.insert_one(request.form.to_dict())
    return redirect(url_for('show_playground'))     
    
# Function for displaying the showplayground.html page    
@app.route('/show_playground/<playground_id>')
def show_playground(playground_id):
    """Retrieving the playground and sending it through to the template"""
    the_playground =  mongo.db.playgrounds.find_one({"_id": ObjectId(playground_id)})
    return render_template('showplayground.html', playground=the_playground)
  
                            
#Retreives playground from the database using its id and displays it in a form for editing
@app.route('/edit_playground/<playground_id>')
def edit_playground(playground_id):
    """Gets playground that matches the playground id '_id' is the key""" 
    the_playground =  mongo.db.playgrounds.find_one({"_id": ObjectId(playground_id)})
    all_playgrounds =  mongo.db.playgrounds.find()
    print(the_playground) 
    return render_template('editplayground.html', playground=the_playground,
                           playgrounds=all_playgrounds)

                           


#Database updates with edited info 
@app.route('/update_playground/<playground_id>', methods=["POST"])
def update_playground(playground_id):
    playgrounds = mongo.db.playgrounds
    """Access playgrounds collection and call the update function"""
    playgrounds.update( {'_id': ObjectId(playground_id)},
    #Match form fields to playgrounds collection keys
    {
        'playground_name': request.form.get('playground_name'),
        'borough_name': request.form.get('borough_name'),
        'playground_description': request.form.get('playground_description'),
        'star_rating': request.form.get('star_rating'),
        'image_url': request.form.get('image_url')
    })
    return redirect(url_for('show_playground'))


# Function and route to display/browse all playgrounds 
@app.route('/browse_playground', methods=["GET", "POST"])
def browse_playground():
    playground_name = mongo.db.playgrounds.find(),
    borough_name = mongo.db.boroughs.find(), 
    playground_description = mongo.db.playgrounds.find(),
    star_rating = mongo.db.playgrounds.find(),
    image_url = mongo.db.playgrounds.find()
    borough_name = request.args.get('borough_name')
    
    if request.method == "POST":
        return render_template('browseplayground.html',
                    playgrounds = mongo.db.playgrounds.find(),
                    boroughs = mongo.db.boroughs.find())
            
    return render_template('browseplayground.html',
                    playgrounds = mongo.db.playgrounds.find({'borough_name': borough_name}),
                    boroughs = mongo.db.boroughs.find())
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
