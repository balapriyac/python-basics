from book import Book
import unittest

class TestBook(unittest.TestCase):
    def test_reading_time(self):
        book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
        self.assertEqual(book_1.get_reading_time(), f"{304*1.5} minutes")
        self.assertEqual(book_2.get_reading_time(), f"{447*1.5} minutes")
    def test_discount(self):
        book_1 = Book('Deep Work','Cal Newport',304,15,0.05)
        book_2 = Book('Grit','Angela Duckworth',447,16,0.15)
        self.assertEqual(book_1.apply_discount(),f"${15 - 15*0.05}")
        self.assertEqual(book_2.apply_discount(),f"${16 - 16*0.15}" )

if __name__=='__main__':
    unittest.main()
