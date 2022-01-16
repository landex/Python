# Working Lists
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

# Print the lists
print("First - MAX")
print(max([len(a), len(b), len(c)]))
print("Second - MIN")
print(min([len(a), len(b), len(c)]))

# Using join in list
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

# Append and Lists
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))