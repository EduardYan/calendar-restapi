"""
Have data of holidays
for return is each month.
"""

from models.holiday import Holiday

# add to this list for more holidas
HOLIDAYS = [
  Holiday("January", "1", "1", "New Year"),
  Holiday("February", "2", "14", "Valentin's Day"),
  Holiday("December", "12", "25", "Christmas"),
  Holiday("October", "10", "1", "Children's Day")
]