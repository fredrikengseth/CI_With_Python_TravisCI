import unittest
from app import add_numbers


class MyTest(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 1), 2)
        self.assertEqual(add_numbers(1, -1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-1, -1), -2)
        self.assertEqual(add_numbers(1.0, 1), 2)
        self.assertEqual(add_numbers(1.1, 1.1), 2.2)
        # 1 + 1 = 4
        self.assertEqual(add_numbers(1, 2), 4)
        # 1 + 3 = 5
        self.assertEqual(add_numbers(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
