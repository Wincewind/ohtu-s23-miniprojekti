import unittest
from unittest import mock
from services.reference_services import ReferenceServices


class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.mock_dataprocessing = mock.Mock()
        self.mock_dataprocessing.get_all_books()
        self.ref_ser = ReferenceServices(self.mock_dataprocessing)

    def test_add_valid_book(self):
        self.assertTrue(self.ref_ser.add_book('Garwin, Robert',
                                              'Clean Code: A Handbook of Agile Software Craftsmanship',
                                              2008, 'Prentice Hall', 'Bakerstreet 123'))

    def test_add_book_with_invalid_year(self):
        self.assertFalse(self.ref_ser.add_book('Garwin, Robert',
                                               'Clean Code: A Handbook of Agile Software Craftsmanship',
                                               1000, 'Prentice Hall', 'Bakerstreet 123'))

    def test_add_book_with_str_type_year(self):
        self.assertFalse(self.ref_ser.add_book('Garwin, Robert',
                                               'Clean Code: A Handbook of Agile Software Craftsmanship',
                                               '1000', 'Prentice Hall', 'Bakerstreet 123'))

    def test_add_book_with_invalid_author(self):
        self.assertFalse(self.ref_ser.add_book(None,
                                               'Clean Code: A Handbook of Agile Software Craftsmanship',
                                               2008, 'Prentice Hall', 'Bakerstreet 123'))

    def test_get_all_references_calls_get_all_books(self):
        self.ref_ser.get_all_references()
        self.mock_dataprocessing.get_all_books.assert_called()
