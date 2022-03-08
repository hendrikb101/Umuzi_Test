def compare(word1, word2):
    first_word = set(word1.lower())
    sec_word = set(word2.lower())
    
    common_characters = (first_word & sec_word)
    for char in common_characters:
        char = ", ".join(common_characters)
    print("Common letters: ", char )
