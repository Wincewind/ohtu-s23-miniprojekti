import unittest
import dataprocessing
from app import app


class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_book(self):
        with app.app_context():
            self.assertEqual(True, dataprocessing.add_book(
                "Wincewind", "My Life", 2000, "My mom", "123 Noway Street"))

    def test_fail_to_add_book(self):
        with app.app_context():
            self.assertEqual(False, dataprocessing.add_book(
                None, None, None, None, None))

    def test_get_all_books(self):
        with app.app_context():
            self.assertEqual(len(dataprocessing.get_all_books()), 0)

    def test_delete_all_books(self):
        with app.app_context():
            dataprocessing.add_book(
                "Wincewind", "My Life", 2000, "My mom", "123 Noway Street")
            self.assertEqual([], dataprocessing.delete_all_books())
