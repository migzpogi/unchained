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


if __name__ == '__main__':
    unittest.main()