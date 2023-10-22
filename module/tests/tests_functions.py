import sys
print(sys.path)

from unittest import TestCase
from module.functions import calory_counter,price_counter
from module.exceptions import MealTooBigError

class CaloriesCounterTestCase(TestCase):
    def test_count_meals_calories(self):
        result = calory_counter('meal-2','meal-4','meal-6')
        self.assertEqual(result, 1115, f"Expected 1115 got {result}.")
    
    def test_count_combo_calories(self):
        result = calory_counter('combo-1','combo-2')
        self.assertEqual(result, 1770, f"Expected 1770 got {result}.")
    
    def test_count_meals_and_combos_calories(self):
        result = calory_counter('combo-1','combo-2','meal-6')
        self.assertEqual(result, 1785, f"Expected 1785 got {result}.")

    def test_raise_error(self):
        with self.assertRaises(MealTooBigError) as e:
            calory_counter('combo-1','combo-1')
        self.assertEqual(
            e.exception.message,
            "Meal is too big! 2140 is way too much!",
            "Not expected error message"
        )

class CaloriesCounterTestCase(TestCase):
    def test_count_meals_price(self):
        result = price_counter('meal-2','meal-4','meal-6')
        self.assertEqual(result, 17, f"Expected 17 got {result}.")
    
    def test_count_combo_calories(self):
        result = price_counter('combo-1','combo-2')
        self.assertEqual(result, 21, f"Expected 21 got {result}.")
    
    def test_count_meals_and_combos_calories(self):
        result = price_counter('combo-1','combo-2','meal-6')
        self.assertEqual(result, 25, f"Expected 25 got {result}.")