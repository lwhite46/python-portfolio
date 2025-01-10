#calculator
#init
import time

#functions
def add(num1, num2):
    print(" ")
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))

def sub(num1, num2):
    print(" ")
    print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))

def mult(num1, num2):
    print(" ")
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))

def div(num1, num2):
    print(" ")
    print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))

def calculator():
    print("Welcome Preschoolers to Simple Calculator")
    while True:
        print(" ")
        print("Enter an operation: ")
        print("""
            1 - Addition
            2 - Subtraction
            3 - Multiplication
            4 - Division
            5 - Quit""")
        time.sleep(1)
        operation = int(input("(1 - 5) Operation: "))
        if operation == 1:
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            add(num1, num2)
        elif operation == 2:
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            sub(num1, num2)
        elif operation == 3:
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            mult(num1, num2)
        elif operation == 4:
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            div(num1, num2)
        elif operation == 5:
            print("""
Quitting...""")
            break
        else:
            print("""
Incorrect Input...""")

#main
calculator()
