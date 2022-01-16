# Tuples is immutables you cannot add or remove items from tuples or sort

# The tuple
dimensions = 52, 40, 100
length, width, height = dimensions#-> Unpacking tuple, to assigne information from a tuple
print("The dimensions are {}x{}x{}".format(length, width, height))

# Other examples of tuple
AngkorWat = (13.4125, 103.866667)
print(type(AngkorWat)) #-> Will print that class is type Tuple

# Format output
print("AngkorWat is at latitude: {}".format(AngkorWat[0])) #-> Print 13.4125
print("AngkorWat is at latitude: {}".format(AngkorWat[1])) #-> Print 103.866667

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

# We can store multiple variables
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} X {} X {}". format(length, width, height))

length, width, height = 52, 40, 100
print("The dimensions are {} x {} X {}".format(length, width, height))