import os
from dotenv import load_dotenv
from pathlib import Path

FORM_ELEMENTS = ['authors', 'title', 'year', 'publisher', 'publisher_address']
TEST_INPUT_1 = ['Mariot Tsitoara', 'Beginning Git and GitHub', '2019', 'APress', 'One New York Plaza, Suite 4600 New York, NY']


class AppLibrary:
    def __init__(self):
        load_dotenv()
        self.reset_application()

    def reset_application(self):
        os.system(f"{os.getenv('PSQL_SCHEMA_COMMAND','psql -f')} schema.sql")

    def load_test_data(self):
        os.system(f"{os.getenv('PSQL_SCHEMA_COMMAND','psql -f')} src/tests/test-schema.sql")

    def read_generated_file(self):
        downloads_path = str(Path.home() / 'Downloads')
        generated_output = open(str(downloads_path / 'exportedReferences.bib')).read()
