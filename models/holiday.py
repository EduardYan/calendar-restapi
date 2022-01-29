"""
This module have the model
for a holiday in the calendar.
"""

class Holiday:
  """
  Model for a holiday.

  Properties:
  month_name:str
  month_number:str
  day:str
  name:str

  """
  def __init__(self, month_name:str, month_number:str, day:str, name:str) -> None:
    # name and number
    self.month_name = month_name
    self.month_number= month_number
    self.day = day
    self.name = name