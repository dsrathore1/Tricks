import random

n = random.randint(1, 50)

guess = int(input("Enter your guess :- "))

while n!= guess :

    if guess < n :
        print ("\nYou Guess is low\n")

        guess = int(input("Enter again your guess :- "))

    elif guess > n :

        print ("\nYour Guess is high\n")

        guess = int(input("Enter again your guess :- "))

    else :
        pass;

print ("\nCONGRATULATIONS!!! You entered correct\n")