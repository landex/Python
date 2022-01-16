# Wich is dense Rio or San Francisco

# Variables that indicate the values of population and density
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

# Calculate the denisty population
san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Created the result variable that compare if san francisco have density great than Rio or False
result = san_francisco_pop_density > rio_de_janeiro_pop_density

# Print the result
print(result)