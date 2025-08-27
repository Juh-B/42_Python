import sys

def read_file(file_name: str) -> None:
    """
    Read the content of a file.

    Parameters:
    file_name (str): File name.

    Returns:
    None
    """
    with open(file_name, "r",encoding='utf-8') as file:
        print(f'{file.read()}')


def main() -> int:
    """
    Main function.
    Convert to float.
    """
    try:
        read_file(sys.argv[1])
        return 0
    except FileNotFoundError:
        print("\033[31mError:\033[0m File not found.")
    except IsADirectoryError:
        print("\033[31mError:\033[0m The argument passed is a directory.")
    except Exception as e:
        print(f"\033[31mUnexpected error:\033[0m {type(e).__name__}\n({e})")
    return 1


if __name__ == "__main__":
    sys.exit(main())