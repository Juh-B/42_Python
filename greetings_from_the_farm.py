import cowsay

def greeting(name: str = 'Strange') -> None:
    """receives a name and prints a greeting"""
    final_str = f"Hello {name}"
    cowsay.turtle(final_str)