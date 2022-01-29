"""
Test for the helpers/utils module
"""

import sys
sys.path.append('..') # for add the other modules

import unittest
from calendar import Calendar
from helpers.utils import get_calendar


class TestUtils(unittest.TestCase):
  def setUp(self) -> None:
    print('setUp')

    # settings
    calendar = Calendar()
    self.good = calendar.yeardayscalendar(2022, width=12)

  def test_get_calendar(self):
    self.assertEqual(self.good, get_calendar(2022))

  def tearDown(self) -> None:
      print('tearDown')

if __name__ == '__main__':
  unittest.main()