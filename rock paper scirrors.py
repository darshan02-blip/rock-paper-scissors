import random

# Available choices
choices = ['rock', 'paper', 'scissors']

# Game loop
while True:
    print("\nRock, Paper, or Scissors? (Type 'exit' to quit)")
    player = input("Your choice: ").lower()

    if player == 'exit':
        print("Thanks for playing!")
        break

    if player not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")
