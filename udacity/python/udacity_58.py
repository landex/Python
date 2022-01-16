# For with Range
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)): #-> Using len and range to get lenght of for loop
    usernames[i] = usernames[i].lower().replace(" ", "-")

print(usernames)