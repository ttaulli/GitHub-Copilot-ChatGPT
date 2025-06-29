import unittest
from tests import calculate

class TestCalculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate('add', 2, 3), 5)
        self.assertEqual(calculate('add', -1, 1), 0)

    def test_subtract(self):
        self.assertEqual(calculate('subtract', 5, 3), 2)
        self.assertEqual(calculate('subtract', 0, 5), -5)

    def test_multiply(self):
        self.assertEqual(calculate('multiply', 2, 3), 6)
        self.assertEqual(calculate('multiply', -1, 3), -3)

    def test_divide(self):
        self.assertEqual(calculate('divide', 6, 3), 2)
        self.assertAlmostEqual(calculate('divide', 7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculate('divide', 5, 0)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate('mod', 5, 2)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate('add', 'a', 2)
        with self.assertRaises(TypeError):
            calculate('add', 2, None)

if __name__ == '__main__':
    unittest.main()
