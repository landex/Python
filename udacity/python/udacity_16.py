# Data Stricture in Python

# List is a data structure ordened, the elements are arranged by index.
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# print the index of list
print(months[0]) #-> Will print the index 0 in this case January
print(months[1]) #-> Will print the index 1 in this case February
print(months[2]) #-> Will print the index 7 in this case August

# The index is the distance of element in list, starting in position 0
# If we use -1 is to get last element, if we use -2 
print(months[-1]) #-> Print last element of list
print(months[-2]) #-> Print penultimate element of list

# Data Structures are containers that organize and group data types together in different ways.

# Slicing of datas, we can slice by quater exempla
quater_3 = months[6:9] #-> Store the months os index 6-> July, 7-> August, 8-> September, 9-> October
# print the quater
print(quater_3) 

# Or we can slice the by start of list, the first 6 months
first_half = months[:6]
print(first_half)
# Or end of list the last 6 months
second_half = months[6:]
print(second_half)

# The lentgh of list is the number of elements
greeting = 'Hello There'
print(len(greeting), len(months))

# We can use the IN or NOT IN to evaluate if object is included in right side or not included in right side
print('her' in greeting, 'her' not in greeting)
print('Sunday' in months, 'Sunday' not in months)

# List is muatable and string not is.
# Creating a new list
my_lst = [1,2,3,4,5]
my_lst[0] = 'one' #-> Will replace  the value 1 in position 0 of my list to value 'one' 
print(my_lst) #-> Print may list