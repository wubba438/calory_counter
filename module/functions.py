import sys
import os

# Get the absolute path of the parent directory containing the 'module' package
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the 'module' directory to the Python path
sys.path.insert(0, module_dir)
from module.data import meals, combos
from module.exceptions import MealTooBigError


def calory_counter(*foods):
    total = 0
    for food in foods:
        try:
            total += meals[food]['calories']
        except KeyError:
            try:
                total += calory_counter(*combos[food]['meals'])
            except KeyError :
                print(f"{food} is not on the menu!")
    if total > 2000:
        raise MealTooBigError(total)
    return total

