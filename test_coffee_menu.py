import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):

    #Set code up for testing
    def setUp(self):
        self.menu = CoffeeMenu()
    
    def tearDown(self):
        self.menu = None

    def test_get_price_exisisting_item(self):
        self.assertEqual(self.menu)

    def test_get_price_non_existing_item(self):
        self.assertTrue(self.menu, 'Foccacia')

    def test_add_item(self):
        self.assertIn(self.menu, 'large latte')


if __name__ == '__main__':
    unittest.main()

    