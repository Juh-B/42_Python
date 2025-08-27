import pytest
import password_validator

test_data = [
    (("senha"), False),
    (("Senhapra42!SaoPaulo"), False),
    (("senhapra42!"), False),
    (("SENHAPRA42!"), False),
    (("Senhaprateste!"), False),
    (("Senhapra42"), False),
    (("Senha pra 42!"), False),
    (("Senha    pra42!"), False),
    (("Senhapra42!"), True)
]

@pytest.mark.parametrize("password, expected", test_data)
def test_valid_password(password : str, expected : bool) -> None:
    """
    Verify if password pass all test.

    Parameters:
    password (str): A string representing the password to be validated.
    expected (bool): Boolean True if the password is valid, False otherwise.

    Returns:
    None
    """
    assert password_validator.is_valid_password(password) == expected