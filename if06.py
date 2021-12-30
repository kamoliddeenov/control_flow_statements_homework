def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    count_pos = 0
    count_neg = 0
    if a > 0:
        count_pos += 1
    if b > 0:
        count_pos += 1
    if c > 0:
        count_pos += 1
    if a < 0:
        count_neg += 1
    if b < 0:
        count_neg += 1
    if c < 0:
        count_neg += 1
    if count_pos > count_neg:
        msg = "there are a lot of positive numbers"
    else:
        msg = "there are a lot of negative numbers"
    return msg
    