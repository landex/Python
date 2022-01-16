# Quiz IF, ELIF and ELSE challenger

# Using random to generate de input
import random


points = random.randint(1,200) #-> To generated the random points value

# the messages
won_prize = "Congratulations! You won a {}!"
lost_game = "Oh dear, no prize this time"

print("You reach ", points) #-> Display the points

# Start IF and ELSE Block to check the prize winner or not winner
if points <= 50:
    result = won_prize.format("wooden rabbit")
elif points <= 150:
    result = lost_game
elif points <= 180:
    result = won_prize.format("wafer-thin mint")
elif points <= 200:
    result = won_prize.format("peguin")
else:
    print("Invalid Reusl")


print(result)