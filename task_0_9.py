def check_vowels(text):
    my_word = []
    text_lower = set(text.lower())

    for char in text_lower:
        if char in ['a','e','i','o','u']:
            my_word.append(char)
    my_word = ", ".join(my_word)
    print(f"Vowels:  {my_word}")


check_vowels("Umuuuzi")