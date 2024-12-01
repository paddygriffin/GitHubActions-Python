import unittest
from myModule.Calculator import add, subtract
#from myModule.Calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2) 