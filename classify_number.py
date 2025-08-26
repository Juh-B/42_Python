import sys

def is_positive(a: int) -> bool:
    """
    Checks if an integer is positive.

    Parameters:
    a (int): An integer number.

    Returns:
    bool: True if the number is greater than zero,\
    otherwise False.
    """
    return a > 0

if __name__ == "__main__":
    nbr = int(sys.argv[1])
    print(f'{is_positive(nbr)}')