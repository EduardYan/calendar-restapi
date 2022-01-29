"""
This file have some utils functions to use
in the server.
"""

from calendar import Calendar
from data.months import OPTIONS_MONTHS
from data.holidays import HOLIDAYS
from messages.errors import MONTH_NAME_INVALID

class YearInvalid(TypeError):
  """
  Class in case the year passed
  for parameter is bad or invalid.
  """

  pass

class MonthInvalid(TypeError):
  """
  Class in case the month passed
  for parameter is bad or invalid.
  """

  pass

def get_calendar(year:str, month = 'all') -> list:
  """
  Return a list validating
  if the month is passed, is the month 
  not is passed return a list with all the year.
  """

  if not year.isdigit():
    raise YearInvalid('The year passed for parameter not is valid.')

  if month not in OPTIONS_MONTHS:
    raise MonthInvalid('The month passed for parameter not is valid.')

  else:
    calendar = Calendar() 

    if month != 'all':
      all = calendar.monthdayscalendar(
        int(year),
        int(month)
      )
      return all

    else:
      # in case all the calendar
      all = calendar.yeardayscalendar(
        int(year),
        width=12
      )
      return all


def validate_month_name(month_name:str) -> int:
  """
  Return the number of the month passed for parameter.
  """

  # validating the type of data
  if type(month_name) not in [str]:
    raise TypeError(MONTH_NAME_INVALID)

  # validating
  if month_name == 'January':
    return '1'
  elif month_name == 'February':
    return '2'
  elif month_name == 'March':
    return '3'
  elif month_name == 'April':
    return '4'
  elif month_name == 'May':
    return '5'
  elif month_name == 'June':
    return '6'
  elif month_name == 'July':
    return '7'
  elif month_name == 'August':
    return '8'
  elif month_name == 'September':
    return '9'
  elif month_name == 'October':
    return '10'
  elif month_name == 'November':
    return '11'
  elif month_name == 'December':
    return '12'
  else:
    return 'The month not is valid'


def get_holidays(month:str) -> list:
  """
  Return a list with the holidays
  of the month passed for parameter.
  """

  for holiday in HOLIDAYS:
    # validating for name and number of the month
    if month == holiday.month_name or month == holiday.month_number:
      return [holiday.name]