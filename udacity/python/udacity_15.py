# This activity is to work wuth string libary
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
#print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
message = "The lenght of the verse is {}, the index of the first occurence of word 'and' in verser is {}, the last occurrences of the word 'you' in verser {}, the count of occurrences of the word 'you' in verse is {}"

#-> 1 - What is the length of the string variable verse?
print(len(verse))
length_verse = len(verse)

#-> 2 - What is the index of the first occurrence of the word 'and' in verse?
print(str.index(verse, 'and')) #-> Return the index
first_index = verse.find('and')

#-> 3 - What is the index of the last occurrence of the word 'you' in verse?
print(str.rindex(verse, 'you'))
last_index = verse.rfind('you')

#-> 4 - What is the count of occurrences of the word 'you' in the verse?
print(str.count(verse, 'you')) #-> This command count occur of string you
count_verse = verse.count('you')

print(message.format(length_verse, first_index, last_index, count_verse))