# Using for loop to change a list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

#-> Created capitalized cities
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

# Print the new list
print(capitalized_cities)