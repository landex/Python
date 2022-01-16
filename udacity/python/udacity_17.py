# List Idenxing
#
# Use list indexing to determine how many days are in a particular month mabsed on the integer variable
# month, and store the value in the integer variable num_days.

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# Use list indexing to determine the number of a days in month
month = int(month-1)
num_days = days_in_month[month]

print(num_days)

# We have a second solution to this problem
days_in_month[month - 1]
print("second solution", num_days)