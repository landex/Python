# Quiz with dictionary
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai" :17.8, "Istanbul" :13.3, "Karachi" :13.0, "Mumbai" :12.5}
print(population)

# Using get in dictionary
elements = {"hydrogen" :1, "helium" :2, "carbon" :6}
print(elements.get('dilithium')) #-> Try search 'dilithium' in dictionary -> Return None
print(elements.get('kryptonite', 'Ther\'s no such element!'))

# Check Equality vs Identity
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a)
print(b)
print(c)

print(a == b) #-> True
print(a is b) #-> True
print(a == c) #-> True
print(a is c) #-> True