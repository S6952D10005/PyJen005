import unittest

from calculator import add, main


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-4, -6), -10)

    def test_add_zero(self):
        self.assertEqual(add(0, 7), 7)

    def test_add_float(self):
        self.assertAlmostEqual(add(1.5, 2.25), 3.75)

    def test_main_with_args(self):
        self.assertEqual(main(["8", "12"]), 20)


if __name__ == "__main__":
    unittest.main()
