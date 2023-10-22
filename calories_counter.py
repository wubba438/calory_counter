meals = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}

combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}

def calory_counter(*foods):
    total = 0
    for food in foods:
        if food in meals:
            total += meals[food]
        elif food in combos:
            for item in combos[food]:
                total += meals[item]
        else :
            print("You have entered something not on the menu!")
            return 1
    return total

