# Using for to create usernames

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

usernames = []
# Write you for loop here

for name in names:
    name = name.lower().replace(" ", "_")
    usernames.append(name)

print(usernames)
