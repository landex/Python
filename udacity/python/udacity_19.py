# Working with list
sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register","a","complaint", "."]

# The code and results
sentence2[6]="!"

print("This is result of sentence2[6]=\"!\" = ", sentence2)

sentence2[0]="Our Majesty"

print("This is result of sentece2[0]=\"Our Majesty\" = ", sentence2)

#sentence1[30]="!"

print("This is result of sentence1[30]=\"!\" = ",sentence1)

sentence2[0:2] = ["We", "want"]

print("This is result of sentence2[0:2] = [\"We\", \"want\"] = ", sentence2)