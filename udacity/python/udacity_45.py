# Using Truth Values of Objects

from random import randrange

points = randrange(0,200)

print(points, "Points used in if and else validation")

# Validating the points
if points <=50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a peguin!"

print(result)