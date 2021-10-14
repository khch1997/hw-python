def calculator(number1, number2, operator):
    """
    The calculator function returns the result of the operation

    Parameters
    ----------
    number1 : float
        the first number

    number2: float
        the second number

    operator: string
        operator to perform calculation

    Returns
    -------
    float:
        The result of the operation.
    
    False:
        if the operation is invalid

    Examples
    --------
    >>> calculator(1, 1, +)
    2
    >>> calculator('a', 1, -)
    False
    >>> calculator(12, 4.2, '*')
    50.400000000000006
    """
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    elif operator == '//':
        return number1 // number2
    elif operator == '**':
        return number1 ** number2
    else:
        return False

def parse_input():
    """
    Take input from the user and call the calculator function

    Examples
    --------
    >>> parse_input()
    Enter equation: 10 + 11
    21.0

    >>> parse_input()
    Enter equation: 12 * 4.2
    50.400000000000006
    
    >>> parse_input()
    Enter equation: 10 ** 2
    100.0
    """
    equation = input('Enter equation: ')
    number1, operator, number2 = equation.split()
    result = calculator(float(number1), float(number2), operator)
    print(result)