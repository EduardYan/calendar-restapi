"""
This file have the routes
for use in the server.
"""

from flask import Blueprint, jsonify
from helpers.utils import (
  MonthInvalid,
  YearInvalid,
  get_calendar,
  validate_month_name,
  get_holidays,
)
from messages.errors import YEAR_INVALID, MONTH_INVALID

# routes
calendars = Blueprint('calendars', __name__)

@calendars.route('/<year>/<month>', methods = ['GET'])
def home(year, month):
  try:
    # in case have a month
    if month != 'all':
      try:
        # getting the calendar
        calendar = get_calendar(year, month)
        holidays = get_holidays(month)
        print(holidays)

        # return the json
        return jsonify({
          'year': year,
          'month': month,
          'all': calendar,
          'holidays': holidays
        })

      except ValueError:
        month_name = month
        month = validate_month_name(month)
        calendar = get_calendar(year, month)
        holidays = get_holidays(month_name)

        return jsonify({
          'year': year,
          'month': month,
          'monthName': month_name,
          'all': calendar,
          'holidays': holidays
        })
    else:
      # getting the calendar
      calendar = get_calendar(year)
      holidays = get_holidays('all')

      return jsonify({
        'year': year,
        'month': month,
        'all': calendar,
        'holidays': holidays
      })


  except YearInvalid:
    return jsonify({
      'message': YEAR_INVALID
    })

  except MonthInvalid:
    return jsonify({
      'message': MONTH_INVALID
    })


@calendars.route('/get-holidays/<month>', methods = ['GET'])
def get_holidays_route(month):
  """
  Route for get the holidays of the month
  passed for parameter.
  """

  # getting holidays
  holidays = get_holidays(month)

  return jsonify({
    'month': month,
    'holidays': holidays
  })


@calendars.route('/about', methods = ['GET'])
def about():
  """
  Route for about.
  """

  return jsonify({
    'message': 'This is a restapi for calendars. Credits to Daniel Yanes.'
  })