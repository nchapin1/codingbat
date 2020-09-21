def diff21(n):
    """Given an int n, return the absolute difference between n and 21.
    If n is over 21, return double the absolute difference between n and 21"""
    result = abs(n - 21)
    if n > 21:
        return result * 2
    else:
        return result


# Note: Do not need abs() ... 21 - n will be absolute.
# Solution
""" def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2 """
