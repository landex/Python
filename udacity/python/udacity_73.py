# Solutions factrial with for loops

# number we'll find the factorial of
number = 6

# start with our porduct equal to one
product = 1

# calculate factorial of number with a for loop
for num in range (2, number + 1):
    product *= num
#-> Print the factorial of number
print(product)