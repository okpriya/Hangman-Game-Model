from hangman import HangmanAI

def evaluate(ai, test_words):
    success, total_mistakes = 0, 0
    
    for word in test_words:
        guessed = ["_"] * len(word)
        guessed_letters = []
        guesses_remaining = 6
        mistakes = 0

        while guesses_remaining > 0 and "_" in guessed:
            guess = ai.next_guess(" ".join(guessed), guessed_letters, guesses_remaining)
            guessed_letters.append(guess)

            if guess in word:
                for i, c in enumerate(word):
                    if c == guess:
                        guessed[i] = c
            else:
                guesses_remaining -= 1
                mistakes += 1

        if "".join(guessed) == word:
            success += 1
        total_mistakes += mistakes

    accuracy = success / len(test_words) * 100
    avg_mistakes = total_mistakes / len(test_words)

    print("\n📊 Evaluation Results")
    print(f"✅ Accuracy: {accuracy:.2f}%")
    print(f"⚡ Avg mistakes per word: {avg_mistakes:.2f}")

if __name__ == "__main__":
    ai = HangmanAI("words.txt")

    with open("words.txt") as f:
        test_words = [w.strip().lower() for w in f.readlines()]

    evaluate(ai, test_words)
from hangman import HangmanAI

# Initialize AI with dictionary
ai = HangmanAI("words.txt")

# Example game state
currentWordState = "_ p p _ e"   # underscores for missing letters
guessedLetters = ["a", "e", "i", "o", "u", "p"]
guessesRemaining = 5

# AI makes a guess
guess = ai.next_guess(currentWordState, guessedLetters, guessesRemaining)
print("AI suggests:", guess)
