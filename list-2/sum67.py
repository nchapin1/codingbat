def sum67(nums):
    """Return the sum of the numbers in the array, except ignore sections of numbers
    starting with a 6 and extending to the next 7 (every 6 will be followed by at least
    one 7). Return 0 for no numbers."""
    for n in range(0, len(nums)):
        if nums[n] == 6:
            nums[n] = 0
            for i in range(n + 1, len(nums)):
                temp = nums[i]
                nums[i] = 0
                if temp == 7:
                    n = i + 1
                    break
    return sum(nums)
