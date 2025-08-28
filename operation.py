import utils

class Operation:
    """Class that represent a person."""
    
    def __init__(self, cents: int, description: str):
        """
        Initialize the class.
        cents (int): Represents the value in cents.
        description (str): The operation's description
        """
        # operations_type (str): The operation's nature.
        self.cents = cents
        self.description = description
        if cents > 0:
            self.operation_type = 'credit'
        elif cents < 0:
            self.operation_type = 'debit'
        else:
            raise ValueError('Needs a value different of zero')
    
    def __repr__(self) -> str:
        return f"Operation(cents={self.cents}, operation_type='{self.operation_type}', description='{self.description}')"


    def __str__(self) -> str:
        return f"{utils.format_cents(self.cents)} ({self.description})"