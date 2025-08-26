def format_names(dictionary: dict[str, str]) -> list[str]:
    """
    Creates a list of full names from a dictionary.

    Parameters:
    dictionary (dict[str, str]): A dictionary of first \
    and last names.

    Returns:
    list[str]: Returns a list of full names.
    """
    list_names = []
    for key, value in dictionary.items():
        full_name = f'{key.capitalize()} {value.capitalize()}'
        list_names.append(full_name)
    return list_names