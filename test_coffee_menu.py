import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):

    #Set code up for testing
    def setUp(self):
        self.menu = CoffeeMenu()
    
    # def tearDown(self):
    #     self.menu = None
    # This is not needed 
    
    # Methods to test
    
    # def test_get_price_exisisting_item(self):
    #     self.assertTrue(self.menu, CoffeeMenu)
    # ISSUE: Incorrect assert usage
    # This doesn't test price retrieval at all
    # Correct code:
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('latte'), 3.00)

    # def test_get_price_non_existing_item(self):
    #     self.assertTrue(self.menu, 'Foccacia') 
    # ISSUE: Incorrect assert usage and logic
    # Correct code:
    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.get_price('focaccia'))

    # def test_add_item(self):
    #     self.assertIn(self.menu, 'large latte')
    # ISSUE: Incorrect assert method and logic
    # Should: 1) Add an item first, 2) Verify it was added with correct price
    # Correct code:
    def test_add_item(self):
        self.menu.add_item('focaccia', 3.50)
        self.assertEqual(self.menu.get_price('focaccia'), 3.50)

if __name__ == '__main__':
    unittest.main()

    