# Improvements in program to show if the minute is even or odd 

# This library is necessary to work with date and time
from datetime import datetime

# Tho get the current minute of today
right_this_minute = datetime.today().minute

# to print the minute get in previous command.
print('The current minute is',right_this_minute)

# the function determine the minute is even or odd, using the 
right_this_minute = right_this_minute % 2

# The conditional compare the current minute is equals 0 to determine is even or odd
if (right_this_minute == 0):
    print('This minute seems a little even.')
else:
    print('This minute seem a little odd.')

