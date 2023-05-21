import unittest
from task1 import mainClass


class mainClassTests(unittest.TestCase):
    def test_positive_case(self):
        with mainClass('exampleTest.txt', 'w') as temp_file:
            temp_file.write('Hello, world!')
            temp_file.flush()

            with mainClass(temp_file.name, 'r') as file:
                contents = file.read()
                self.assertEqual(contents, 'Hello, world!')

        self.assertTrue(file.closed)
        self.assertEqual(file.mode, 'r')

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            with mainClass('nonexistent_file.txt', 'r') as file:
                contents = file.read()

    def test_exception_in_context_suite(self):
        with self.assertRaises(ValueError):
            with mainClass('example.txt', 'r') as file:
                raise ValueError('Some error occurred.')




if __name__ == '__main__':
    unittest.main()