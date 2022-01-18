a = 20
b = 60
c = 30
def numbers(a, b, c):
    if a > b :
        max_num = a
    elif b > c:
        max_num = b
    elif c > a :
        max_num = c
    return max_num
max_num = numbers(a, b, c)
print(str(max_num) + " is the highest number of the three")