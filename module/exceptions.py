class MealTooBigError(Exception):
    def __init__(self, calories):
        self.message = f"Meal is too big! {calories} is way too much!"
        super().__init__(self.message)

class MealNotFoundError(Exception):
    def __init__(self, food_id):
        self.message = f"{food_id} is not on the menu"
        super().__init__(self.message)