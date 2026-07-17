import unittest
import sys
from pathlib import Path

# Add parent directory to path to import calculator
sys.path.insert(0, str(Path(__file__).parent.parent))

from calculator import add_numbers


class TestAddNumbers(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        self.assertEqual(add_numbers(2, 3), 5)
    
    def test_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        self.assertEqual(add_numbers(-2, -3), -5)
    
    def test_add_mixed_positive_negative(self):
        """Test addition of positive and negative numbers."""
        self.assertEqual(add_numbers(5, -3), 2)
        self.assertEqual(add_numbers(-5, 3), -2)
    
    def test_add_with_zero(self):
        """Test addition with zero."""
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(5, 0), 5)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_add_decimal_numbers(self):
        """Test addition of decimal/float numbers."""
        self.assertAlmostEqual(add_numbers(1.5, 2.3), 3.8, places=5)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=5)
    
    def test_add_large_numbers(self):
        """Test addition of large numbers."""
        self.assertEqual(add_numbers(1000000, 2000000), 3000000)
    
    def test_add_commutative_property(self):
        """Test that addition is commutative (a + b = b + a)."""
        self.assertEqual(add_numbers(3, 7), add_numbers(7, 3))


if __name__ == '__main__':
    unittest.main()
