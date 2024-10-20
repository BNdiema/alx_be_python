import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(10, 0), None)


if __name__ == '__main__':
    unittest.main()