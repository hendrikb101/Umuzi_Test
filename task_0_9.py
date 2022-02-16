def check_vowels(text):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    my_word = []
    text_lower = set(text.lower())

    for char in text_lower:
        for vowel in vowels:
            if char == vowel:
                my_word.append(char)
    my_word = ", ".join(my_word)
    print(f"Vowels:  {my_word}")


check_vowels("Umuzi")