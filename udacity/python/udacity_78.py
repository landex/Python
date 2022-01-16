# For loop with break

manifest = [("bananas", 15), ("mattresses", 34), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

weight = 0
items = []

for cargo in manifest:
    if weight >= 100:
        break
    else:
        items.append(cargo[0])
        weight += cargo[1 ]

print(weight)
print(items)