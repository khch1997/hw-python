def calculator(number1, number2, operator):
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
    equation = input('Enter equation: ')
    number1, operator, number2 = equation.split()
    result = calculator(float(number1), float(number2), operator)
    print(result)