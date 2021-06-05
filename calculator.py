# Python Calculator

print("1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division")

while True:
    # Check if the user input is a valid option
    user_input = input("What operation do you want to do? ");
    try:
        user_answer = int(user_input);
        break;
    except ValueError:
        print("Enter a valid option.")


if (user_answer >= 1) and (user_answer <= 4):
    continue_execution = False
    
    while True:
        # Check if the user input is valid to make the operations
        value1 = input("Enter the first number: ")
        value2 = input("Enter the second number: ")
        try:
            num1 = int(value1)
            num2 = int(value2)
            continue_execution = True
            break;
        except ValueError:
            try:
                num1 = float(value1)
                num2 = float(value2)
                continue_execution = True
                break;
            except ValueError:
                continue_execution = False
                print("Enter a valid number.")

    if continue_execution == True:
        if user_answer == 1:
            # Addition
            result = num1 + num2
            print("{} + {} = {}".format(num1, num2, result))
        elif user_answer == 2:
            # Subtraction
            result = num1 - num2
            print("{} - {} = {}".format(num1, num2, result))
        elif user_answer == 3:
            # Multiplication
            result = num1 * num2
            print("{} * {} = {}".format(num1, num2, result))
        else:
            # Division
            result = num1 / num2
            print("{} / {} = {}".format(num1, num2, result))

else:
    # If the user input doesn't represent a real option, shows an error message
    print("The option that you type is not a valid option.")
