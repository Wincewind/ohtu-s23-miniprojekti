import os
from dotenv import load_dotenv
from pathlib import Path

BOOK_FORM_ELEMENTS = ["authors", "title", "year", "publisher", "publisher_address"]
ARTICLE_FORM_ELEMENTS = ["authors", "title", "journal", "year", "volume", "number", "pages"]

BOOK_COL_INDEXES = [1,2,3,4,5]
ARTICLE_COL_INDEXES = [1,2,3,6,7,8,9]

TEST_INPUT_1 = [
    ("authors","Mariot Tsitoara"),
    ("title","Beginning Git and GitHub"),
    ("year","2019"),
    ("publisher","APress"),
    ("publisher_address","One New York Plaza, Suite 4600 New York, NY")
]
TEST_INPUT_2 = [
    ("authors","Hawking, Stephen"),
    ("title","A Brief History of Time: From the Big Bang to Black Holes"),
    ("year","1988"),
    ("publisher","Bantam"),
    ("publisher_address","Random House Academic Marketing, 1745 Broadway, 20th Floor, New York")
]

TEST_INPUT_3 = [

    ("authors","Lijia Chen, Pingping Chen, Zhijian Lin"),
    ("title","Artificial Intelligence in Education: A Review"),
    ("year","2020"),
    ("journal","IEEE Access"),
    ("volume","8"),
    ("number",""),
    ("pages","75264-75278")
]

DOI_3 = "10.1109/ACCESS.2020.2988510"

PATH_TO_GENERATED_BIBTEX = str(Path.home() / "Downloads" / "exportedReferences.bib")
EXPECTED_BIBTEX_FOR_INPUT_1 = ("@book{MARIOT1, "
                                "author = {Mariot Tsitoara}, "
                                "title = {Beginning Git and GitHub}, "
                                "year = {2019}, publisher = {APress}, "
                                "address = {One New York Plaza, Suite 4600 New York, NY}}")
EXPECTED_BIBTEX_FOR_INPUT_3 = ("@article{LIJIA2, "
                               "author = {Lijia Chen, Pingping Chen, Zhijian Lin}, "
                               "title = {Artificial Intelligence in Education: A Review}, "
                               "journal = {IEEE Access}, "
                               "year = {2020}, "
                               "volume = {8}, "
                               "number = {null}, "
                               "pages = {75264-75278}}")

class AppLibrary:
    def __init__(self):
        load_dotenv()

    def reset_application(self):
        os.system(f"{os.getenv('PSQL_SCHEMA_COMMAND','psql -f')} schema.sql")

    def load_test_data(self):
        os.system(
            f"{os.getenv('PSQL_SCHEMA_COMMAND','psql -f')} src/tests/test-schema.sql"
        )

    def validate_generated_book_bibtex_file(self):
        generated_output = open(PATH_TO_GENERATED_BIBTEX, encoding="utf-8").read()
        if EXPECTED_BIBTEX_FOR_INPUT_1 == generated_output:
            pass
        else:
            raise ValueError("The generated BibTex contents didn't match expected values.")
        
    def validate_generated_bibtex_file_for_multiple_references(self):
        generated_output = open(PATH_TO_GENERATED_BIBTEX, encoding="utf-8").read().split("\n")
        if EXPECTED_BIBTEX_FOR_INPUT_1 != generated_output[0]:
            raise ValueError("The generated BibTex contents for book didn't match expected values.")
        if EXPECTED_BIBTEX_FOR_INPUT_3 != generated_output[1]:
            raise ValueError("The generated BibTex contents for article didn't match expected values.")

    def get_variables(self):
        return {
            "BOOK_COL_INDEXES": BOOK_COL_INDEXES,
            "ARTICLE_COL_INDEXES": ARTICLE_COL_INDEXES,
            "TEST_INPUT_1": TEST_INPUT_1,
            "TEST_INPUT_2": TEST_INPUT_2,
            "TEST_INPUT_3": TEST_INPUT_3,
            "DOI_3": DOI_3,
            "PATH_TO_GENERATED_BIBTEX": PATH_TO_GENERATED_BIBTEX,
        }
