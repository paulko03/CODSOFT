#4)Rock-Paper-scissor

import random
user_score = 0
machine_score = 0

choices = ["rock","paper","scissor"]
def determine_winner(user, machine):
    if user ==machine:
        return "tie"
    elif (user == "rock" and machine == "scissors") or \
         (user == "scissors" and machine == "paper") or \
         (user == "paper" and machine == "rock"):
        return "user"
    else:
        return "computer"

while True:
    print("\n Rock-Paper-Scissor ")
    print("Choose any one: Rock, Paper or Scissors")
    user_choice = input("Your choice: ").lower()
    if user_choice not in choices:
        print("Invalid choice.")
        continue
    machine_choice = random.choice(choices)
    print(f"Machine chose: {machine_choice}")

    result = determine_winner(user_choice, machine_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
        user_score += 1
    else:
        print("machine wins!")
        machine_score += 1

    print(f"Your Score: {user_score} | Machine Score: {machine_score}")
