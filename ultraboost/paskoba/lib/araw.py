import pytz
from datetime import datetime


class Araw(object):

    @staticmethod
    def get_current_date_with_tz(time_zone):
        """
        Gets the current date with the specified time zone
        :param time_zone: Location to get the local time of
        :return datetime.datetime: Current date and time
        """

        tz = pytz.timezone(time_zone)
        return datetime.now(tz)

    def get_simple_manila_date(self):
        """
        Gets the current date in Asia/Manila and converts it to string
        :return str: month-day-year hour:minute
        """

        manila = self.get_current_date_with_tz('Asia/Manila')
        return f'{manila.month}-{manila.day}-{manila.year}  {manila.hour}:{manila.minute}'