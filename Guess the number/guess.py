import random

def guess(x):
    number = random.randint(1, x)
    guess = 0

    while number != guess:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess > number:
            print("Sorry, number is too high. ")
        if guess < number:
            print("Sorry, number is too low. ")
    print("Nice! correct number.")
    quit()

x = int(input("Pick the limit to guess: "))
guess(x)