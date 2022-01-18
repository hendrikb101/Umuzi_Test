word1 = str(input('Enter a word: '))
word2 = str(input('Enter a second word: '))
def compare(word1, word2):
    match = ""
    for char1 in word1:
        for char2 in word2:
            if char2 == char1:
                match = match + char2
    return match
match = compare(word1, word2)
print(match)
