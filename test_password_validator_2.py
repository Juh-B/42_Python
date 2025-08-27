# import pytest
import string
import password_validator

def test_password_len() -> None:
    assert password_validator.password_len("abcd") == False
    assert password_validator.password_len("abcdefghijklmnopqrstuvwxyz") == False
    assert password_validator.password_len("abcdefghijk") == True


def test_password_upper() -> None:
    assert password_validator.password_upper("aBcdEfghiJk") == True
    assert password_validator.password_upper("abcdefghijk") == False


def test_password_lower() -> None:
    assert password_validator.password_lower("aBcdEfghiJk") == True
    assert password_validator.password_lower("ABCDEFGHIJK") == False


def test_password_digit() -> None:
    assert password_validator.password_digit("aBcdEfghi10") == True
    assert password_validator.password_digit("aBcd40Efghi") == True
    assert password_validator.password_digit("aBcdEfghiJk") == False


def test_special_char() -> None:
    assert password_validator.special_char("aBcdEfghi10" + string.punctuation[0]) == True
    assert password_validator.special_char("a#Bcd$40Efghi") == True
    assert password_validator.special_char("aBcdEfghiJ15") == False


def test_white_space() -> None:
    assert password_validator.white_space("a#Bcd$40Efghi") == False
    assert password_validator.white_space("aBcdE  fg15!") == True
    assert password_validator.white_space(" aBcdEfg15!") == True
    assert password_validator.white_space("aBcdEfg15! ") == True
    assert password_validator.white_space("aBcdE    fg15!") == True


def test_valid_password() -> None:
    assert password_validator.is_valid_password("a#Bcd$40Efghi") == True
    assert password_validator.is_valid_password("Senhadeubom!43") == True
    assert password_validator.is_valid_password("a#bC42") == False
    assert password_validator.is_valid_password("a#Bcd$40Efghi  bla") == False
    assert password_validator.is_valid_password("a#Bcd$40Efghi12345bla") == False