from ultraboost.paskoba.lib.araw import Araw
import unittest
import datetime


class TestAraw(unittest.TestCase):

    def test_get_current_date_with_tz_return_type(self):
        """
        Tests if the return type is datetime.datetime
        :return:
        """
        a = Araw()
        self.assertTrue(isinstance(a.get_current_date_with_tz('Asia/Manila'),
                                   datetime.datetime))

    def test_get_simple_date_return_type(self):
        """
        Tests if the return type is string
        :return:
        """
        a = Araw()
        self.assertTrue(isinstance(a.get_simple_date(),
                                   str))

    def test_is_today_christmas(self):
        """
        Tests is_today_christmas
        :return:
        """
        a = Araw()
        expected = False, 99.73
        actual = a.is_today_christmas()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()