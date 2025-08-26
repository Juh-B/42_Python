import sys

def downcase_str(string: str) -> str:
    """
    Converts all characters to lowercase.

    Parameters:
    string (str): A string

    Returns:
    str: Return a lowercase string.
    """
    return string.lower()


if __name__ == "__main__":
    # From argv, extracts the list of strings
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            print(f'{downcase_str(arg)}')
    else:
        print(f'{None}')