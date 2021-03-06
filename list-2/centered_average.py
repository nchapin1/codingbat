def centered_average(nums):
    """Return the "centered" average of an array of ints, which we'll say is the mean 
    average of the values, except ignoring the largest and smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, and 
    likewise for the largest value. Use int division to produce the final average. 
    You may assume that the array is length 3 or more."""
    imin = min(nums)
    imax = max(nums)
    return (sum(nums) - imin - imax)/(len(nums)-2)