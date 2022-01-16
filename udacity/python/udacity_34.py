# Compoud Data Structure

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
            "helium":   {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

# Access the element in dictionary
print(elements["helium"]) #-> print the helium info
print(elements["hydrogen"]["weight"]) #-> pritn the weight of hydrogen

# We can add a new key to element in out dictionary
oxygen = {"number" :8, "weight": 15.999, "symbol": "O"}
elements["oxygen"] = oxygen #-> Assign 'oxyge' as key to elements dictionary

print(elements)

# TEsting new dictionary structure
print(elements["oxygen"])