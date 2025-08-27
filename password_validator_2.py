import string

def password_len(password: str) -> bool:
    """
    Validates a password when it has between 8 and 16 characteres.

    Parameters:
    password (str): A string representing the password to be validated.

    Returns:
    bool: Returns True if the password is valid, False otherwise.
    """
    if len(password) < 8 or len(password) > 16:
        return False
    return True


def password_upper(password: str) -> bool:
    """
    Validates a password when it contain at least one uppercase letter.

    Parameters:
    password (str): A string representing the password to be validated.

    Returns:
    bool: Returns True if the password is valid, False otherwise.
    """
    return any(c.isupper() for c in password)


def password_lower(password: str) -> bool:
    """
    Validates a password when it contain at least one lowercase letter.

    Parameters:
    password (str): A string representing the password to be validated.

    Returns:
    bool: Returns True if the password is valid, False otherwise.
    """
    return any(c.islower() for c in password)


def password_digit(password: str) -> bool:
    """
    Validates a password when it contain at least one digit.

    Parameters:
    password (str): A string representing the password to be validated.

    Returns:
    bool: Returns True if the password is valid, False otherwise.
    """
    return any(c.isdigit() for c in password)


def special_char(password: str) -> bool:
    """
    Validates a password when it contain at least one special charactere.

    Parameters:
    password (str): A string representing the password to be validated.

    Returns:
    bool: Returns True if the password is valid, False otherwise.
    """
    return any(c in string.punctuation for c in password)


def white_space(password: str) -> bool:
    """
    Validates a password when it not contain white spaces.

    Parameters:
    password (str): A string representing the password to be validated.

    Returns:
    bool: Returns True if the password is valid, False otherwise.
    """
    return any(c.isspace() for c in password)


def is_valid_password(password: str) -> bool:
    """
    Validates whether a password meets security requirements.

    Parameters:
    password (str): A string representing the password to be validated.

    Returns:
    bool: Returns True if the password is valid, False otherwise.

    A valid password must:
    - Be at least 8 characters long.
    - Be at most 16 characters long.
    - Contain at least one uppercase letter.
    - Contain at least one lowercase letter.
    - Contain at least one digit.
    - Contain at least one special character.
    - Not contain any whitespace characters.
    """
    if password_len(password) and password_upper(password) \
        and password_lower(password) and password_digit(password) \
        and special_char(password) and not white_space(password):
        return True
    else:
        return False


