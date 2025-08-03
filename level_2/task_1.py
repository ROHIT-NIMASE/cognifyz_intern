import random

def guessing_game():
    print("🎲 Welcome to the Guessing Game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⛔ Please guess a number **within 1 to 100**.")
            elif guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number {secret_number} in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

guessing_game()
'''🎲 Welcome to the Guessing Game!
Guess a number between 1 and 100: 45
📈 Too high! Try again.
Guess a number between 1 and 100: 12
📉 Too low! Try again.
Guess a number between 1 and 100: 25
📉 Too low! Try again.
Guess a number between 1 and 100: 50
📈 Too high! Try again.
Guess a number between 1 and 100: 35
📉 Too low! Try again.
Guess a number between 1 and 100: 40
📉 Too low! Try again.
Guess a number between 1 and 100: 41
📉 Too low! Try again.
Guess a number between 1 and 100:
❌ Invalid input! Please enter a valid number.
Guess a number between 1 and 100: 41
📉 Too low! Try again.
Guess a number between 1 and 100:
❌ Invalid input! Please enter a valid number.
Guess a number between 1 and 100: 42
📉 Too low! Try again.
Guess a number between 1 and 100: 43
🎉 Correct! You guessed the number 43 in 10 attempts.'''
