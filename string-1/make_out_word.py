def make_out_word(out, word):
    """Given an "out" string length 4, such as "<<>>",
    and a word, return a new string where the word is in
    the middle of the out string, e.g. "<<word>>"."""
    one = out[:2]
    two = out[2:]
    return one + word + two


# Solution
# No solution available