# Continue actives with sets
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] #-> Created list with 10 elements
b = set(a) #-> the list is changed to list of unique elements
b.add(5) #-> Now is added the element 5
print(b) #-> Display the new list of unique elements
b.pop() #-> Is removed with away form the one element of list
print(b) #-> Print the list with unique elements