def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a == 0:
        msg = "the number is zero"
    if a > 0 and a % 2 == 1:
        msg = "positive odd number"
    if a > 0 and a % 2 == 0:
        msg = "positive even number"
    if a < 0 and a % 2 == 1:
        msg = "negative odd number"
    if a < 0 and a % 2 == 0:
        msg = "negative even number"
    
    return msg