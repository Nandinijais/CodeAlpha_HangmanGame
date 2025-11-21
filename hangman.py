import random

def get_random_word():
    words = ["python", "hangman", "apple", "orange", "coding"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_guesses:
        print("\nCurrent Word:", display_current_state(word, guessed_letters))
        print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")

        guess = input("Enter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print("Incorrect guess!")
        else:
            print("Correct guess!")

        # Check win
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You won! The word was:", word)
            return

    print("\n❌ You lost! The word was:", word)

if __name__ == "__main__":
    hangman()
