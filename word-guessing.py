import random

# Greet the player
name = input("Welcome to word guessing\n. Please enter your name: ")
print(f"Good luck {name}")

# words: a single comma-separated string inside a list (split if you want individual words)
words = [
    "daughter", "romantic", "flu", "feminist", "moon", "clerk", "deserve", "clue",
    "killer", "bow", "lamp", "unfortunate", "dealer", "ban", "sculpture", "exit",
    "neutral", "accumulation", "confine", "inhibition", "revenge", "thread", "criticism",
    "study", "polite", "ignorant", "discover", "morale", "leaflet", "recover", "chapter",
    "pneumonia", "action", "satisfaction", "abundant", "category", "horseshoe", "canvas",
    "brain", "novel", "sunday", "likely", "ghost", "freckle", "dance", "slap", "invisible",
    "restless", "mind", "motivation"
]


# pick the target word
word = random.choice(words) # generating a random word

# track guesses and remaining turns
guesses = ''
turns = 12

# main game loop
while turns > 0:
    guess = input("Guess the characters: ")
    guesses += guess
    
    failed = 0
    # reveal guessed characters, hide others as underscores
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()  # move to new line after each round


    # win if no unrevealed characters remain
    if failed == 0:
        print(f"Congratulations you got it right.\n The word is {word}")
        break
    # wrong guess reduces turns
    elif guess not in word:
        turns -= 1
        print(f"Wrong.\n You have {turns} more guesses")
        # lose message when out of turns
        if turns == 0:
            print(f"💀 You lose. The word was '{word}'.")

