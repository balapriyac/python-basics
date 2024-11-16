from book import Book
import unittest

class TestBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass method: Runs before all tests...")
    def setUp(self):
        print("\nRunning setUp method...")
        self.book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        self.book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
    def tearDown(self):
        print("Running tearDown method...")
    def test_reading_time(self):
        print("Running test_reading_time...")
        self.assertEqual(self.book_1.get_reading_time(), f"{304*1.5} minutes")
        self.assertEqual(self.book_2.get_reading_time(), f"{447*1.5} minutes")
    def test_discount(self):
        print("Running test_discount...")
        self.assertEqual(self.book_1.apply_discount(),f"${15 - 15*0.05}")
        self.assertEqual(self.book_2.apply_discount(),f"${16 - 16*0.15}" )
    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass method: Runs after all tests...")

if __name__=='__main__':
    unittest.main()
