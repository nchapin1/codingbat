def same_first_last(nums):
    """ Given an array of ints, return True if the array is length 1 or more, and the 
    first element and last element are equal """
    return len(nums) >= 1 and nums[0] == nums[-1] 

# Solution
# Observation: Inconsistent use of parenthesis throughout the codingbat examples, perhaps because multiple factors?
""" def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[-1]) """