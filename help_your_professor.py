def average(dictionary: dict[str, int]) -> float:
    """
    Generates the class' average grade \
    from a dictionary with names and grades

    Parameters:
    dictionary (dict[str, int]): A dictionary with names and grades.

    Returns:
    float: Returns the arithmetic mean of the class's grades.
    """
    grade_sum = 0
    students = 0
    if dictionary == {}:
        return 0
    
    for key, value in dictionary.items():
        if value is None:
            return 0
        grade_sum += value
        students += 1
    
    return grade_sum / students
