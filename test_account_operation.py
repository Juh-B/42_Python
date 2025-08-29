import pytest
from account import Account, InsufficientBalanceError
from operation import Operation
from utils import format_cents


# --- TEST ACCOUNT ---
def test_account() -> None:
    """Verify if the account is working propriely."""
    ac = Account(123, '123.456.789-01')
    # Testa o __repr__
    assert repr(ac) == "Account(123, '123.456.789-01')."
    # Testa o __str__
    assert str(ac) == "Account: 123\nBalance: [+] R$ 0,00"


# Deposite tests
def test_deposite() -> None:
    """Verify if the deposite is working propriely."""
    ac = Account(123, '123.456.789-01')
    ac.deposit(11_222_00, 'ATM deposit')
    assert ac.statement() == "[+] R$ 11.222,00 (ATM deposit)\nBalance: [+] R$ 11.222,00"

def test_deposit_negative_amount() -> None:
    ac = Account(123, '123.456.789-01')
    with pytest.raises(ValueError, match="The amount must be greater than zero."):
        ac.deposit(-100, 'Invalid deposit')

# Withdraw test
def test_withdraw() -> None:
    """Verify if the withdraw is working propriely."""
    ac = Account(123, '123.456.789-01')
    ac.deposit(11_222_00, 'ATM deposit')
    ac.withdraw(222_00, 'ATM withdraw')
    assert ac.statement() == "[+] R$ 11.222,00 (ATM deposit)\n[+] R$ 222,00 (ATM withdraw)\nBalance: [+] R$ 11.000,00"

def test_withdraw_negative_amount() -> None:
    ac = Account(123, '123.456.789-01')
    with pytest.raises(ValueError, match="The amount must be greater than zero."):
        ac.withdraw(-100, 'Invalid withdraw')

def test_insufficient_balance() -> None:
    ac = Account(123, '123.456.789-01')
    with pytest.raises(InsufficientBalanceError, match="Insufficient balance."):
        ac.withdraw(100, 'Invalid withdraw')


# --- TEST OPERATION ---
test_data_operation = [
    (11_222_00, 'ATM deposit', "credit"),
    (-11_222_00, 'ATM deposit', "debit"),
]

@pytest.mark.parametrize("cents, description, operation_type", test_data_operation)
def test_operation(cents: int, description: str, operation_type: str) -> None:
    """Verify if the operation is working propriely."""
    t = Operation(cents, description)
    # Testa o __repr__
    assert repr(t) == f"Operation(cents={cents}, operation_type='{operation_type}', description='{description}')"
    # Testa o __str__
    assert str(t) == f"{format_cents(cents)} ({description})"

def test_operation_with_zero() -> None:
    """Verify if the operation with zero is working propriely."""
    with pytest.raises(ValueError, match="Needs a value different of zero"):
        Operation(0, 'ATM deposit')