def maximum(a, *nums):
    max_num = a
    for x in nums:
        if x > max_num:
            max_num = x
    return max_num


print(maximum(0, -1, 1,4,9,80))