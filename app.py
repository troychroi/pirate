responses = {}

import random

def askQuestions():
	questions = {
		"strong": "do you like your drink strong?",
		"salty": "do you like your drink tangy?",
		"bitter": "do you like your drink bitter?",
		"sweet": "do you like your drink sweet?",
		"fruity": "do you like your drink fruity?",
	}	
	for key, value in questions.items():
		y = True
		n = False		
		user_input = input(value+" (y/n?) ")
		responses.update({key: user_input})
def constructDrink():
	ingredients = {
		"strong": ["rum", "whiskey", "gin"],
		"salty": ["olive", "salted rim", "bacon"],
		"bitter": ["bitters", "tonic", "lemon"],
		"sweet": ["sugar", "honey", "cola"],
		"fruity": ["orange", "cassis", "cherry"],
	}	
	drink_ingredients = []
	for key, value in responses.items():
		if(value == True):
			drink_ingredients.append(random.choice(ingredients[key]))
	print(drink_ingredients)
	return drink_ingredients
def nameDrink():
	adjectives = [
		"Potent",
		"Salty",
		"Punching",
		"Cloying",
		"Tropical"
	]
	nouns = [
		"Bomb",
		"Dog",
		"Martini",
		"Daquiri",
		"Punch"
	]
	return (random.choice(adjectives) + ' ' + random.choice(nouns))

if __name__ == '__main__':
	askQuestions()
	constructDrink()
	yesAnother = nameDrink()
	while True:	
		y = True
		n = False
		another = input("Would you like another "+ yesAnother +"(y/n)? ")
		if (another == False):
			break
		else:
			print("Here's another " + yesAnother)