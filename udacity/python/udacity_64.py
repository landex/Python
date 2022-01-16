# Interating Through DIctionaries with For loops

# The cast
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

# The for loop
for key in cast:
    print(key)

# Now create a method
for key, value in cast.items():
    print("Actor: {}        Role:{}".format(key, value))