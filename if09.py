def main(a):
    """
    The two digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    a = str(a) 
    b = a[1] + a[0]
    if int(b) <= int(a):
        return True
    if int(b) > int(a):
        return False

