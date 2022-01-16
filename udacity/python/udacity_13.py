#String Methods

my_string = "landi leite"

print(str.capitalize(my_string)) #-> Return the first letter capitalized

my_string_capitol = 'LANDI'

print(str.casefold(my_string_capitol)) #-> Return the all string with lowcase

print(str.center(my_string, 40,'*')) #-> Centralize the string and add a charecters

print(str.count(my_string, 'l', 0,7)) #-> Count occur of string or letter, and is optional pass the range to search

print(str.encode(my_string, encoding="utf-8", errors="strict")) #-> Enconding to UTF-8

print(str.endswith(my_string, 'leite',2,19)) #-> Will return true if find the sufix, is possible insert a range
