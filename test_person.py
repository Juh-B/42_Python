from person import Person

def test_person_initialization() -> None:
    """Test the person inicialization for name and age."""
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30

def test_person_birthday() -> None:
    """Test a birthday implementation."""
    p = Person("Alice", 30)
    assert p.age == 30
    p.birthday()
    p.birthday()
    assert p.age == 32
