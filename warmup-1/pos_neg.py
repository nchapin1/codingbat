def pos_neg(a, b, negative):
    """Given two int values, return True if one is negative and one is positive.
    Except if the parameter negative is True, then return True only if both
    are negative"""
    if negative == True:
        return a < 0 and b < 0
    else:
        return (a > 0 and b < 0) or (a < 0 and b > 0)


# Solution
""" def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0)) """
