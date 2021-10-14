def calculator(number1, number2, operator):
    operators = ['+', '-', '*', '/', '//', '**']
    
    if operator not in operators:
        return False

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

def parse_input():
    equation = input('Enter equation: ')
    number1, operator, number2 = equation.split()
    result = calculator(float(number1), float(number2), operator)
    print(result)