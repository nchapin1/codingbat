def first_two(str):
    """Given a string, return the string made of its first two chars,
    so the String "Hello" yields "He". If the string is shorter than
    length 2, return whatever there is, so "X" yields "X", and the empty
    string "" yields the empty string ""."""
    begin = str[:2]
    if len(str) < 2:
        return str
    else:
        return begin


# Solution
# Note: Do not create variables needlessly. Be smart Noah! Keep it simple.
""" def first_two(str):
  if len(str) >= 2:
    return str[:2]
  else:
    return str """
