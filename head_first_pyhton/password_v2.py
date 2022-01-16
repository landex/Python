# This program is version: 2.0
# This program validate if and else interation.
# This program hidden the password inputed by user.
# In this program the input file have an User | Password


# Library to hidden password.
from getpass import getpass

# To read input file with user and password.
file_handle = open('user_and_password.txt','r')
for line in file_handle:
    fields = line.split('|')
    stored_user = fields[0]
    stored_password = fields[1]
file_handle.close()

# To inpt user name
print ('Enter your user name.')
typed_user = input()

# Request to user inform the password
print('Enter you password.')
# To type password hidden values
typed_password = getpass('Password:')

# Conditional to validate the user and password

if typed_user not in [stored_user]:
    print ('Invalid user name')

elif typed_password == stored_password:
    print ('Access granted!!!')

elif typed_password == '123456':
    print('That password is one that an idiot puts on their luggage.')

else:
    print('Acess denied!')