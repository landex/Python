#Sets is used to remove the duplicated values of list
contries = ['Angola', 'Maldives', 'India', 'United States', 'India', 'Denmark','Sweden', 'Ghana', 'Italy',
'Canada', 'Sweden', 'United States', 'Brazil', 'Italy', 'Brazil', 'Mexico', 'Canada', 'Poland','Norway']

print(len(contries)) #-> Print the length of contries the result is = 19 because we have repeated countries

print(contries[:5]) #-> Print the first five countries

# Now using set we will remove the repeated countries of the list.
country_set = set(contries) #-> Now the contry_set have only one entrie in their list
print(country_set) #-> Now will print the 13 contries

# We can add a contry in our set
country_set.add('Germany')
print(country_set) #-> Now Germany is added

# Set is a data type for mutable unordered collections of unique elements, is used to remove duplicates from the list
numbers = [1,2,6,3,1,1,6]
print(numbers)
# now remove the duplicated using set
unique_num = set(numbers)
print (unique_num)

# Sets support the IN operator, ADD method to add elements and POP to remove.
fruit = {"apple", "banana", "orange", "grapefruit"}
print("watermelon" in fruit) #Check for element -> Return FALSE
print("apple" in fruit) #Check for element -> Return TRUE

# Now to add element
fruit.add("watermelon") #-> Added watermelon in fruid list
print(fruit) #-> Print the list
print("watermelon" in fruit) #-> Check element in list, now will return TRUE

# Now to remove one element
print(fruit)
fruit.pop()#-> Removed one random element
print(fruit)