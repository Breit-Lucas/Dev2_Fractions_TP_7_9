from fractions import Fraction
import unittest

class TestFraction(unittest.TestCase):

    def test_constructeur(self):

        frac1 = Fraction(2, 4)
        self.assertEqual(frac1.numerator, 1)
        self.assertEqual(frac1.denominator, 2)

    def test_as_mixed_number(self):

        frac1 = Fraction(7, 2)
        self.assertEqual(frac1.as_mixed_number(), "3 + 1 / 2")

    def test_add(self):

        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        result = frac1 + frac2
        self.assertEqual(str(result), "7 / 6")

    def test_div(self):

        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        result = frac1 / frac2
        self.assertEqual(str(result), "3 / 4")

    def test_eq(self):

        frac1 = Fraction(2, 4)
        frac2 = Fraction(1, 2)
        self.assertTrue(frac1 == frac2)

    def test_is_integer(self):

        frac1 = Fraction(8, 4)
        self.assertTrue(frac1.is_integer())

    def test_is_proper(self):

        frac1 = Fraction(1, 2)
        self.assertTrue(frac1.is_proper())

    def test_is_adjacent_to(self):

        frac1 = Fraction(1, 2)
        frac2 = Fraction(2, 3)
        self.assertTrue(frac1.is_adjacent_to(frac2))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)