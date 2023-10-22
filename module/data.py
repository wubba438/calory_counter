import json

with open("module/data/meals.json") as file:
	meals = json.load(file)['meals']
with open("module/data/combos.json") as file:
	combos = json.load(file)['combos']
print(meals)

meals = {meal['id']: meal for meal in meals}
combos = {combo['id']: combo for combo in combos}