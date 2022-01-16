# Practice: Factorials with While Loops
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while number > 1:
    # multiply the product so far by the current number
    number = number - current
    
    # increment current with each iteration until it reaches number
    product += product * number


# print the factorial of number
print(product)