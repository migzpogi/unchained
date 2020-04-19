import unittest
from ultraboost.ilan.lib.ilan import Ilan


class TestIlan(unittest.TestCase):

    def test_get_qty_both_integers(self):
        """
        Total amount and price are both integers
        :return:
        """

        expected = 4
        actual = Ilan().get_qty(100, 25)
        self.assertEqual(expected, actual)

    def test_get_qty_both_float(self):
        """
        Total amount and price are both floating points
        :return:
        """

        expected = 8
        actual = Ilan().get_qty(100.0, 12.5)
        self.assertEqual(expected, actual)

    def test_get_qty_answer_is_float(self):
        """
        Answer is floating point but must be rounded down
        :return:
        """

        expected = 12
        actual = Ilan().get_qty(100, 8)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()