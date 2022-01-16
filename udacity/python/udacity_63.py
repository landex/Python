# Dictionary now using get method
# Building Dictionaries
# Using for loo
book_title = ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

# Create empty dictionary
word_count = {}

# Create loop for with get
for word in book_title:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)