from unittest import TestCase

from module.orders import Order

class OrderTestCase(TestCase):
    def test_order_id_is_unique(self):
        initial_counter = Order.counter
        order_1 = Order(['meal-1'])
        self.assertEqual(order_1.order_id, f"order-{initial_counter+1}")
        order_2 = Order(['meal-3'])
        self.assertEqual(order_2.order_id, f"order-{initial_counter+2}")
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
        
        

