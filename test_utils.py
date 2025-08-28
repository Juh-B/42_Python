import pytest
import utils

test_data = [
    (11_222_00, ("[+] R$ 11.222,00")),
    (-11_222_00, ("[-] R$ 11.222,00"))
]

@pytest.mark.parametrize("value, expected", test_data)
def test_format_cents(value: int, expected : str) -> None:
    """
    Verify if the int is convert for the right string.

    Parameters:
    value (int): An interge.
    expected (str): A string with the correct formatting.

    Returns:
    None
    """
    assert utils.format_cents(value) == expected