import random

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors Game ---")
    print("Choose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice (1/2/3): ")

    if user_choice == "1":
        user = "rock"
    elif user_choice == "2":
        user = "paper"
    elif user_choice == "3":
        user = "scissors"
    else:
        print("Invalid choice! Try again.")
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

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
