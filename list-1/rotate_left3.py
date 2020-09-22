def rotate_left3(nums):
    """Given an array of ints length 3, return an array with the elements "rotated left"
    so {1, 2, 3} yields {2, 3, 1}."""
    a = nums[1]
    b = nums[-1]
    c = nums[0]
    nums = [a, b, c]
    return nums


""" return nums[1], nums[-1], nums[0]  """
# Note: Initially wrote above. Returned values. Not correct because returning values in array, as
# opposed to rewriting the 'nums' array structure.

# Solution
# No solution available