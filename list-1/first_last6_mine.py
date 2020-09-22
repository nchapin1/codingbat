def first_last6(nums):
  if len(nums) <= 1 and 6 in nums:
    return True
  if nums[1:] or nums[:1] == 6:
    return True
  else:
    return False

# INCORRECT NEED TO FIX