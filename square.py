import unittest


def area(a):
    '''Принимает число a и возвращает площадь квадрата со сторонами a на a'''
    return a * a


def perimeter(a):
    '''Принимает число a и возвращает периметр квадрата со сторонами a на a'''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_integer(self):
        self.assertEqual(area(3), 9)

    def test_area_fraction(self):
        self.assertEqual(area(0.5), 0.25)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_integer(self):
        self.assertEqual(perimeter(3), 12)

    def test_perimeter_fraction(self):
        self.assertEqual(perimeter(0.5), 2)
