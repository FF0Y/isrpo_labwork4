import math
import unittest


def area(r):
    '''Принимает число r и возвращает площадь круга с радиусом r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r и возвращает периметр круга с радиусом r'''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_integer(self):
        self.assertAlmostEqual(area(3), 28.274333882308138, places=12)

    def test_area_fraction(self):
        self.assertAlmostEqual(area(0.5), 0.7853981633974483, places=12)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_integer(self):
        self.assertAlmostEqual(perimeter(3), 18.84955592153876, places=12)

    def test_perimeter_fraction(self):
        self.assertAlmostEqual(perimeter(0.5), 3.141592653589793, places=12)
