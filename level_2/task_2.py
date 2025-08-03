import random

def number_guesser():
    print("🎯 Welcome to the Number Guesser Game!")

    try:
        lower = int(input("Enter the lower bound of the range: "))
        upper = int(input("Enter the upper bound of the range: "))

        if lower >= upper:
            print("❌ Invalid range. Lower bound must be less than upper bound.")
            return

        secret_number = random.randint(lower, upper)
        attempts = 0

        while True:
            try:
                guess = int(input(f"Guess a number between {lower} and {upper}: "))
                attempts += 1

                if guess < lower or guess > upper:
                    print("⚠️ Guess out of range. Try again.")
                elif guess < secret_number:
                    print("📉 Too low! Try again.")
                elif guess > secret_number:
                    print("📈 Too high! Try again.")
                else:
                    print(f"🎉 Correct! You guessed the number {secret_number} in {attempts} attempts.")
                    break

            except ValueError:
                print("❌ Invalid input. Please enter a number.")

    except ValueError:
        print("❌ Please enter valid integers for the range.")


number_guesser()
'''🎯 Welcome to the Number Guesser Game!
Enter the lower bound of the range: 20
Enter the upper bound of the range: 80
Guess a number between 20 and 80: 50
📉 Too low! Try again.
Guess a number between 20 and 80: 70
📈 Too high! Try again.
Guess a number between 20 and 80: 65
🎉 Correct! You guessed the number 65 in 3 attempts.'''

