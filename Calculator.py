# Date: 7/27/2023
# File: Calculator.py
# Name: Dillon Teakell
# Desc: Calculator using Python 
#
#
import time
import math
import os

# Setup and IO Functions
# Setup Function
def setup():

    # Create a file to hold setup information
    setup_file_1 = open('calculator_setup.txt', 'w')
    
    # Print welcome message
    print("Welcome to Python Calculator!\n")

    #Get user name
    user_name = input("Please enter your name: ")

    time.sleep(0.5)

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\nHi, " + user_name + "!\n")

    # Write user name to the file
    setup_file_1.write(user_name)
    setup_file_1.close()

    setup_file_2 = open('history.txt', 'w')

# Welcome Message 
def welcome():
    # Open file containing the user name
    try:
        name_file = open('calculator_setup.txt', 'r')
        print("Welcome back, " + name_file.read() + "!\n")
        time.sleep(0.5)
        name_file.close()

    except FileNotFoundError:
        input("Setup files not found. Please press 'Enter' to start setup.")
        print("\nCreating File. Please wait. \n")
        time.sleep(2)
        print("File created successfully! Launching program. \n")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        setup()




# Menu Functions
# Prints the main menu of the calculator
def show_menu():
    print("Please make a selection from the list below.\n")
    print("1.) Addition \n2.) Subtration \n3.) Multiplication \n4.) Division \n5.) Settings \n0.) Exit Program\n")
    get_menu_choice()

# Get choice from list
def get_menu_choice():
    try:
        user_choice = int(input("Choice: "))
    except (ValueError, UnboundLocalError): 
        print("\nERROR: Please enter a valid integer value. Retrying...\n")
        time.sleep(0.5)
        show_menu()
        get_menu_choice()
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

    elif user_choice == 5:
        print("\nPlease wait...")
        time.sleep(1)
        show_settings()
    
    elif user_choice == 0:
        exit_program()

    else:
        print("\nERROR: Invalid input. Please input a valid choice")
        time.sleep(0.5)
        show_menu()
        get_menu_choice()




# Calculation Functions
def addition():
   int1 = int(input("Please enter an integer: "))
   int2 = int(input("Please enter another integer: "))
   sum = int1 + int2
   time.sleep(0.5)
   print("\n", int1, "+", int2, "=", sum)

   input("\nPlease press any key to continue: ")
   os.system('cls' if os.name == 'nt' else 'clear')
   
   show_menu()
   get_menu_choice()

def subtraction():
    int1 = int(input("Please enter an integer: "))
    int2 = int(input("Please enter another integer: "))
    difference = int1 - int2
    time.sleep(0.5)
    print("\n", int1, "-", int2, "=", difference)

    input("\nPlease press any key to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    show_menu()
    get_menu_choice()

def multiplication():
    int1 = int(input("Please enter an integer: "))
    int2 = int(input("Please enter another integer: "))
    product = int1 * int2
    time.sleep(0.5)
    print("\n", int1, "*", int2, "=", product, "\n")

    input("\nPlease press any key to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    show_menu()
    get_menu_choice()

def division():
    int1 = int(input("Please enter an integer: "))
    int2 = int(input("Please enter another integer: "))
    try:
        quotient = int1 / int2

        input("Please press any key to continue: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        show_menu()
        get_menu_choice()

    except ZeroDivisionError:
        print("\nERROR: Dividing by zero is impossible! \n")
        input("Please press any key to continue: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        get_menu_choice()




# Settings functions
# Settings menu
#
def show_settings():
    os.system("cls" if os.name == 'nt' else "clear")
    print("\nSettings\n")
    print("1.) Edit setup file \n2.) Delete setup file \n3.) Delete history file \n4.) Exit\n")
    get_settings_choice()

def get_settings_choice():
    try:
        settings_choice = int(input("Choice: "))
    except (ValueError, UnboundLocalError):
        print("\nERROR: Please enter a valid input. Try again. \n")
        time.sleep(0.5)
        show_settings()
        get_settings_choice()
        pass

    if settings_choice == 1:
        print("Please wait...\n")
        time.sleep(0.5)
        edit_setup()
    
    elif settings_choice == 2:
        print("Please wait...")
        time.sleep(0.5)

    elif settings_choice == 3:
        print("Please wait...")
        time.sleep(0.5)

    elif settings_choice == 4:
        print("Please wait...")
        time.sleep(0.5)

    else:
        print("\nERROR: Invalid choice. Please try again.\n")
        time.sleep(0.5)

def edit_setup():
    time.sleep(1)
    setup_file = open("calculator_setup.txt", 'w')
    user_name = input("Please enter a new name: ")
    
    setup_file.write(user_name)
    setup_file.close()

    time.sleep(0.5)
    show_menu()





# Exit Program
def exit_program():
    choice = input("\nAre you sure you want to close the program? (y/n): ")
    if choice == 'y':
        print("Closing Program...")
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)
        exit()
    elif choice == 'n':
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)
        show_menu()
        get_menu_choice()
    else:
        print("\nERROR: Invalid input. Please try again")
        time.sleep(0.5)
        exit_program()


def main():

    print("\nPython Calculator v1.0 \n")

    welcome()

    show_menu()

main()