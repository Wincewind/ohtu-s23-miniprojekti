import unittest
from unittest import mock
from services.reference_services import ReferenceServices


class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.mock_dataprocessing = mock.Mock()
        self.mock_dataprocessing.get_all_books()

        '''setting return value to False indicating that a book with the same title do not exist in beginning'''
        self.mock_dataprocessing.get_book_by_title.return_value = False

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

    def test_add_booktitle_twice(self):
        self.assertTrue(self.ref_ser.add_book('Garwin, Robert',
                                              'Clean Code: A Handbook of Agile Software Craftsmanship',
                                              2008, 'Prentice Hall', 'Bakerstreet 123'))
        
        '''setting return value to True indicating that a book with the same title do exist after added title'''
        self.mock_dataprocessing.get_book_by_title.return_value = True
        self.assertFalse(self.ref_ser.add_book('Garwin, Robert',
                                               'Clean Code: A Handbook of Agile Software Craftsmanship',
                                               2008, 'Prentice Hall', 'Bakerstreet 123'))
