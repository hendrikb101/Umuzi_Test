def numbers(a, b, c):
    if a > b :
        max_num = a
    elif b > c:
        max_num = b
    elif c > a :
        max_num = c
    print(str(max_num))

numbers(12,20,30)
