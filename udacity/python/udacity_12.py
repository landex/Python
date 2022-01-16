# String Methods

print(len("Olá Mundo")) #-> Show the length of string

# Declare a variable string
my_string = "landi leite" #-> This is my string

print(my_string)

print(my_string.islower()) #-> Verify is my string was write in lower characters

print(my_string.count('l')) #-> Will count the letters "l" exist in my string

print(my_string.find('a')) #-> WIll find the position of "l" letter in my string

# Format String
print("Mohammed has {} ballons".format(27))

# Other example, using strings
animal = "dog"
action = "bite"
print("Does you {} {} ?".format(animal, action))

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))