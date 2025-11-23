import unittest
import math


from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

class TestRectangle(unittest.TestCase):
        
    def test_rectangle_area_small(self):
        self.assertEqual(rectangle_area(4, 6), 24)

    def test_rectangle_area_large(self):
        self.assertEqual(rectangle_area(20, 30), 600)
        
    def test_rectangle_area_float(self):
        self.assertEqual(rectangle_area(3.5, 2.5), 8.75)
        
    def test_rectangle_perimeter_small(self):
        self.assertEqual(rectangle_perimeter(5, 5), 20)
        
    def test_rectangle_perimeter_large(self):
        self.assertEqual(rectangle_perimeter(15, 2500), 5030)
        
    def test_rectangle_perimeter_float(self):
        self.assertEqual(rectangle_perimeter(2.5, 3.5), 12.0)

    def test_area_negative(self):
        self.assertFalse(rectangle_area(-5, 3))
        self.assertFalse(rectangle_area(5, -3))
        self.assertFalse(rectangle_area(-2, -4))
    
    def test_area_zero(self):
        self.assertFalse(rectangle_area(0, 0))
    
    def test_perimeter_negative(self):
        self.assertFalse(rectangle_perimeter(-5, 3))
        self.assertFalse(rectangle_perimeter(5, -3))
        self.assertFalse(rectangle_perimeter(-2, -4))
    
    def test_perimeter_zero(self):
        self.assertFalse(rectangle_perimeter(0, 0))