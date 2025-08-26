def greeting(name: str = '42') -> None:
    """receives a name and prints a greeting"""
    print(f"Hello \033[32m{name}\033[0m")