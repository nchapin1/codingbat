""" def first_last6(nums):
  if len(nums) <= 1 and 6 in nums:
    return True
  if nums[1:] or nums[:1] == 6:
    return True
  else:
    return False

def first_last6(nums):
  if nums[1:] or nums[:-1] == 6:
    return True
  elif len(nums) == 1 and 6 in nums:
    return True
  else:
    return False """

# Not my solution! I attempted this question for hours (2). My logic is to view similar answers to this
# type of question and to see how the different tools may be manipulated. I learned from both the solution and
# this answer that I was on the right track by specifying nums[] == 6, but I need to generalize more. Too much
# complexity made this question cumbersome to understand.
def first_last6(nums):
    """Given an array of ints, return True if 6 appears
    as either the first or last element in the array. The
    array will be length 1 or more."""
    return nums[0] == 6 or nums[-1] == 6


# Solution
""" def first_last6(nums):
  return (nums[0]==6 or nums[-1]==6) """
