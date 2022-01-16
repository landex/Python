# DIctionaries store pair of elements
# Dictionary is a mutable data type
elements = {"hydrogen" :1, "helium" :2, "carbon" :6}
print(elements["carbon"]) #-> Print the value mapped to "carbon"
elements["lithium"] = 3 #-> Insert "lithium" with a value of 3 into the dictionary
print(elements)

# Check if we have a element in the list
print("carbon" in elements) #-> Will returned true
print(elements.get("dilithium")) #-> Return NONE because we not have this value in dictionary

# Some keyword that we use in these examples
# is -> evaluates if both sides have the same identity
# is not -> evaluates if both sides have different identities
n = elements.get("dilithium") #-> Will return none, because we not have this element in dictionary
print (n is None) #-> is in this case indicate that the result of n is None -> Return TRUE -> Because the return is None
print (n is not None) #-> in this case inticate that the result of n is not None -> Return FALSE -> Because the return is None