import unittest
from prime_number_1 import is_prime

class TestPrime(unittest.TestCase):
    def test_prime_not_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))
    def test_typeerror_1(self):
        with self.assertRaises(TypeError):
            is_prime(6.5)
    def test_typeerror_2(self):
        with self.assertRaises(TypeError):
            is_prime('five')
    def test_valueerror(self):
        with self.assertRaises(ValueError):
            is_prime(-4)

if __name__=='__main__':
    unittest.main()
