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

    def test_is_string_number_valid_integer(self):
        """
        Integer in string format is provided
        :return:
        """

        self.assertTrue(Ilan().is_string_number_valid('100'))

    def test_is_string_number_valid_float(self):
        """
        Float in string format is provided
        :return:
        """

        self.assertTrue(Ilan().is_string_number_valid('100.50'))

    def test_is_string_number_int_type(self):
        """
        Integer in integer format is provided
        :return:
        """

        self.assertFalse(Ilan().is_string_number_valid(100))

    def test_is_string_number_float_type(self):
        """
        Float in float format is provided
        :return:
        """

        self.assertFalse(Ilan().is_string_number_valid(100.50))

    def test_is_string_number_commas(self):
        """
        Input with commas
        :return:
        """

        expected = 1000
        actual = Ilan().is_string_number_valid('1,000')
        self.assertEqual(expected, actual)

    def test_is_string_number_multiple_points(self):
        """
        Input with multiple decimal points
        :return:
        """

        self.assertFalse(Ilan().is_string_number_valid('1.000.000'))

    def test_is_string_number_with_non_numeric(self):
        """
        Input with letters and special characters
        :return:
        """

        self.assertFalse(Ilan().is_string_number_valid('1000a!'))

    def test_is_string_number_with_negative(self):
        """
        Input with negative sign
        :return:
        """

        expected = -1000
        actual = Ilan().is_string_number_valid('-1000')
        self.assertEqual(expected, actual)





if __name__ == '__main__':
    unittest.main()