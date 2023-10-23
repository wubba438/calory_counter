from unittest import TestCase
from datetime import datetime
from module.orders import Order

class OrderTestCase(TestCase):
    def test_order_id_is_unique(self):
        initial_counter = Order.counter
        order_1 = Order(['meal-1'])
        self.assertEqual(order_1.order_id, f"order-{initial_counter+1}")
        order_2 = Order(['meal-3'])
        self.assertEqual(order_2.order_id, f"order-{initial_counter+2}")
    def test_order_counter(self):
        initial_counter = Order.counter
        order_1 = Order(['meal-1'])
        order_2 = Order(['meal-3'])
        result = Order.counter
        self.assertEqual(result, initial_counter+2, f"Expected 2 got {result}")
    def test_order_calory_counter(self):
        order_3 = Order(['meal-1','meal-2'])
        result = order_3.calories
        self.assertEqual(result, 1350, f"Expected 1350 got {result}.")
    def test_order_price_counter(self):
        order_3 = Order(['meal-1','meal-2'])
        result = order_3.price
        self.assertEqual(result, 12, f"Expected 12 got {result}.")
    def test_order_date(self):
        order_3 = Order(['meal-1','meal-2'], '11-Nov-2001')
        result = order_3.date
        self.assertEqual(result.year, 2001, f"Expected 2001 got {result}.")
        self.assertEqual(result.month, 11, f"Expected 11 got {result}.")
        self.assertEqual(result.day, 11, f"Expected 11 got {result}.")
    def test_order_date_default(self):
        order_3= Order(['meal-1','meal-2'])
        result = order_3.date
        year_today = datetime.today().year
        self.assertEqual(result.year, year_today, f"Expected {year_today} got {result}.")
        month_today = datetime.today().month
        self.assertEqual(result.month, month_today, f"Expected {month_today} got {result}.")
        day_today = datetime.today().day
        self.assertEqual(result.day, day_today, f"Expected {day_today} got {result}.")
    def test_order_meal_too_big_error(self):
        order_3 = Order(['meal-1', 'meal-1', 'meal-1', 'meal-1'])
        result = order_3.order_accepted
        result_2 = order_3.order_refused_reson
        self.assertEqual(result, False, f"Expected False got {result}")
        self.assertEqual(result_2, 'Meal is too big! 2400 is way too much!', f"Not {result_2}")
    def test_order_meal_not_found_error(self):
        order_4 = Order(['gh'])
        result = order_4.order_accepted
        result_2 = order_4.order_refused_reson
        self.assertEqual(result, False, f"Expected False got {result}")
        self.assertEqual(result_2, "gh is not on the menu", f"Not {result_2}")
    def test_order_meal_accepted_correctly(self):
        order_3 = Order(['meal-1','meal-2'])
        result = order_3.order_accepted
        result_2 = order_3.order_refused_reson
        self.assertEqual(result, True, f"Expected True got {result}")
        self.assertEqual(result_2, None, f"Not {result_2}")
        
