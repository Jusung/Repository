import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number (1-100):")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! It took you {attempts} attempts.")
            break

guess_number()