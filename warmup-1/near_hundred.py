def near_hundred(n):
    """ Given int n, return True if it is within 10 or 100 
    or 200. """
    return (90 <= n <= 110 or 190 <= n <= 210)

# Note: I calculated two separate ranges 
# Solution
""" def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10)) """

# ((abs(100 - n) <= 10)) 
# Return True if the absolute value of the difference between 100 and n is less than or equal to 10