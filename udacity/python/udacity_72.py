# SOlutions Udacity
# While loop

# number to fin the factorial of
number = 6

# start with our product equal to one
product = 1

# track the current number beig multiplied
current = 1

# Start the while loop
while current <= number:
    # multiply the product so far by the current number
    product *= current
    #-> Increment current with each iteration until it reacher number
    current += 1

# print the factorial of number
print(product)