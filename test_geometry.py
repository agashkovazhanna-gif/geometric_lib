import unittest
import math

from triangle import area as triangle_area, perimeter as triangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

class TestTriangle(unittest.TestCase):
    def test_triangle_area_zero(self):
        self.assertEqual(triangle_area(10, 0), 0)
        
    def test_triangle_area_small(self):
        self.assertEqual(triangle_area(4, 3), 6)
        
    def test_triangle_area_large(self):
        self.assertEqual(triangle_area(100, 5000), 250000)
        
    def test_triangle_area_float(self):
        self.assertEqual(triangle_area(5.5, 2.0), 5.5)

    def test_triangle_perimeter_equilateral(self):
        self.assertEqual(triangle_perimeter(5, 5, 5), 15)
        
    def test_triangle_perimeter_small(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        
    def test_triangle_perimeter_large(self):
        self.assertEqual(triangle_perimeter(746, 865, 938), 2549)
        
    def test_triangle_perimeter_float(self):
        self.assertEqual(triangle_perimeter(2.5, 3.5, 4.5), 10.5)

class TestSquare(unittest.TestCase):
    def test_square_area_zero(self):
        self.assertEqual(square_area(0), 0)
        
    def test_square_area_small(self):
        self.assertEqual(square_area(3), 9)
        
    def test_square_area_large(self):
        self.assertEqual(square_area(10000), 100000000)
        
    def test_square_area_float(self):
        self.assertEqual(square_area(2.5), 6.25)

    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)
        
    def test_square_perimeter_small(self):
        self.assertEqual(square_perimeter(3), 12)
        
    def test_square_perimeter_large(self):
        self.assertEqual(square_perimeter(10000), 40000)
        
    def test_square_perimeter_float(self):
        self.assertEqual(square_perimeter(1.5), 6.0)

class TestRectangle(unittest.TestCase):
    def test_rectangle_area_zero(self):
        self.assertEqual(rectangle_area(10, 0), 0)
        
    def test_rectangle_area_small(self):
        self.assertEqual(rectangle_area(4, 6), 24)

    def test_rectangle_area_large(self):
        self.assertEqual(rectangle_area(20, 30), 600)
        
    def test_rectangle_area_float(self):
        self.assertEqual(rectangle_area(3.5, 2.5), 8.75)

    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        
    def test_rectangle_perimeter_small(self):
        self.assertEqual(rectangle_perimeter(5, 5), 20)
        
    def test_rectangle_perimeter_large(self):
        self.assertEqual(rectangle_perimeter(15, 2500), 5030)
        
    def test_rectangle_perimeter_float(self):
        self.assertEqual(rectangle_perimeter(2.5, 3.5), 12.0)

class TestCircle(unittest.TestCase):
    def test_circle_area_zero(self):
        self.assertAlmostEqual(circle_area(0), 0)
        
    def test_circle_area_unit(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        
    def test_circle_area_large(self):
        self.assertAlmostEqual(circle_area(10), 100 * math.pi)
        
    def test_circle_area_float(self):
        self.assertAlmostEqual(circle_area(1.5), 2.25 * math.pi)

    def test_circle_perimeter_zero(self):
        self.assertAlmostEqual(circle_perimeter(0), 0)
        
    def test_circle_perimeter_unit(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        
    def test_circle_perimeter_large(self):
        self.assertAlmostEqual(circle_perimeter(10), 20 * math.pi)
        
    def test_circle_perimeter_float(self):
        self.assertAlmostEqual(circle_perimeter(2.5), 5 * math.pi)