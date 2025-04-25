import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):

    #Set code up for testing
    def setUp(self):
        self.account = CoffeeMenu()
    
    def tearDown(self):
        self.account = None



if __name__ == '__main__':
    unittest.main()

    