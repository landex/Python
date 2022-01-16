# The quis of verse, count unique words

# To store a big variable
verse = """
        if you can keep your head when all about you are losing theirs and blaming it on you
        if you can trust yourself when all men doubt you   
        but make allowance for their doubting too   
        if you can wait and not be tired by waiting      
        or being lied about  don’t deal in lies   
        or being hated  don’t give way to hating      
        and yet don’t look too good  nor talk too wise
                                                    """
#-> Print the verse
print(verse, '\n')

# Split verse in words
verse_list = verse.split() #-> this will split the verse in list
print(verse_list, '\n') #-> To print

# Convert a list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the numnber of unique words
num_unique = len(verse_set)
print(num_unique, '\n')