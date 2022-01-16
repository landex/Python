# Continue works with list
scores = ["B", "C", "A", "D", "B", "A"]
grades = scores

print("scores:" + str(scores) )
print("grades:" + str(grades) )

# We can chage a score value in the list
scores[3] = "B"

# Now we will print score with new vale
print("scores:" + str(scores) )
print("grades:" + str(grades) )

# Using some funcions >-> len() >-> max() >-> min()

# Using max() in list with numbers will be returned the large numbers
batch_sizes = [16, 6, 89, 34, 65, 35]
print(max(batch_sizes)) #-> return 89 that is the large value of list

# Using max() in list of strings, will be returde according alphabetic order
python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python',
'Reticulate Python', 'Angolan Python']
# Use print to retunr the max value
print(max(python_varieties)) #-> return Reticulate Python

# Using interger and string will be return error if use these functions

# Using min() to return the minimal value of the list
print(min(batch_sizes)) #-> return the 6
print(min(python_varieties)) #-> return African Rock Python

# Sorted will organize the list in order
print(sorted(batch_sizes)) #-> will organize the numbers from minor to max
print(sorted(python_varieties)) #-> Will organize the string in alphabetic order

# Sorted we can use in reverser order
print(sorted(batch_sizes, reverse=True)) #-> organize number in reverse order
print(sorted(python_varieties, reverse=True))