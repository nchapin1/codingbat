def not_string(str):
    """Given a string, return a new string where "not " has been added
    to the front. However, if the string already begins with "not", return
    the string unchanged"""
    if "not " in str:
        return str
    if " not" in str:
        return "not " + str
    if "not" not in str:
        return "not " + str
    else:
        return str


# Solution
""" def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str """


# str[:3] goes from the start of the string up to but not
# including index 3

# Note: if the length of str is greater than or equal to three, and
# from the start of string up to but not including index 3 equals "not"
# return str. Else, return "not " to the str
