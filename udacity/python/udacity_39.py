# Using IF, ELIF and ELSE
import random #-> to use a random values from list
# List of year season
season_list = ['spring','summer','fall','winter','none']

season = random.choice(season_list) #-> get season from list

print("Selected season is", season) #-> Print season selected from list

# IF, ELIF and ELSE block

if season == "spring": 
    print("plant the garden!")
elif season == "summer":
    print("water the garden!")
elif season == "fall":
    print("hrvest the garden!")
elif season == "winter":
    print("stay indoors!")
else:
    print("unrecognized season")