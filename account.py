from operation import Operation
import utils

class InsufficientBalanceError(Exception):
    """Raised when the withdrawal amount exceeds the available balance."""
    pass


class Account:
    """Class that represents a bank account"""

    def __init__(self, account_id: int, cpf: str):
        """Initialize the class."""
        self.account_id = account_id
        self.cpf = cpf
        self.__balance = 0
        self.__operations: list[str] = []


    def __repr__(self) -> str:
        """Provide an official representation of the account."""
        return f"Account({self.account_id}, '{self.cpf}')."

    def __str__(self) -> str:
        """Provide a readable and user-friendly representation of the account."""
        return (
            f"Account: {self.account_id}\n"
            f"Balance: {utils.format_cents(self.__balance)}"
        )


    def deposit(self, amount: int, description: str) -> None:
        """Performs deposit operations."""
        if amount < 0:
            raise ValueError('The amount must be greater than zero.')
        op = Operation(amount, description)
        self.__balance += amount
        self.__operations.append(f'{(op)}')
    
    def withdraw(self, amount: int, description: str) -> None:
        """Carries out withdrawal operations."""
        if amount < 0:
            raise ValueError('The amount must be greater than zero(0).')
        if self.__balance - amount < 0:
            raise InsufficientBalanceError('Insufficient balance.')
        op = Operation(amount, description)
        self.__balance -= amount
        self.__operations.append(f'{(op)}')

    def statement(self) -> str:
        """Returns the statement of operations as a string."""
        result = '\n'.join(str(op) for op in self.__operations)
        return f"{result}\nBalance: {utils.format_cents(self.__balance)}"

