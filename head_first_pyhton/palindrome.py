# This program will verify if word inpute by user is palindrome

# to get user input
print('Please digita any word...')
string_inputed = input()

# This condition is to remove spaces
string_inputed_stored = ''.join(string_inputed.split())

# To verify if scring is a palindrome
string_palidrome = string_inputed_stored [::-1]

if string_inputed_stored == string_palidrome:
    print('The string is palindrome', string_inputed)
else:
    print ('The string is not a palindrome')