def format_cents(nbr: int) -> str:
    """
    Convert an interge to string.
    
    Parameters:
    nbr (int): A interge (number).

    Returns:
    str: Return a string from the number.
    """
    signal = "+" if nbr >= 0 else "-"
    real = abs(nbr) // 100
    cents = abs(nbr) % 100
    real_format = f'{real:,}'.replace(",", ".")

    return f"[{signal}] R$ {real_format},{cents:02d}"