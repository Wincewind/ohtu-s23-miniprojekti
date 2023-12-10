import unittest
from entities.reference import Book, Article


class TestReference(unittest.TestCase):
    def setUp(self):
        self.book = Book(authors="Martin, Robert",
                         title="Clean Code: A Handbook of Agile Software Craftsmanship",
                         year=2000,
                         publisher="Prentice Hall",
                         publisher_address="Upper Saddle River, NJ")
        
        self.article = Article(authors="Nash, John",
                         title="Non-cooperative Games",
                         journal="Annals of Mathematics",
                         year    = 1951,
                         volume  = 54,
                         number  = 2,
                         pages   = "286--295")

    def test_setup_book(self):
        self.assertEqual(self.book.authors, "Martin, Robert")
        self.assertEqual(self.article.journal, "Annals of Mathematics")