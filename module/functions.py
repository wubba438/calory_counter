from module.data import meals, combos
from module.exceptions import MealTooBigError, MealNotFoundError


def calory_counter(foods):
    total = 0
    for food in foods:
        if food in meals.keys():
            total += meals[food]['calories']
        elif food in combos.keys():
            total += calory_counter(combos[food]['meals'])
        else:
            raise MealNotFoundError(food)
    if total > 2000:
        raise MealTooBigError(total)
    return total


def price_counter(foods):
    total = 0
    for food in foods:
        if food in meals.keys():
            total += meals[food]['price']
        elif food in combos.keys():
            total += combos[food]['price']
        else:
            raise MealNotFoundError(food)
    return total
