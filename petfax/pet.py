from flask import ( Blueprint, render_template, abort ) 
import json

pets = json.load(open('pets.json'))
# print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('pets/index.html', pets=pets)

# Define the route for showing individual pet
@bp.route('/<int:index>')
def show_pet(index):
    # Check if the index is within the valid range of the list
    if index < 1 or index > len(pets):
        abort(404)  # Return a 404 Not Found error if the index is out of range
    
    # Adjust the index and get the pet data
    pet = pets[index - 1]
    
    # Render the show pet template with the pet data
    return render_template('pets/show.html', pet=pet)
