def missing_char(str, n):
    """Given a non empty string and int n, return new string where
    the char at index n has been removed. The value of n will be a
    valid index of char in the original string. n will be in the
    range 0... len(str) - 1 inclusive"""
    return str[:n] + str[n + 1 :]


# Solution
""" def missing_char(str, n):
    front = str[:n]   # up to but not including n
    back = str[n+1:]  # n+1 through end of string
    return front + back
 """