import random
sides = 6
def roll_dice():
    return random.randint(1, sides)

def main():
    print("Welcome to the Dice Roll Simulator!")

    while True:
        user_input = input("Press 'r' to roll the dice or 'q' to quit: ").lower()

        if user_input == 'r':
            result = roll_dice()
            print(f"You rolled a {result}!")
        elif user_input == 'q':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()