def extra_end(str):
    """Given a string, return a new string made of 3
    copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """
    length = len(str)
    two_char = str[length - 2 :]
    if len(str) > 2:
        return two_char * 3
    else:
        return str * 3


# Solution
# Findings: Do not need to use len(str), instead use -2 to indicate up to
# last 2 characters in a str
# Note: generalize the function, 'end' may be used repeatedly
""" def extra_end(str):
    end = str[-2:]
    return end + end + end """
