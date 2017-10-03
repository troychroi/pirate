questions = {
	"strong": "do you like your drink strong?",
	"salty": "do you like your drink tangy?",
	"bitter": "do you like your drink bitter?",
	"sweet": "do you like your drink sweet?",
	"fruity": "do you like your drink fruity?",
}

ingredients = {
	"strong": ["rum", "whiskey", "gin"],
	"salty": ["olive", "salted rim", "bacon"],
	"bitter": ["bitters", "tonic", "lemon"],
	"sweet": ["sugar", "honey", "cola"],
	"fruity": ["orange", "cassis", "cherry"],
}

responses = {}
drink_ingredients = []

import sys
import random

if __name__ == '__main__':
	
	def askQuestions():
		for key, value in questions.items():
			y = True
			n = False		
			user_input = input(value+" (y/n?) ")
			responses.update({key: user_input})
		# for key, value in responses.items():
		# 	print({key: value})
	askQuestions()
	def constructDrink():
		for key, value in responses.items():
			if(value == True):
				drink_ingredients.append(random.choice(ingredients[key]))
		print(drink_ingredients)
	constructDrink()