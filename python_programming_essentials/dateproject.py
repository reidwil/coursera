"""
This program works with dates
functions:
    days_in_months
    is_valid_date
    days_between
    age_in_days
"""

import datetime


def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if datetime.MINYEAR <= year <= datetime.MAXYEAR:
        cur_month = datetime.date(year, month, 1)
        try:
            next_month = datetime.date(year, month + 1, 1)
        except ValueError:
            next_month = datetime.date(year + 1, 1, 1)
        day_diff = next_month - cur_month
        return day_diff.days
    else:
        return f"Choose a year between {datetime.MINYEAR} and {datetime.MAXYEAR}"


def is_valid_date(year, month, day):
    """"
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if datetime.MINYEAR <= year <= datetime.MAXYEAR:
        if 1 <= month <= 12:
            if 1 <= day <= days_in_month(year, month):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) & is_valid_date(year2, month2, day2):
        first_date = datetime.date(year1, month1, day1)
        second_date = datetime.date(year2, month2, day2)
    else:
        return 0

    date_diff = second_date - first_date
    if date_diff.days >= 0:
        return date_diff.days
    else:
        return 0


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    today = datetime.date.today()
    today_year = today.year
    today_month = today.month
    today_day = today.day

    if is_valid_date(year, month, day):
        days_old = days_between(year, month, day, today_year, today_month, today_day)
        if days_old >= 0:
            return days_old
        else:
            return 0
    else:
        return 0
