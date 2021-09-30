from typing import Counter


a = str(input('Enter a number: '))
b = str(input('Enter a number: '))
def compare(a, b):
    dict1 = Counter(a)
    dict2 = Counter(b)

    commonDict = dict1 & dict2

    if len(commonDict) == 0:
        print (-1)
        return

commonChars = list(commonDict.elements())

commonChars = sorted(commonChars)

print (''.join(commonChars))

