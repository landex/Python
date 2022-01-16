# '''
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''

# Use rando to select state code
import random
from random import randrange
state_code_list = ['CA','MN','NY']

state = random.choice(state_code_list)#-> Either CA, MN, or NY
purchase_amount = randrange(10,99)#-> amount of purchase

# To us know the values selected by code
print("The state code is {} and the total purchase amount is {} .".format(state,purchase_amount))


if state == 'CA': #-> Provide conditional for checkin state is CA
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, you total cost is {}.".format(state, total_cost)
elif state == 'MN': #-> Provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
elif state == 'NY': #-> Provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)