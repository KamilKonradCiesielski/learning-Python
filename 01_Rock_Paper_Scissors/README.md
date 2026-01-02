# ✂️ Rock Paper Scissors

A terminal-based implementation of the classic game, focusing on clean logic and user interaction.

## 🛠️ Logic Overview
The program follows these key steps:
* **User Input:** Accepts choice and sanitizes it using `.lower()` to prevent case-sensitive errors.
* **Computer Choice:** Uses the `random.choice()` method to select a move.
* **Game Loop:** A `while` loop runs until either the player or the computer reaches 3 points.
* **Evaluation:** A series of `if/elif/else` statements determines the winner of each round.

## 🚀 How to Run
1. Open your terminal or command prompt.
2. Run: `python main.py`
