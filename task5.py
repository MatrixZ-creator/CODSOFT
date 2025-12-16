import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("Instructions:")
    print("rock beats scissors")
    print("scissors beats paper")
    print("paper beats rock")

    user = input("\nChoose rock, paper, or scissors: ").lower()

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("Result: It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: You Lose!")
        computer_score += 1

    print("Score → You:", user_score, "| Computer:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break
