import unittest
from add import add_ab

class TestAdd(unittest.TestCase):
    def test_add_23(self):
        self.assertEqual(add_ab(2,3), 5)
    
    def test_add_19(self):
        self.assertEqual(add_ab(1,9), 10)
    
    def test_add_1_minus7(self):
        self.assertEqual(add_ab(1,-7), 8)
    
if __name__=='__main__':
        unittest.main()