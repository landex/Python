# ZIP Function

# manifest = [("bananas", 15), ("mattresses", 34), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

items = ['bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses']

weights = [15, 34, 42, 120, 5]

print(list(zip(items, weights)))

# The second solution for this
for cargo in zip(items, weights):
    print(cargo[0], cargo[1])
