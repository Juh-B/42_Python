import sys

def main() -> int:
    """
    Main function.
    Convert to float.
    """
    try:
        print(f'{float(sys.argv[1])}')
        return 0
    except ValueError:
        print("\033[31mOps, impossible to convert to float.\033[0m")
        return 1

if __name__ == "__main__":
    # Convert for float
    sys.exit(main())