import random

def hangman():
    words = ["python", "internship", "computer", "program", "hangman"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word: " + " ".join(guessed))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        print("Current word:", " ".join(guessed))

        if "_" not in guessed:
            print("Congratulations! You guessed the word:", word)
            return

    print("Game Over! The word was:", word)

hangman()
