import random

number = random.randint(1, 100)
guess = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        guess +=1

    
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number.")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")