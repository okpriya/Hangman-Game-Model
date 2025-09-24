import re
from collections import Counter

class HangmanAI:
    def __init__(self, dictionary_file="words.txt"):
        with open(dictionary_file, "r") as f:
            self.dictionary = [w.strip().lower() for w in f.readlines()]

    def next_guess(self, currentWordState, guessedLetters, guessesRemaining):
        # Convert state into regex (e.g., "_ _ e _ a n" -> "^..e.an$")
        pattern = "^" + currentWordState.replace(" ", "").replace("_", ".") + "$"

        # Candidate words matching pattern
        candidates = [w for w in self.dictionary if re.match(pattern, w)]

        # Exclude words with wrongly guessed letters
        wrong_guesses = [g for g in guessedLetters if g not in currentWordState]
        candidates = [w for w in candidates if all(l not in w for l in wrong_guesses)]

        # Count frequency of remaining letters
        freq = Counter("".join(candidates))

        # Remove already guessed letters
        for g in guessedLetters:
            if g in freq:
                del freq[g]

        # Pick most frequent letter, or fallback
        if freq:
            return max(freq, key=freq.get)
        else:
            for l in "etaoinshrdlucmfwypvbgkjqxz":
                if l not in guessedLetters:
                    return l
        return None
