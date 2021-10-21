def main():
    print('1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division')

    while True:
        try:
            operation = int(input('What operation do you want to do? '))
            value1 = float(input('Enter the first number: '))
            value2 = float(input('Enter the second number: '))
            break
        except:
            print('Invalid input.')

    if (operation == 4) and (value2 == 0):
        print('We cannot divide a number by zero.')
    else:
        result = round(calculation(operation, value1, value2))
        print(f'The result is {result}.')

def calculation(operation, value1, value2):
    if operation == 1:
        result = addition(value1, value2)
    elif operation == 2:
        result = subtraction(value1, value2)
    elif operation == 3:
        result = multiplication(value1, value2)
    elif operation == 4:
        result = division(value1, value2)

    return result

def addition(value1, value2):
    return value1 + value2

def subtraction(value1, value2):
    return value1 - value2

def multiplication(value1, value2):
    return value1 * value2

def division(value1, value2):
    return value1 / value2

if __name__ == '__main__':
    main()
