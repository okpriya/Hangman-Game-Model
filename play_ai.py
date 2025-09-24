from hangman import HangmanAI

# Initialize AI with dictionary
ai = HangmanAI("words.txt")

# Example secret word (you can change this)
secret_word = "apple"
currentWordState = "_ " * len(secret_word)   # "_ _ _ _ _"
currentWordState = currentWordState.strip()
guessedLetters = []
guessesRemaining = 6   # classic Hangman limit

print("🔤 Starting Hangman AI Game!")
print("Secret word has", len(secret_word), "letters.")
print("Current State:", currentWordState)

while "_" in currentWordState and guessesRemaining > 0:
    guess = ai.next_guess(currentWordState.replace(" ", ""), guessedLetters, guessesRemaining)
    print(f"\n🤖 AI guesses: {guess}")

    guessedLetters.append(guess)

    # Check if guess is in secret word
    if guess in secret_word:
        # Update currentWordState
        new_state = list(currentWordState.replace(" ", ""))
        for i, ch in enumerate(secret_word):
            if ch == guess:
                new_state[i] = guess
        currentWordState = " ".join(new_state)
        print("✅ Correct guess!")
    else:
        guessesRemaining -= 1
        print("❌ Wrong guess! Remaining attempts:", guessesRemaining)

    print("Word State:", currentWordState)

# Final result
if "_" not in currentWordState:
    print("\n🎉 AI solved the word:", secret_word)
else:
    print("\n💀 AI failed! The word was:", secret_word)
