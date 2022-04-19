# ---------------------------------------------------------------------------------------------------------
# Name : ABUBAKAR PASHA
# Date : 13 - Mar - 2022
# Assignment 2
# Q.2. Create a menu-based calculator using python, & it should execute as many times as required. (20 Marks)
# ==========================================================================================================
def prin_oper():
    print("**************************************")
    print("You can perform below operations")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - for exponent")
    print("**************************************")

blnChoice = True

while blnChoice:
    print("This is sample calculator to perform basic mathematical calculations on two numbers")
    usrChoice = input("Please enter y to continue, any other character to QUIT : ")
    if usrChoice == 'y' or usrChoice == 'Y':
        prin_oper()
        usrOperation = input("PLease enter the choice of operation from above list :: ")
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        if usrOperation == "1":
            print("The SUM of 2 numbers is :: " + str(num1+num2))
        elif usrOperation == "2":
            print("The Difference of 2 numbers is :: " + str(num1 - num2))
        elif usrOperation == "3":
            print("The Product of 2 numbers is :: " + str(num1 * num2))
        elif usrOperation == "4":
            print("The Quotient of 2 numbers is :: " + str(num1 / num2))
        elif usrOperation == "5":
            print(f'The exponent of {num1} to the power {num2}  is :: ' + str(num1 ** num2))
        else:
            pass
    else:
        exit(0)