logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(logo)
    result_response = 'n'
    while True:
        try:
            if result_response == 'n':
                first_num = float(input("What's the first number? "))
            operation = input("+\n-\n*\n/\nPick an operation: ")

            while operation not in ['+', '-', '*', '/']:
                print("Please enter a valid operation!")
                operation = input("+\n-\n*\n/\nPick an operation: ")

            second_num = float(input("What's the second number? "))

        except ValueError:
            raise ValueError("Invalid Input!")



        result = operations[operation](first_num, second_num)

        print(f"{first_num} {operation} {second_num} = {result}")
        
        result_response = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if result_response not in ['y', 'n']:
            print("Invalid Input!")
            result_response = input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if result_response not in ['y', 'n']:
            print("Invalid Response!")
            result_response = input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if result_response == 'y':
            first_num = result

calculator()