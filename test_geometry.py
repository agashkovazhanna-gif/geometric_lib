import unittest
import math

from triangle import area as triangle_area, perimeter as triangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

class TestTriangle(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(10, 5), 25)
        self.assertEqual(triangle_area(4, 3), 6)
        self.assertEqual(triangle_area(100, 50), 2500)
        self.assertEqual(triangle_area(5.5, 2.0), 5.5)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(5, 5, 5), 15)
        self.assertEqual(triangle_perimeter(7, 8, 9), 24)
        self.assertEqual(triangle_perimeter(2.5, 3.5, 4.5), 10.5)

class TestSquare(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_area(3), 9)
        self.assertEqual(square_area(10), 100)
        self.assertEqual(square_area(2.5), 6.25)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(3), 12)
        self.assertEqual(square_perimeter(10), 40)
        self.assertEqual(square_perimeter(1.5), 6.0)

class TestRectangle(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(4, 6), 24)
        self.assertEqual(rectangle_area(5, 5), 25)
        self.assertEqual(rectangle_area(20, 30), 600)
        self.assertEqual(rectangle_area(3.5, 2.5), 8.75)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(4, 6), 20)
        self.assertEqual(rectangle_perimeter(5, 5), 20)
        self.assertEqual(rectangle_perimeter(15, 25), 80)
        self.assertEqual(rectangle_perimeter(2.5, 3.5), 12.0)

class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(2), 4 * math.pi)
        self.assertAlmostEqual(circle_area(10), 100 * math.pi)
        self.assertAlmostEqual(circle_area(1.5), 2.25 * math.pi)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(2), 4 * math.pi)
        self.assertAlmostEqual(circle_perimeter(10), 20 * math.pi)
        self.assertAlmostEqual(circle_perimeter(2.5), 5 * math.pi)
