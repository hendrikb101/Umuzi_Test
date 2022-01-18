text = "Umuzi"
def check_vowels(text):
    tot = ""
    for char in text:
        if char in 'aeiouAEIOU':
            tot = tot + char + ", "
    return tot
tot = check_vowels(text)
print("Vowels: " + tot)