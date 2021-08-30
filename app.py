#!flask/bin/python
"""LOL a handmade list"""
import random
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Tacos',
        'ing': 'Meat - or alt, Tortillas, Tomatoes, Greek Yogurt, Salsa, Hotsauce, Lettuce, Beans',
	      'dif': 'easy'
    },
    {
        'id': 2,
        'name': 'Pizza Night',
        'ing': 'Doughs, Cheeses, Tomato Sauce, Tomato Paste, Toppings',
	      'dif': 'medium'
    },
    {
        'id': 3,
        'name': 'Mandarin Chicken',
        'ing': 'TJs Orange Chicken, Rice',
	      'dif': 'easy'
    },
    {
        'id': 4,
        'name': 'Hibachi',
        'ing': 'Meat or alt, Rice, Zucchini, Onions, Soy Sauce, Ginger',
	      'dif': 'medium'
    },
    {
        'id': 5,
        'name': 'Steak Night',
        'ing': 'Steaks, EVOO, Garlic, Mustard, Soy Sauce, Woosh, Lemon Juice, Salt, Pepper',
	      'dif': 'date night'
    },
    {
        'id': 6,
        'name': 'Bourbon Salmon',
        'ing': 'Salmon, Bourbon, Brown Sugar, Pineapple Juice, Garlic, Oil, Soy Sauce, Black Pepper',
	      'dif': 'date night'
    },
    {
        'id': 7,
        'name': 'Nuggies',
        'ing': 'Frozen Nuggets, Mac and Cheese side',
	      'dif': 'easiest'
    },
    {
        'id': 8,
        'name': 'Meat Loaf',
        'ing': 'Ground Beef or Turkey, Egg, Onion, Breadcrumbs',
	      'dif': 'easy'
    },	
    {
        'id': 9,
        'name': 'Spaghetti',
        'ing': 'Angel Hair, Onion, Tomato Sauce, Tomato Paste, Garlic, Italian Sausage, Parsley, Basil, Woosh',
	      'dif': 'easy'
    },
    {
        'id': 10,
        'name': 'BBQ pork',
        'ing': 'Pork Shoulder, Sauce, Apple Cider, Mustard, Paprika, Chili Powder, Brown Sugar, Cayenne, Garlic Powder',
	      'dif': 'hard'
    },
    {
        'id': 11,
        'name': 'Fajitas',
        'ing': 'Bell Peppers, Onions, Optional meat, Tortillas, Avocado, Refried Beans, Rice, Salsa',
	      'dif': 'easy'
    },
    {
        'id': 12,
        'name': 'Black Bean Tostadas',
        'ing': 'Black Beans, Corn, Tortillas, Chives, Avocado, Red Onion, Jalapeno, Greek Yogurt, Lemon Juice, Cilantro',
	      'dif': 'easy'
    },
    {
        'id': 13,
        'name': 'Summer Rolls',
        'ing': 'Rice Paper, Cilantro, Carrots, Vermicelli Noodles, Cucumber, Cabbage, Peanut Sauce - ginger, garlic, peanut butter, soy sauce, rice vinegar',
	      'dif': 'medium'
    },
    {
        'id': 14,
        'name': 'Soba Noodles',
        'ing': 'Buckwhear Soba Noodles, Sesame Oil, Rice Vinegar, Soba Dipping Sauce',
	      'dif': 'easy'
    },
    {
        'id': 15,
        'name': 'Soup and Grilled Cheese',
        'ing': 'Tomato or other Soup, Bread, Cheddar, Gouda',
	      'dif': 'easy'
    },
    {
        'id': 16,
        'name': 'Terryaki Chicken - BCBR',
        'ing': 'Chicken Breast, Mirin, Soy Sauce, Rice',
	      'dif': 'easy'
    },
    {
        'id': 17,
        'name': 'Philly CheeseSteaks',
        'ing': 'Ribeyes, Provolone, Green Pepper, Onion, Mushrooms, Hoagie Rolls',
	      'dif': 'medium'
    },
    {
        'id': 18,
        'name': 'Tomato Gnocchi',
        'ing': 'Gnocchi, Sundried Tomatoes, Garlic, Vegetable Stock, Heavy Cream, Basil, Parmesan',
	      'dif': 'medium'
    },
    {
        'id': 19,
        'name': 'Spinach Goat Cheese Pasta',
        'ing': 'Spinach, Goat Cheese, Pasta, Lemon Juice',
	      'dif': 'easy'
    }
]



@app.route('/recipe/api/v1.0/recipe/<int:id>', methods=['GET'])
def Get_Recipe(id):
    """Return recipe by ID"""
    if id not in range(1,len(recipes)):
        abort(404)
    recipe = recipes[id-1]
    return jsonify({'recipe': recipe})

	
@app.route('/recipe/api/v1.0/recipe/allrecipes', methods=['GET'])
def Get_Allrecipes():
    """Return all recipes"""
    return jsonify(recipes)

	
@app.route('/recipe/api/v1.0/recipe/recipeoftheday', methods=['GET'])
def Get_Recipeoftheday():
    """Return a random recipe"""
	#Example
	#curl -X GET http://localhost:5000/recipe/api/v1.0/recipe/recipeoftheday
    recipe = random.choice(recipes)
    return jsonify({'Meal of the day': recipe['name']}, {'Ingredients': recipe['ing']}, {'Difficulty Level': recipe['dif']})

	
@app.route('/recipe/api/v1.0/newrecipe', methods=['POST'])
def Create_Recipe():
    """Adds a recipe to the list"""
	#Example
	#curl -H "Content-Type: application/json" -X POST -d '{"name":"recipename","ing":"ingredient1, ingredient2, ingredient3","dif":"difficultylevel"}' http://localhost:5000/recipe/api/v1.0/newrecipe
    if not request.json or not 'text' in request.json:
        abort(400)
    recipe = {
        'id': len(recipes) + 1,
        'text': request.json.get('text', ""),
        'def': request.json.get('def', "")
    }
    recipes.append(recipe)
    return jsonify({'recipe': recipe}), 201
	

@app.route('/recipe/api/v1.0/DeleteRecipeById/<int:id>', methods=['DELETE'])
def Delete_RecipeById(id):
    """Delete a recipe with the provided recipeID"""
    if id not in range(1,len(recipes)):
        abort(404)
    recipe = recipes[id-1]
    recipes.remove(recipe)
    return jsonify({'Successfully removed the recipe': recipe['name']})


if __name__ == '__main__':
    app.run(debug=True)
