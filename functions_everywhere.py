import sys

def enlarge(string: str) -> str:
    """
    Complete the string with 'Z' until it has 8 characters.

    Parameters:
    string (str): A string.

    Returns:
    str: Return a string with 8 characters.
    """
    return string.ljust(8, 'Z')

def shrink(string: str) -> str:
    """
    Slice the firts 8 characters from a string.

    Parameters:
    string (str): A string.

    Returns:
    str: Return a sliced string with 8 characters.
    """
    return string[:8]

if __name__ == "__main__":
    # From argv, extracts the list of strings
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                print(f'{shrink(arg)}')
            else:
                print(f'{enlarge(arg)}')
    else:
        print(f'{None}')