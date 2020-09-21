def parrot_trouble(talking, hour):
    """ "Hour" parameter is current hour time in range 0...23.
    In trouble if parrot talking and hour is before 7 or after 20. Return
    True if in trouble."""
    if talking == False:
        return False
    if hour < 7 or hour > 20:
        return True
    else:
        return False


# Note: I originally wrote return(talking == True and hour < 7 or hour > 20)
# Solution
""" def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20)) """
# Need extra parenthesis around the or clause
# since and binds more tightly than or.
# and is like arithmetic *, or is like arithmetic +
