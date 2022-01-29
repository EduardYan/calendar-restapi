"""
Hav the options for validate the months
"""

OPTIONS_MONTHS = [
  'all',
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December'
]

# adding the number to options list
for i in range(13):
  if i != 0: # if is 0 not add
    OPTIONS_MONTHS.append(str(i))