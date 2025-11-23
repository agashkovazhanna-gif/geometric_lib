import unittest
import math

from square import area as square_area, perimeter as square_perimeter


class TestSquare(unittest.TestCase):
        
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

    def test_area_negative(self):
        self.assertFalse(square_area(-5))
        self.assertFalse(square_area(-2.5))
    
    def test_area_zero(self):
        self.assertFalse(square_area(0))

    def test_perimeter_negative(self):
        self.assertFalse(square_perimeter(-5))
        self.assertFalse(square_perimeter(-2.5))
    
    def test_perimeter_zero(self):
        self.assertFalse(square_perimeter(0))
