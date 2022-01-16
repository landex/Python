# Importing the function
from os import getcwd
import sys

# Calling the function to use
where_am_i = getcwd()
my_computer = sys.platform
my_python = sys.version

# To print result of function called
print('Where am I:\n',where_am_i)
print('My computer:\n',my_computer)
print('The version of python interpreter:\n',my_python)
