import os


class AppLibrary:
    def __init__(self):
        self.reset_application()

    def reset_application(self):
        os.system("psql -f schema.sql")

    def load_test_data(self):
        os.system("psql -f tests/test-schema.sql")
