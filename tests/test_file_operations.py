import unittest
import os
from src.file_operations import write_to_file, read_from_file
class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_file.json'
        self.test_data = {
            "pk": 4,
            "title": "Test Title",
            "author": "Test Author",
            "published_date": "2024-06-23",
            "publisher": 6,
            "price": 9.99,
            "discounted_price": 3.56,
            "is_bestseller": True,
            "is_banned": False,
            "genres": [1, 2, 3]
        }

    def test_write_and_read_file(self):
        write_to_file(self.test_file, self.test_data)
        result = read_from_file(self.test_file)
        self.assertEqual(result, self.test_data)

    def test_write_and_read_empty_file(self):
        write_to_file(self.test_file, {})
        result = read_from_file(self.test_file)
        self.assertEqual(result, {})

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file('nonexistent_file.json')

    def test_write_bad_data_into_file(self):
        bad_data = set([1, 2, 3])  # Множество не поддерживается в JSON
        with self.assertRaises(TypeError):
            write_to_file(self.test_file, bad_data)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()
