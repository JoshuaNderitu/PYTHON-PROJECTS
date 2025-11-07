import random

# Welcome message
name = input("Enter your name: ")
print(f"Welcome to the Hangman Game, {name}!")
print("Guess the programming language...\n")

# List of programming languages
programming_languages = [
    "python", "java", "javascript", "c", "cpp", "csharp", "ruby", "swift", "kotlin",
    "typescript", "go", "rust", "php", "dart", "scala", "r", "perl", "lua", "haskell",
    "matlab", "fortran", "pascal", "cobol", "bash", "powershell", "sql", "objectivec",
    "elixir", "julia", "scheme", "lisp", "prolog", "scratch", "visualbasic", "assembly",
    "fsharp", "groovy", "erlang", "clojure", "vhdl"
]

# Pick a random word
def hangman() :
    word = random.choice(programming_languages)
    guessed_letters = []
    attempts_remaining = len(word) + 2

    # Create initial display (hidden word)
    display_word = ["_"] * len(word)

    while attempts_remaining > 0:
        print("\nCurrent word:", " ".join(display_word))
        print(f"Attempts remaining: {attempts_remaining}")
        print(f"Guessed letters: {' '.join(guessed_letters)}")

        guess = input("Pick a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for index, char in enumerate(word):
                if char == guess:
                    display_word[index] = guess
            print("✅ Correct guess!")
        else:
            attempts_remaining -= 1
            print("❌ Wrong guess!")

        # Check win condition
        if "_" not in display_word:
            print("\n🎉 You win!")
            print(f"The word was: {word}")
            break
    else:
        print("\n💀 Game Over!")
        print(f"The correct word was: {word}")

hangman()

# Ask to play again

while True:
    hangman()
    play_again = input("\nWould you like to play again (y/n)? ").lower()
    if play_again not in ('y', 'yes'):
        print("Thanks for playing Hangman!")
        break


