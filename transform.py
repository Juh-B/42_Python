import sys

def square_even_numbers(nbrs: list[int]) -> list[int]:
    """
    Transform the evens numbers from a list in square.

    Parameters:
    nbrs (list[int]): A list of intergers.

    Returns:
    list[int]: Return a list with square numbers.
    """
    square = [nbr**2 for nbr in nbrs if (nbr % 2) == 0]
    return square

if __name__ == "__main__":
    if len(sys.argv) > 1:
        numbers = list(map(int, sys.argv[1].split(' ')))
        print(f'Square evens: {square_even_numbers(numbers)}')
    else:
        print("You need add a number's list")