from Simple_Calculator import Calculator

import unittest

class CalcTest (unittest.TestCase):
    type_of_calc = "Standard"
    calc = Calculator (type_of_calc)

    def test_Add(self):
        self.assertEqual(self.calc.Add(2,2), 4)

    def test_Divide(self):
        self.assertEqual(self.calc.Divide(10,5), 2)

    def test_Minus(self):
        self.assertEqual(self.calc.Minus(10,5), 5)

if __name__ == "__main__":
    unittest.main()