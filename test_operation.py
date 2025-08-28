import pytest
from operation import Operation
from utils import format_cents

test_data = [
    (11_222_00, 'ATM deposit', "credit"),
    (-11_222_00, 'ATM deposit', "debit"),
]

@pytest.mark.parametrize("cents, description, operation_type", test_data)
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
