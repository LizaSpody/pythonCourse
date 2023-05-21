# Pick your solution to one of the exercises in this module.
# Design tests for this solution and write tests using unittest library.

import unittest
import func_for_task1


class RangeTestCase(unittest.TestCase):
    def test_range(self):
        result = list(func_for_task1.in_range(0, 9, 2))
        self.assertEqual(result, list(range(0, 9, 2)))
        result = list(func_for_task1.in_range(9))
        self.assertEqual(result, list(range(9)))


if __name__ == '__main__':
    unittest.main()
