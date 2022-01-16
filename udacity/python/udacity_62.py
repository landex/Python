# Building Dictionaries
# Using for loo
book_title = ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

# Create empty dictionary
word_count = {}

# Create loop for
for word in book_title:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
print(word_count)