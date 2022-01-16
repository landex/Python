# Solution Fruit Basket - Tasks 1&2
result = 0
basket_items =  {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Start the for
for object, count in basket_items.items():
    if object in fruits:
        result += count
# Print the result
print ("There are {} fruits in the basket.".format(result))


# Solution: Fruit Basket - Task 3
fruit_count, not_fruit_count = 0, 0

# The dictionary
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate throught the dictionary
for object, count in basket_items.items():
    if object in fruits:
        fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))