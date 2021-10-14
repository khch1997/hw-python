def multiply_list(nums):
    product = 1
    for num in nums:
        if type(num) != int:
            return False
        product *= num
    return product