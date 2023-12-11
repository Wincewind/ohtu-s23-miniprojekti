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
        os.system(
            f"{os.getenv('PSQL_SCHEMA_COMMAND','psql -d testdb -f')} src/tests/test-schema.sql")

    def test_add_reference(self):
        with app.app_context():
            self.assertEqual(True, dataprocessing.add_reference(
                author="Wincewind", title="My Life", year=2000, publisher="My mom",
                publisher_address="123 Noway Street"))

    def test_fail_to_add_reference(self):
        with app.app_context():
            self.assertEqual(False, dataprocessing.add_reference())

    def test_get_all_references(self):
        with app.app_context():
            self.assertEqual(len(dataprocessing.get_all_references()), 2)

    @patch('dataprocessing.db.session.execute')
    def test_fail_to_get_all_references(self, mock_execute):
        with app.app_context():
            mock_execute.side_effect = Exception("Database error")
            result = dataprocessing.get_all_references()
            self.assertEqual(result, [])
            mock_execute.assert_called_once()

    def test_delete_all_references(self):
        with app.app_context():
            dataprocessing.add_reference(
                author="Wincewind", title="My Life", year=2000, publisher="My Dad",
                publisher_address="123 Noway Street")
            self.assertEqual([], dataprocessing.delete_all_references())

    @patch('dataprocessing.db.session.execute')
    def test_fail_to_delete_references(self, mock_execute):
        with app.app_context():
            mock_execute.side_effect = Exception("Database error")
            result = dataprocessing.delete_all_references()
            self.assertEqual(result, [])
            self.assertEqual(mock_execute.call_count, 2)

    def test_delete_single_reference(self):
        with app.app_context():
            dataprocessing.add_reference(
                author="Wincewind", title="My Life", year=2000, publisher="My Dad",
                publisher_address="123 Noway Street")
            # Get reference from database (listed dictionary)
            result = dataprocessing.get_all_references()
            # Return the id of the reference as a list
            self.assertEqual(
                True, dataprocessing.delete_references_by_id([result[0]['id']]))
            self.assertEqual(2, len(dataprocessing.get_all_references()))

    def test_delete_multiple_references(self):
        with app.app_context():
            dataprocessing.add_reference(
                author="Hawking, Stephen", title="Brief Answers to the Big Questions", year=2018,
                publisher="Murray, John", publisher_address="338 Euston Road London")
            dataprocessing.add_reference(
                author="Wincewind", title="My Life", year=2000, publisher="My Dad",
                publisher_address="123 Noway Street")
            # Returns references from database (listed dictionary)
            result = dataprocessing.get_all_references()
            # Get the ids of the references as a list
            ids = [id['id'] for id in result]
            self.assertEqual(True, dataprocessing.delete_references_by_id(ids))
            self.assertEqual(0, len(dataprocessing.get_all_references()))

    @patch('dataprocessing.db.session.execute')
    def test_fail_to_delete_references_by_id(self, mock_execute):
        with app.app_context():
            mock_execute.side_effect = Exception("Database error")
            self.assertFalse(dataprocessing.delete_references_by_id([1]))
            mock_execute.assert_called_once()

    def test_get_reference_by_title(self):
        with app.app_context():
            dataprocessing.add_reference(
                author="Wincewind", title="My Life", year=2000, publisher="My Dad",
                publisher_address="123 Noway Street")
            self.assertEqual(
                True, dataprocessing.get_reference_by_title("My Life"))

    def test_fail_to_get_reference_by_title(self):
        with app.app_context():
            self.assertEqual(
                False, dataprocessing.get_reference_by_title("Your Life"))

    @patch('dataprocessing.db.session.execute')
    def test_fail_to_get_reference_by_title_database_error(self, mock_execute):
        with app.app_context():
            mock_execute.side_effect = Exception("Database error")
            result = dataprocessing.get_reference_by_title("Your Life")
            self.assertEqual(result, False)
