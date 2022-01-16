# This program is to work with date
# In this program we will calculating the 2 things
# Age of Person
# Time to next bithday

# Import the date library
from datetime import datetime

# In the first part ot the program inform you birth day
print('Inform the date of you born, in this format: MM-DD-YYYY')
birth_day = input()

# Display to user the date informed
print(birth_day)

# converting the string to date format using str
date_object = datetime.birth_day(str, '%m-%d-%Y')

print('The date converted is\n')
print(date_object)
