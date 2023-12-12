import unittest
from unittest import mock
from services.reference_services import ReferenceServices


class TestReferenceService(unittest.TestCase):
    def setUp(self):
        self.mock_dataprocessing = mock.Mock()
        self.mock_dataprocessing.get_all_references()

        # setting return value to False indicating that a reference with the same title do not exist in beginning
        self.mock_dataprocessing.get_reference_by_title.return_value = False

        self.ref_ser = ReferenceServices(self.mock_dataprocessing)

    def test_add_valid_book(self):
        self.assertTrue(self.ref_ser.add_reference(authors='Garwin, Robert',
                                                   title='Clean Code: A Handbook of Agile Software Craftsmanship',
                                                   year=2008, publisher='Prentice Hall', publisher_address='Bakerstreet 123',
                                                   ref_type="book"))

    def test_add_valid_article(self):
        self.assertTrue(self.ref_ser.add_reference(authors="Johnson, Mike",
                                                   title='Clean Code: Magazine Version',
                                                   journal="Best Magazine", year=2008, volume="2", number="3", pages="45-50", ref_type="article"))

    def test_add_invalid_reference_type(self):
        self.assertFalse(self.ref_ser.add_reference(authors='Garwin, Robert',
                                                    title='Clean Code: A Handbook of Agile Software Craftsmanship',
                                                    year=1000, publisher='Prentice Hall', publisher_address='Bakerstreet 123', ref_type="magazine"))

    def test_add_book_with_invalid_year(self):
        self.assertFalse(self.ref_ser.add_reference(authors='Garwin, Robert',
                                                    title='Clean Code: A Handbook of Agile Software Craftsmanship',
                                                    year=1000, publisher='Prentice Hall', publisher_address='Bakerstreet 123', ref_type="book"))

    def test_add_book_with_str_type_year(self):
        self.assertFalse(self.ref_ser.add_reference(authors='Garwin, Robert',
                                                    title='Clean Code: A Handbook of Agile Software Craftsmanship',
                                                    year='1000', publisher='Prentice Hall', publisher_address='Bakerstreet 123', ref_type="book"))

    def test_add_book_with_invalid_author(self):
        self.assertFalse(self.ref_ser.add_reference(authors=None,
                                                    title='Clean Code: A Handbook of Agile Software Craftsmanship',
                                                    year=2008, publisher='Prentice Hall', publisher_address='Bakerstreet 123', ref_type="book"))

    def test_add_booktitle_twice(self):
        self.assertTrue(self.ref_ser.add_reference(authors='Garwin, Robert',
                                                   title='Clean Code: A Handbook of Agile Software Craftsmanship',
                                                   year=2008, publisher='Prentice Hall', publisher_address='Bakerstreet 123',
                                                   ref_type='book'))

        # setting return value to True indicating that a book with the same title do exist after added title
        self.mock_dataprocessing.get_reference_by_title.return_value = True
        self.assertFalse(self.ref_ser.add_reference(authors='Garwin, Robert',
                                                    title='Clean Code: A Handbook of Agile Software Craftsmanship',
                                                    year=2008, publisher='Prentice Hall', publisher_address='Bakerstreet 123',
                                                    ref_type='book'))

    def test_add_article_with_invalid_year(self):
        self.assertFalse(self.ref_ser.add_reference(authors="Johnson, Mike",
                                                    title='Clean Code: Magazine Version',
                                                    journal="Best Magazine", year=20082, volume="2", number="3", pages="45-50", ref_type="article"))

    def test_add_article_with_str_type_year(self):
        self.assertFalse(self.ref_ser.add_reference(authors="Johnson, Mike",
                                                    title='Clean Code: Magazine Version',
                                                    journal="Best Magazine", year="20082", volume="2", number="3", pages="45-50", ref_type="article"))

    def test_add_article_with_invalid_author(self):
        self.assertFalse(self.ref_ser.add_reference(authors=None,
                                                    title='Clean Code: Magazine Version',
                                                    journal="Best Magazine", year=2008, volume="2", number="3", pages="45-50", ref_type="article"))

    def test_add_article_twice(self):
        self.assertTrue(self.ref_ser.add_reference(authors="Johnson, Mike",
                                                   title='Clean Code: Magazine Version',
                                                   journal="Best Magazine", year=2008, volume="2", number="3", pages="45-50", ref_type="article"))

        self.mock_dataprocessing.get_reference_by_title.return_value = True
        self.assertFalse(self.ref_ser.add_reference(authors="Johnson, Mike",
                                                    title='Clean Code: Magazine Version',
                                                    journal="Best Magazine", year=2008, volume="2", number="3", pages="45-50", ref_type="article"))

    def test_get_all_references(self):
        self.ref_ser.get_all_references()
        self.mock_dataprocessing.get_all_references.assert_called()

    def test_delete_all_references(self):
        self.ref_ser.delete_all_references()
        self.mock_dataprocessing.delete_all_references.assert_called()

    def test_delete_references_by_id(self):
        self.ref_ser.delete_references_by_id([1, 2, 3])
        self.mock_dataprocessing.delete_references_by_id.assert_called()

    def test_add_reference_with_incorrect_ref_type(self):
        self.assertFalse(self.ref_ser.add_reference(authors="Johnson, Mike",
                                                    title='Clean Code: Magazine Version',
                                                    journal="Best Magazine", year=2008, volume="2", number="3", pages="45-50", ref_type="homework"))
