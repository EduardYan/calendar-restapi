"""
Test for data.months
"""

import sys
sys.path.append('..')

import unittest
from data.months import OPTIONS_MONTHS

class TestMonths(unittest.TestCase):
  def setUp(self) -> None:
      print('setUp')

      self.good_options = [
        'all',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'
      ]

  def tearDown(self) -> None:
      print('tearDown')

  def test_compare_list(self):
    self.assertEqual(self.good_options, OPTIONS_MONTHS)