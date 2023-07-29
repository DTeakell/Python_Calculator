# Date: 7/27/2023
# File: Calculator.py
# Name: Dillon Teakell
# Desc: Calculator using Python 
#
#
import time
import math
import os

# Get name of user to make it more personal
def get_user_name():
    userName = input("Please enter your name: ")
    time.sleep(0.5)
    return userName

# Print welcome message to greet the user
def welcome_message(user_name):
    print("\nHello, " + user_name + ".\n")
    time.sleep(0.5)
    print("Welcome to Python Calculator.\n")

# Prints the main menu of the calculator
def show_menu():
    print("Please make a selection from the list below.\n")
    print("1.) Addition \n2.) Subtration \n3.) Multiplication \n4.) Division \n0.) Exit Program\n")

# Get choice from list
def get_user_choice():
    try:
        user_choice = int(input("Choice: "))
    except (ValueError, UnboundLocalError): 
        print("\nERROR: Please enter a valid integer value. Retrying...\n")
        time.sleep(0.5)
        show_menu()
        get_user_choice()
        pass
    
    if user_choice == 1:
        print("\nPlease wait...\n")
        time.sleep(1)
        addition()

    elif user_choice == 2:
        print("\nPlease wait...\n")
        time.sleep(1)
        subtraction()

    elif user_choice == 3:
        print("\nPlease wait...\n")
        time.sleep(1)
        multiplication()

    elif user_choice == 4:
        print("\nPlease wait...\n")
        time.sleep(1)
        division()
    
    elif user_choice == 0:
        exit_program()

    else:
        print("\nERROR: Invalid input. Please input a valid choice")
        time.sleep(0.5)
        show_menu()
        get_user_choice()
    
# Addition calculations
def addition():
   int1 = int(input("Please enter an integer: "))
   int2 = int(input("Please enter another integer: "))
   sum = int1 + int2
   time.sleep(0.5)
   print(int1, "+", int2, "=", sum)

   input("Please press any key to continue: ")
   os.system('cls' if os.name == 'nt' else 'clear')
   
   show_menu()
   get_user_choice()

# Subtraction calculations
def subtraction():
    int1 = int(input("Please enter an integer: "))
    int2 = int(input("Please enter another integer: "))
    difference = int1 - int2
    time.sleep(0.5)
    print(int1, "-", int2, "=", difference)

    input("Please press any key to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    show_menu()
    get_user_choice()

# Multiplication calculations
def multiplication():
    int1 = int(input("Please enter an integer: "))
    int2 = int(input("Please enter another integer: "))
    product = int1 * int2
    time.sleep(0.5)
    print(int1, "*", int2, "=", product, "\n")

    input("\nPlease press any key to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    show_menu()
    get_user_choice()

# Division calculations
def division():
    int1 = int(input("Please enter an integer: "))
    int2 = int(input("Please enter another integer: "))
    try:
        quotient = int1 / int2
        print(int1, "/", int2, "=", quotient)

        input("Please press any key to continue: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        show_menu()
        get_user_choice()

    except ZeroDivisionError:
        print("\nERROR: Dividing by zero is impossible! \n")
        input("Please press any key to continue: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        get_user_choice()

# Exit
def exit_program():
    choice = input("\nAre you sure you want to close the program? (y/n): ")
    if choice == 'y':
        print("Closing Program...")
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)
        exit()
    elif choice == 'n':
        show_menu()
        get_user_choice()
    else:
        print("\nERROR: Invalid input. Please try again")
        time.sleep(0.5)
        exit_program()


def main():

    print("\nPython Calculator v1.0 \n \n")

    name = get_user_name()

    welcome_message(name)

    show_menu()

    get_user_choice()

main()