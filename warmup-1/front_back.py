def front_back(str):
    """Given a new string, return a new string where the first and last chars
    have been exchanged"""
    first = str[:1]
    last = str[-1:]
    middle = str[1:-1]

    if len(str) > 1:
        return last + middle + first
    else:
        return str


# Solution
""" def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1 : len(str) - 1]  # can be written as str[1:-1]

    # last + mid + first
    return str[len(str) - 1] + mid + str[0]  """
