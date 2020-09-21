def makes10(a, b):
    """Given 2 ints, a and b, return True if one of them is 10
    or if their sum is 10"""
    sum = a + b
    return sum == 10 or a == 10 or b == 10


# Note: Don't create variables when you don't have to.
# Solution
""" def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10) """