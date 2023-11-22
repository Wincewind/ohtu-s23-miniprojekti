import unittest
import dataprocessing
from app import app


class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_book(self):
        with app.app_context():
            self.assertEqual(True, dataprocessing.add_book("Wincewind","My Life",2000,"My mom","123 Noway Street"))