# Python using IF

# Import rando to us work with random numbers
from random import randrange
phone_balance = randrange(10) #-> Using random to get a phone balance

bank_balance = 100 #-> Variable of bank balance

print("Phone Balance is", phone_balance, "Bank Balance is", bank_balance)

if phone_balance < 5: # Check if phone balance is low of 5, if low code enter in flow below
    print("You phone balance is low of 5")
    phone_balance += 10
    bank_balance -= 10

print("Phone Balance is", phone_balance, "Bank Balance is", bank_balance)