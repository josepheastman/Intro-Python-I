"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


month_input = input('Month: ')
year_input = input('Year: ')
month = datetime.today().strftime('%m')
year = datetime.today().strftime('%Y')

if month_input == "" and year_input == "":
    month
    year
    print(calendar.month(int(year_input), int(month_input)))
elif year_input == "" and month_input != None:
    if month_input.isdigit():
        year
        print(calendar.month(int(year_input), int(month_input)))
    else:
        print('Please input a number for the month.')
elif month_input == "" and year_input != None:
    if year_input.isdigit():
        month
        print(calendar.month(int(year_input), int(month_input)))
    else:
        print('Please input a number for the year.')
else:
    if month_input.isdigit() and year_input.isdigit():
        print(calendar.month(int(year_input), int(month_input)))
    else:
        print('Please input numbers for the month and year.')
