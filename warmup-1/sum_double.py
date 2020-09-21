def sum_double(a, b):
    """Given two int values, return their sum.
    Unless two values are same, return double their sum"""
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


# Solution
""" def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum """