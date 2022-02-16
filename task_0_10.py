def compare(word1, word2):
    match = []
    for char1 in word1:
        for char2 in word2:
            if char1.casefold() == char2.casefold():
                match.append(char2)
    
    new_match = []
    for a in match:
        if a not in new_match:
            new_match.append(a)
    new_match = ", ".join(new_match)
    print(f"Common letters: {new_match}")

compare("look","fool")