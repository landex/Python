# Variables
# This program is to work with math in variables in python

# The current volume of a water resevoir in cubic metres
reservoir_volume = 4.445e8

# rainfall is the volume of cubique meters of water
rainfall = 5e6

# Decrease the rainfall by 10% to account for runoff
rainfall = (rainfall-(rainfall * 0.10))

# add rainfall variable to the reservoir_volume
reservoir_volume = reservoir_volume + rainfall

# Increase reservoir_volume by 5% to account for storwater that flow
# into the reservoir in the days following the storm
reservoir_volume = (reservoir_volume + (reservoir_volume * 0.05))

# Decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = (reservoir_volume - (reservoir_volume * 0.05))

# Subtract 3.5e5 cubic meter from resevoir_volume to account for water
# that's piped to arid regions
reservoir_volume = (reservoir_volume - 2.5e5)

# Print the result
print(reservoir_volume)

