import unittest
from entities.reference import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(["Martin","Robert"],
                         "Clean Code: A Handbook of Agile Software Craftsmanship",
                         2000,
                         "Prentice Hall")
        
    def test_setup(self):
        self.assertEqual(self.book.authors,["Martin","Robert"])
