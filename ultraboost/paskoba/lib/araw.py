import pytz
from datetime import datetime


class Araw(object):

    @staticmethod
    def get_current_date_with_tz(time_zone='Asia/Manila'):
        """
        Gets the current date with the specified time zone
        :param time_zone: Location to get the local time of
        :return datetime.datetime: Current date and time
        """

        tz = pytz.timezone(time_zone)
        return datetime.now(tz)

    def get_simple_date(self, time_zone='Asia/Manila'):
        """
        Gets the current date in Asia/Manila and converts it to string
        :param time_zone: Location to get the local time of
        :return str: month-day-year hour:minute
        """

        manila = self.get_current_date_with_tz(time_zone)
        return f'{manila.month}-{manila.day}-{manila.year}  {manila.hour}:{manila.minute}'

    @staticmethod
    def is_today_christmas():
        """
        Checks if it is Christmas day
        :return tuple: this always returns False with its accuracy (False, x%)
        """

        accuracy = round((364/365) * 100, 2)
        return False, accuracy

