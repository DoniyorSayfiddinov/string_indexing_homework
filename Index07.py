def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if (len(s)-1)>=n:
        return s[n-1]
    else :
        return False
print(main("uzxdcvbgnm",4))
