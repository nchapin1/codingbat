def has22(nums):
    """ Given an array of ints, return True if the array contains a 2 next to a 2 somewhere. """
    for n in range(0, len(nums) - 1):
        if nums[n] == 2:
            if nums[n + 1] == 2:
                return True
    return False
