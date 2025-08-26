import sys
from typing import Any

def add(nbr1: int, nbr2: int) -> int:
    """
    Calculates the sum of two numbers.

    Parameters:
    nbr1 (int), nbr2 (int): Interger numbers.

    Returns:
    int: Result os the sum of nbr1 and nbr2
    """
    return nbr1 + nbr2


def subtract(nbr1: int, nbr2: int) -> int:
    """
    Calculates the subtraction between two numbers.

    Parameters:
    nbr1 (int), nbr2 (int): Interger numbers.

    Returns:
    int: Result of the subtraction between nbr1 and nbr2
    """
    return nbr1 - nbr2


def multiply(factor1: int, factor2: int) -> int:
    """
    Calculates the multiplication between two numbers(factors).

    Parameters:
    factor1 (int), factor2 (int): Interger numbers.

    Returns:
    int: The product between factor1 and factor2
    """
    return factor1 * factor2


def divide(dividend: int, divisor: int) -> float:
    """
    Calculates the divison between two numbers.

    Parameters:
    dividend (int): The number to be divide.
    divisor (int): The number by which the dividend will be divided.

    Returns:
    float: The Quotient of the division between the dividend for the divisor.
    """
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")

    return dividend / divisor


def power(base: int, exponent: int) -> Any:
    """
    Calculates the result of raising a base to a given exponent.

    Parameters:
    base (int): The number that will be raised to a power.
    exponent (int): The number that indicates how many times the base \
        is multiplied by itself.

    Returns:
    # Any: The result of the exponentiation. Type depends on the inputs:
    #      int or float for numeric inputs, str for string repetition, etc.
    """
    return base ** exponent