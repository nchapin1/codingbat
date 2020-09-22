def reverse3(nums):
    """Given an array of ints length 3, return a new array with
    the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}."""
    a = nums[0]
    b = nums[1]
    c = nums[-1]
    nums = [c, b, a]
    return nums


# Solution
# No solution available
# Alternate solution
""" def reverse3(nums):
    return [nums[2], nums[1], nums[0]] """
# Notes: Can return new array using [] instead of assigning variables. Fix for previous issue in
# earlier exercise.