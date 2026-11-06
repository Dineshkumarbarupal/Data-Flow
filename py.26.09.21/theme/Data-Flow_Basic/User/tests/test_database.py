import tempfile
import unittest
from pathlib import Path
from db.database import initialize_database, connect

class DatabaseTests(unittest.TestCase):
    def test_initialization_creates_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'test.sqlite3'
            initialize_database(path)
            with connect(path) as connection:
                row = connection.execute('SELECT version FROM schema_version').fetchone()
                self.assertEqual(row['version'], 1)

if __name__ == '__main__':
    unittest.main()
