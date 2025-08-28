class Person:
    """Class that represent a person."""
    
    def __init__(self, name: str, age: int):
        """Initialize the class with a name and age."""
        self.name = name
        self.age = age

    def birthday(self) -> None:
        """Represent a birthday that add one year to the age \
            of the person."""
        self.age += 1