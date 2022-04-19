# Use of while loop
import random

print('This is number guessing game')
print('How many times you want to try your luck\nYou can get upto 5 chances only')
chance = int(input('Enter your number of CHANCES :: '))

if chance > 5:
    print('You can get only up to 5 chances')
    exit()

while chance > 0:
    ranNumber = random.randint(1, 20)
    print(f'You have {chance} chances to predict a number')
    answer = int(input('Guess a number :: '))
    chance -= 1

    if chance > 5:
        break;
    else:

        if answer == ranNumber:
            print('You got it right...!!!!')
            break
        elif answer < ranNumber:
            print('You missed it, Guess higher')
            print('The number was :: ', ranNumber)

        elif answer > ranNumber:
            print('You missed it, Guess lower')
            print('The number was :: ', ranNumber)
        else:
            pass
