# Name lenght

# The variables
give_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = give_name + ' ' + middle_names + ' ' + family_name #todo: calculate now long this name is.
name_length=len(name_length)
print(name_length)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you to do here
driving_licence_character_limit = 28
print(name_length <= driving_licence_character_limit)