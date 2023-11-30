import os


class AppLibrary:
    def __init__(self):
        self.reset_application()

    def reset_application(self):
        os.system(f"{os.getenv('PSQL_SCHEMA_COMMAND','psql -f')} schema.sql")

    def load_test_data(self):
        os.system(f"{os.getenv('PSQL_SCHEMA_COMMAND','psql -f')} tests/test-schema.sql")
