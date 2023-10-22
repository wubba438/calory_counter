class MealTooBigError(Exception):
    def __init__(self, calories):
        self.message = f"Meal is too big! {calories} is way too much!"
        super().__init__(self.message)