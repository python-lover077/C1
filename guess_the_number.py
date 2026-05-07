import random

def guess_the_number():
    """
    A simple number guessing game using the random module.
    The player has to guess a random number between 1 and 100.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    print("=" * 50)
    
    while not guessed:
        try:
            guess = int(input("\nEnter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1
            
            if guess < secret_number:
                print(f"Too low! Try again. (Attempt {attempts})")
            elif guess > secret_number:
                print(f"Too high! Try again. (Attempt {attempts})")
            else:
                guessed = True
                print(f"\n🎉 Congratulations! You guessed the number {secret_number}!")
                print(f"You took {attempts} attempt(s).")
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            print("\n" + "=" * 50)
            guess_the_number()
        elif play_again in ['no', 'n']:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")
