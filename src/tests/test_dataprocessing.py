import os
import unittest
from unittest.mock import patch
import dataprocessing
from app import app


class TestDataProcessing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.system("psql -c 'create database testdb;'")

    def setUp(self):
        os.system(f"psql -d {os.getenv('DATABASE_URL')} -f src/tests/test-schema.sql")

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
            self.assertEqual(len(dataprocessing.get_all_books()), 2)

    @patch('dataprocessing.db.session.execute')
    def test_fail_to_get_all_books(self, mock_execute):
        with app.app_context():
            mock_execute.side_effect = Exception("Database error")
            result = dataprocessing.get_all_books()
            self.assertEqual(result, [])
            mock_execute.assert_called_once()

    def test_delete_all_books(self):
        with app.app_context():
            dataprocessing.add_book(
                "Wincewind", "My Life", 2000, "My mom", "123 Noway Street")
            self.assertEqual([], dataprocessing.delete_all_books())

    @patch('dataprocessing.db.session.execute')
    def test_fail_to_delete_books(self, mock_execute):
        with app.app_context():
            mock_execute.side_effect = Exception("Database error")
            result = dataprocessing.delete_all_books()
            self.assertEqual(result, [])
            self.assertEqual(mock_execute.call_count, 2)

    def test_delete_single_book(self):
        with app.app_context():
            dataprocessing.add_book(
                "Wincewind", "My Life", 2000, "My mom", "123 Noway Street")
            result = dataprocessing.get_all_books() # Get book from database (listed dictionary)
            # Return the id of the book as a list
            self.assertEqual(True, dataprocessing.delete_books_by_id([result[0]['book_id']]))
            self.assertEqual(0, len(dataprocessing.get_all_books()))

    def test_delete_multiple_books(self):
        with app.app_context():
            dataprocessing.add_book(
                "Hawking, Stephen", "Brief Answers to the Big Questions", 2018,
                "Murray, John", "338 Euston Road London")
            dataprocessing.add_book(
                "Wincewind", "My Life", 2000, "My mom", "123 Noway Street")
            result = dataprocessing.get_all_books() # Returns both books from database (listed dictionary)
            # Get the ids of the books as a list
            ids = [id['book_id'] for id in result]
            self.assertEqual(True, dataprocessing.delete_books_by_id(ids))
            self.assertEqual(0, len(dataprocessing.get_all_books()))

    @patch('dataprocessing.db.session.execute')
    def test_fail_to_delete_books_by_id(self, mock_execute):
        with app.app_context():
            mock_execute.side_effect = Exception("Database error")
            self.assertFalse(dataprocessing.delete_books_by_id([1]))
            mock_execute.assert_called_once()
