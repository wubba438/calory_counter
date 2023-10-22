from data import meals, combos
from exceptions import MealTooBigError

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

