# ---------------------------------------------------------------------------------------------------------
# Name : ABUBAKAR PASHA
# Date : 13 - Mar - 2022
# Assignment 3
# Q.3. Write a program that can calculate the compound interest by taking all the requisites from the user. (10 Marks)
# ==========================================================================================================

# Get the Principle, rate & time details from User


print("This program will help you calculate compound interest")
prin = float(input('Enter PRINCIPLE : '))  # get the Principle value from user and convert it to float
rate = float(input('Enter RATE percent : '))  # get the rate value from user and convert it to float
time = float(input('Enter Time in years : '))  # get the time value from user and convert it to float

amt = prin * (pow((1 + rate / 100), time))  # calculate amount using formula
ci = amt - prin  # Calculate principle
print('The compound interest will be :: ' + str(ci))
print("Total amount payable after {} years will be {}".format(time,amt))
