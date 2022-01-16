# Working with for

# List of cities
cities = ['new yoork city', 'mountain view', 'chicago', 'los angeles']

for city in cities:#|-> Start the for loop  
    print(city)
print("Done!!!")

# Using range in for functions
for i in range(3):
    print("Hello")

# In function range we can use 3 values
#-> Start, Stop and Step
for i in range (3,16,3):
    print(i)

# Using for loop to capitalize a list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for city in cities:
    print(city.title()) #-> Print capitalizing the first consoant)
