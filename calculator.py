from art import logo
import os


def operation_numbers(first_number, second_number):
    match operation:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number
        case "/":
            return first_number / second_number
        case _:
            return "Operation not valid"


should_continue = True
print(logo)

while should_continue:
    os.system('cls')
    first_number = int(input("What's the first number?: "))
    print("+ - * /")
    operation = input("Pick an operation: ")
    second_number = int(input("What's the second number?: "))

    result = operation_numbers(first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {result}")
    if input("Type 'y' if you would like to continue doing operations. ") != 'y':
        should_continue = False
        print("Thanks for using my calculator!")
