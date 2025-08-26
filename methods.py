import sys

def verify_str(string: str) -> None:
    """
    Checks some methods on a string.

    Parameters:
    string (str): A string.

    Returns:
    None
    """
    print(
        f'São maiúsculas? {string.isupper()}\n'
        f"É numerico? {string.isdigit()}\n"
        f"É ascii? {string.isascii()}\n"
        f"É alfanumérico? {string.isalnum()}"
    )

if __name__ == "__main__":
    verify_str(sys.argv[1])