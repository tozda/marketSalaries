# tozdautils.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from datetime import timedelta
from datetime import date
import logging

# file encoding windows-1250


def get_browser(param_incognito='', param_headless=''):
    """ Builds object driver in incoginto mode

    :param param_headless: use string 'headless' to run browser in this mode
    :param param_incognito: use string 'incognito' to run browser in this mode
    :return: object browser
    """

    chrome_options = Options()
    if param_incognito == 'incognito':
        chrome_options.add_argument("--incognito")

    if param_headless == 'headless':
        chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(options=chrome_options)

    return browser


def remove_new_line(string):
    """
    Get Off new line sign from string
    :param string:
    :return: string
    """

    string = re.sub('\n', ' ', string)

    return string


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger


class Calendar:
    def __init__(self):
        self.weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
                         'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
        self.today = date.today()

    def get_date_of_month_days(self, name_of_day, month, year):
        """
        On the basis of name of day, month (int) and year (int) returns
        array of dates for given name of date within provided month
        :param name_of_day: string, name of day
        :param month: int, number of moth
        :param year: int, year
        :return dates: list, dates
        """

        # verify if provided name of day is any
        # day name
        if self.is_name_day_verified(name_of_day):

            # Get the date of first day
            day_id = self.weekdays[name_of_day]
            # define start date
            first_day = date(year, month, 1)
            while first_day.weekday() != day_id:
                first_day += timedelta(days=1)

            # having fist date iterate through
            # the complete month to get all dates
            dates = []
            while first_day.month == month:
                dates.append(first_day)
                first_day += timedelta(weeks=1)

        return dates

    def is_name_day_verified(self, name_of_day):
        """
        Verifies if provided name of day comply with predefined
        list of weekdays in classes' variable 'weekdays'.

        :return:
        """

        # fist check if this is string
        if not isinstance(name_of_day, str):
            print("Name of day is not type of 'string'!")
            return False

        # then check if exists in weekdays dictionary
        for d in self.weekdays:
            if d == name_of_day:
                return True

        print("Name of day is not recognizable!")
        return False