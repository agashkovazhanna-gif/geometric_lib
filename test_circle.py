import unittest
import math


from circle import area as circle_area, perimeter as circle_perimeter

class TestCircle(unittest.TestCase):
        
    def test_circle_area_unit(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        
    def test_circle_area_large(self):
        self.assertAlmostEqual(circle_area(10), 100 * math.pi)
        
    def test_circle_area_float(self):
        self.assertAlmostEqual(circle_area(1.5), 2.25 * math.pi)
        
    def test_circle_perimeter_unit(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        
    def test_circle_perimeter_large(self):
        self.assertAlmostEqual(circle_perimeter(10), 20 * math.pi)
        
    def test_circle_perimeter_float(self):
        self.assertAlmostEqual(circle_perimeter(2.5), 5 * math.pi)

    def test_area_negative(self):
        self.assertFalse(circle_area(-5))
        self.assertFalse(circle_area(-2.5))
    
    def test_area_zero(self):
        self.assertFalse(circle_area(0))

    def test_perimeter_negative(self):
        self.assertFalse(circle_perimeter(-5))
        self.assertFalse(circle_perimeter(-2.5))
    
    def test_perimeter_zero(self):
        self.assertFalse(circle_perimeter(0))
    
