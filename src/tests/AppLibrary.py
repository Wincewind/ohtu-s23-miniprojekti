import os
from dotenv import load_dotenv
from pathlib import Path

FORM_ELEMENTS = ["authors", "title", "year", "publisher", "publisher_address"]
TEST_INPUT_1 = [
    "Mariot Tsitoara",
    "Beginning Git and GitHub",
    "2019",
    "APress",
    "One New York Plaza, Suite 4600 New York, NY",
]
TEST_INPUT_2 = [
    "Hawking, Stephen",
    "A Brief History of Time: From the Big Bang to Black Holes",
    "1988",
    "Bantam",
    "Random House Academic Marketing, 1745 Broadway, 20th Floor, New York",
]
PATH_TO_GENERATED_BIBTEX = str(Path.home() / "Downloads" / "exportedReferences.bib")
EXPECTED_BIBTEX_FOR_INPUT_1 = ("@book{MARIOT1, "
                                "author = {Mariot Tsitoara}, "
                                "title = {Beginning Git and GitHub}, "
                                "year = {2019}, publisher = {APress}, "
                                "address = {One New York Plaza, Suite 4600 New York, NY}}")


class AppLibrary:
    def __init__(self):
        load_dotenv()

    def reset_application(self):
        os.system(f"{os.getenv('PSQL_SCHEMA_COMMAND','psql -f')} schema.sql")

    def load_test_data(self):
        os.system(
            f"{os.getenv('PSQL_SCHEMA_COMMAND','psql -f')} src/tests/test-schema.sql"
        )

    def validate_generated_bibtex_file(self):
        generated_output = open(PATH_TO_GENERATED_BIBTEX, encoding="utf-8").read()
        if EXPECTED_BIBTEX_FOR_INPUT_1 == generated_output:
            pass
        else:
            raise ValueError("The generated BibTex contents didn't match expected values.")

    def get_variables(self):
        return {
            "FORM_ELEMENTS": FORM_ELEMENTS,
            "TEST_INPUT_1": TEST_INPUT_1,
            "TEST_INPUT_2": TEST_INPUT_2,
            "PATH_TO_GENERATED_BIBTEX": PATH_TO_GENERATED_BIBTEX,
        }
