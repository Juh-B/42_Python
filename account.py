class Account:
    """Class that represents a bank account"""

    def __init__(self, account_id: int, cpf: str):
        """Initialize the class."""
        self.account_id = account_id
        self.cpf = cpf
        self.__balance = 0
        self.__operations = []
    
    def deposit(self, amount: int, description: str) -> int:
        self.__operations = self.__operations.append()
    

        