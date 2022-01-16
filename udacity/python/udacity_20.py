# Wworking with list

VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'UMH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL',
         'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZ', 'MSFT', 'AAPL']

# Print tickets
print(VINIX[0]) #-> Print  the first occur of list that is C
print(VINIX[1]) #-> Print second occur

# We can see if some element is part of the list
check_one = 'GE' in VINIX
check_two = 'GOOGL' in VINIX

print('GE in the list ?', check_one)
print('GOOGL in the list ?', check_two)