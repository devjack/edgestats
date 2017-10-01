import unittest
import gzip
from edgestats import EdgeStats

class EdgestatsTest(unittest.TestCase):
    def test_can_parse_log_file(self):
        with gzip.open('tests/data/simple_unzip_test.gz', 'rb') as f:
            file_content = f.read()
        expected = b"Simple gzipped string\n"
        self.assertEqual(expected, file_content)

if __name__ == '__main__':
    unittest.main()
