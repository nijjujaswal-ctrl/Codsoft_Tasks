import random

# Choices
choices = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0

print("===================================")
print("     ROCK - PAPER - SCISSORS")
print("===================================")

while True:
    # User input
    user_choice = input(
        "\nChoose rock, paper, or scissors: "
    ).lower()

    # Validate input
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer selection
    computer_choice = random.choice(choices)

    # Display choices
    print("\nYou chose      :", user_choice)
    print("Computer chose :", computer_choice)

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a TIE!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You WIN!")
        user_score += 1

    else:
        print("Result: You LOSE!")
        computer_score += 1

    # Display score
    print("\n----------- SCORE -----------")
    print("Your Score     :", user_score)
    print("Computer Score :", computer_score)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n===================================")
print("          FINAL SCORE")
print("===================================")
print("Your Score     :", user_score)
print("Computer Score :", computer_score)

if user_score > computer_score:
    print("Congratulations! You are the overall winner!")
elif computer_score > user_score:
    print("Computer wins the game!")
else:
    print("The game ended in a tie!")

print("\nThanks for playing!")
