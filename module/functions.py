import sys
import os

# Get the absolute path of the parent directory containing the 'module' package
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the 'module' directory to the Python path
sys.path.insert(0, module_dir)
from module.data import meals, combos
from module.exceptions import MealTooBigError, MealNotFoundError


def calory_counter(*foods):
    total = 0
    for food in foods:
        if food in meals.keys():
            total += meals[food]['calories']
        elif food in combos.keys():
            total += calory_counter(*combos[food]['meals'])
        else:
            raise MealNotFoundError(food)
    if total > 2000:
        raise MealTooBigError(total)
    return total

def price_counter(*foods):
    total = 0
    for food in foods:
        if food in meals.keys():
            total += meals[food]['price']
        elif food in combos.keys():
            total += combos[food]['price']
        else :
            raise MealNotFoundError(food)
    return total

