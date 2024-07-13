import random

choices = ["rock", "paper", "scissor"]

user_choice = input("Rock, Paper, Scissor? ").lower()

if user_choice not in choices:
    print("Invalid choice!")
    exit()

computer_choice = random.choice(choices)

wins = {"rock": "scissor", "paper": "rock", "scissor": "paper"}

result = "Tie" if user_choice == computer_choice else "You win!" if wins[user_choice] == computer_choice else "You lose!"

print(f"{result} You chose {user_choice}, computer chose {computer_choice}.")
