from datetime import datetime

# To verify is number is odd
odds = [ 1, 3, 5, 7, 9,11,13,15,17,19,
        21,23,25,27,29,31,33,35,37,39,
        41,43,45,47,49,51,53,55,57,59]

# Tho get the current minute of today
right_this_minute = datetime.today().minute

# The conditional compare the current minute with list to verify the minute is odds.
if right_this_minute in odds:
    print('This minute seems a little odd.')
else:
    print('Not an odd minute.')

