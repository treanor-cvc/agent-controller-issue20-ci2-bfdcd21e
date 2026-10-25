import unittest

from feature_a import add


class AddBehaviorTests(unittest.TestCase):
    def test_positive_operands(self):
        self.assertEqual(add(7, 12), 19)

    def test_negative_operands(self):
        self.assertEqual(add(-7, -12), -19)

    def test_mixed_sign_operands(self):
        for left, right, expected in ((12, -7, 5), (-12, 7, -5), (7, -7, 0)):
            with self.subTest(left=left, right=right):
                self.assertEqual(add(left, right), expected)
                self.assertEqual(add(right, left), expected)

    def test_zero_operands(self):
        for value in (0, 15, -15):
            with self.subTest(value=value):
                self.assertEqual(add(value, 0), value)
                self.assertEqual(add(0, value), value)

    def test_arbitrary_precision_integers(self):
        self.assertEqual(add(2 ** 100, 2 ** 100), 2 ** 101)
        self.assertEqual(add(-(2 ** 100), -1), -(2 ** 100) - 1)


if __name__ == "__main__":
    unittest.main()
