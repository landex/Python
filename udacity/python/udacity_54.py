# Using for to change the user names

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)): #-> Using range, and len to get the lenght of range
    usernames[index] = usernames[index].lower().replace(" ", "_")
    

print(usernames)