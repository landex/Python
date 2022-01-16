# This program is version: 1.0
# This program validate if and else interation.
# This program hidden the password inputed by user.

# Library to hidden password.
from getpass import getpass

# Input file indication, that have the passwords.
password_file = open('passwords.txt')

# To read input file
secret_password = password_file.read()

# Request to user inform the password
print('Enter you password.')
# typed_password = input()

# To type password hidden values.
typed_password = getpass('Password:')

# Conditional to validate the password.
if typed_password == secret_password:
    print('Access granted!!!')

elif typed_password == '123456':
    print('That password is one that an idiot puts on their luggage.')

else:
    print('Acess denied!')
