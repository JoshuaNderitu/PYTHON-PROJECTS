import random

name = input("Enter your name: ")
print(f"Welcome to Rock Paper Scissors {name}\n")

player_score = 0
computer_score = 0
options = ["r", "p", "s"]
choice_map = {"r": "rock", "p": "paper", "s": "scissors"}

while True:
    choice = input("Enter rock, paper, or scissors (r/p/s) or 'q' to quit: ").lower()
    
    if choice == "q":
        print(f"\nFinal Score - {name}: {player_score}, Computer: {computer_score}")
        print("Thanks for playing!")
        break
    
    if choice not in options:
        print("Invalid choice. Please try again.\n")
        continue
    
    computer_choice = random.choice(options)
    
    print(f"You chose: {choice_map[choice]}")
    print(f"Computer chose: {choice_map[computer_choice]}\n")
    
    if choice == computer_choice:
        print("It's a tie!\n")
    elif (choice == "r" and computer_choice == "s") or \
         (choice == "p" and computer_choice == "r") or \
         (choice == "s" and computer_choice == "p"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    print(f"Score - {name}: {player_score}, Computer: {computer_score}\n")
