Hangman AI 
## Overview
This project implements an AI that plays the Hangman game.  
The AI is tested against a dataset of **100 airline-related words** and evaluated on accuracy and mistakes per word.

### Approach / Strategy
- **Dictionary Filtering**: Candidate words are filtered from a dictionary (`words.txt`) to match the current known pattern.
- **Frequency Analysis**: Among candidate words, the AI selects the most frequent letter that has not yet been guessed.
- **Heuristics**:
  - Eliminate words containing letters known to be incorrect.
  - Update guesses dynamically as word state changes.

### Evaluation
The script evaluates:
- **Accuracy**: Percentage of words guessed correctly.
- **Avg Mistakes**: Average number of wrong guesses per word.
### Example Result
📊 Evaluation Results
✅ Accuracy: 57.28%
⚡ Avg mistakes per word: 3.57
