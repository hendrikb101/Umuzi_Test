def maximum(*nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


print(maximum(0, -1, 1,4,9,80,100))
