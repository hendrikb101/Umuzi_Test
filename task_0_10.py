def compare(word1, word2):
    first_word = set(word1)
    sec_word = set(word2)
    
    print("Common letters: " + ", ".join(sorted(first_word.intersection(sec_word))))
    

compare("look","fool")
