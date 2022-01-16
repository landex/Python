# Exercice to add new value in a existing dictionary
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
# Print 
print(elements)
# hint: helium is a noble gas, hydrogen isn't
print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])
