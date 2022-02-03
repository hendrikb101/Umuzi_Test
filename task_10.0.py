def compare(word1, word2):
    match = []
    for char1 in word1:
        for char2 in word2:
            if char1.casefold() == char2.casefold():
                match.append(char2)
    match = ", ".join(match)
    print("Common letters: " + match)

compare("dEar","ear")
