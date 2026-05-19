import random

while True:

    print("🎮 WELCOME TO THE GAME ARCADE! 🎮")
    print("1. Rock Paper Scissors")
    print("2. Number Guessing Game")

    choice = input("Pick a game (1 or 2): ")

    # ROCK PAPER SCISSORS
    if choice == "1":
        print("\nLet's play Rock Paper Scissors!")
        options = ['rock', 'paper', 'scissors']

        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(options)

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!🤝")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("🏆You win!🏆")
        else:
            print("💀Computer wins!💀")

    # NUMBER GUESSING
    elif choice == "2":
        print("\nWelcome to the Number Guessing Game!")
        secret = random.randint(1, 100)
        attempts = 0

        while True:
            try:
                guess = int(input("Guess number (1-100): "))
                attempts += 1

                if guess > secret:
                    print("📉 Too high!")
                elif guess < secret:
                    print("📈 Too low!")
                else:
                    print(f"🏆 Correct! {secret} in {attempts} tries!")
                    break

            except:
                print("❌ Enter a valid number!")

    else:
        print("Invalid choice!")

    replay = input("Do you want to play again? (y/n): ").lower()

    if replay != "y":
        break

print("Thanks for playing! 👋")