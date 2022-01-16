# Resolution by Udacity of variables exercice

# The current volume of water
reservoir_volume = 4.445e8

# Rain faull volume
rainfall = 5e6

# decrease 10% of rainfall
rainfall *= .9 #-> With this we indicate to consider 90% of value

# add rainfall to reservoir_volume
reservoir_volume += rainfall

# increase in the reservoir_volume the stormwater is 5%
reservoir_volume *= 1.05 #-> Indicate the 105% of value is the same of 100% of value + 5%

# decrease the reservoir_volume 5% by evaporation
reservoir_volume *= 0.95

# subtraction of 2.5e5 
reservoir_volume -= 2.5e5

# print the result
print(reservoir_volume)