import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = self.calc.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = self.calc.multiply(4, 5)
        self.assertEqual(result, 20)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(10, 0), None)


if __name__ == '__main__':
    unittest.main()