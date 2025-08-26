import sys

def read_file(file_name: str):
    """
    Read the content of a file.

    Parameters:
    file_name (str): File name.

    Returns:
    None
    """
    with open(file_name, "r",encoding='utf-8') as file:
        print(f'{file.read()}')


def handle_error(e: Exception) -> int:
    """
    Prints the error type and message in a standardized way.
    
    Parameters:
    e (Exception): The exception instance to handle.

    Returns:
    int: Return an interge as error code.
    """
    if isinstance(e, FileNotFoundError):
        print(f"\033[31mError:\033[0m File not found.")
    elif isinstance(e, IsADirectoryError):
        print(f"\033[31mError:\033[0m The argument passed is a directory.")
    else:
        print(f"\033[31mUnexpected error:\033[0m {type(e).__name__}\n({e})")
    return 1


def main() -> int:
    """
    Main function.
    Convert to float.
    """
    try:
        read_file(sys.argv[1])
        return 0
    except Exception as e:
        return handle_error(e)

if __name__ == "__main__":
    sys.exit(main())