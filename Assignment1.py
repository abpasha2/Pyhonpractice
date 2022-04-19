# ---------------------------------------------------------------------------------------------------------
#
# Name : ABUBAKAR PASHA
# Date : 13 - Mar - 2022
# Assignment 1
# Q.1. Write a program to take the name of the user as input & just greet it.
# For example, if the user entered “Harshit”, it should print “Hello Harshit”.  (10 Marks)
# ==========================================================================================================

# uname= input("Enter your name : ")  # Getting the input from User
# print("Hello " + uname)             # Printing user's name with greeting


# Q.2. Create a menu-based calculator using python, & it should execute as many times as required. (20 Marks)

# Q.3. Write a program that can calculate the compound interest by taking all the requisites from the user. (10 Marks)

print("This program will help you calculate compound interest")
prin = float(input('Enter PRINCIPLE : '))
rate = float(input('Enter RATE percent : '))
time = float(input('enter Time in years : '))

amt = prin * (pow((1 + rate / 100), time))
ci = amt - prin
print('The compound interest will be :: ' + str(ci))