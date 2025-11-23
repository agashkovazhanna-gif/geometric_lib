import unittest
import math

from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestTriangle(unittest.TestCase):

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
   
    def test_area_negative(self):
        self.assertFalse(triangle_area(-5, 10))
        self.assertFalse(triangle_area(0, 10))
        self.assertFalse(triangle_area(10, -5))
    
    def test_perimeter_negative(self):
        self.assertFalse(triangle_perimeter(-3, 4, 5))
        self.assertFalse(triangle_perimeter(1, 1, 3))
        self.assertFalse(triangle_perimeter(0, 4, 5))