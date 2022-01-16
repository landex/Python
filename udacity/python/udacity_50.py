# Using range to get index of list
cities = ['new york city', 'mountain view', 'chicado', 'los angeles']

for index in range(len(cities)): #->We get the index len, in this case is 4 positions
    cities[index] = cities[index].title() #-> Create number of the list according number of index
    print(cities) #-> Print the lists created