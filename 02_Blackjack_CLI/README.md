# 🃏 Blackjack Terminal Game & Logic Practice

A Python-based implementation of the classic Blackjack (Oczko) game. This project focuses on structured data management, functional deck generation, and implementing automated dealer rules.

## 📝 Challenge Description
The program simulates a card game where the player competes against a dealer. It manages a 52-card deck and calculates scores based on custom values, ensuring that the game logic follows standard casino "hit or stand" mechanics.

**The logic follows these stages:**
- **Functional Deck Construction:** Uses four separate functions to generate suits and merges them into a single, shuffled 52-string list.
- **Dynamic Scoring System:** Maps card ranks (strings) to integer values using a dictionary lookup, handling face cards with custom point values (J:2, Q:3, K:4, A:11).
- **Player Decision Loop:** A `while` loop that monitors the player's total and allows for iterative "hit" (draw) decisions until a "stand" or "bust" (score > 21).
- **Automated Dealer AI:** Implements the "Hit on 16, Stand on 17" rule, where the dealer automatically draws cards until their score is $\ge 17$.
- **Session Management:** Allows the user to define a specific number of rounds (1–10) to be played in a single execution.



## 🛠️ Key Concepts Covered
In this project, I practiced:
* **Dictionary Mapping** – Using Python dictionaries (`.get()`) to translate string-based card ranks into numerical values for arithmetic operations.
* **List Manipulation & State** – Using `.pop()` to remove cards from the deck and `.append()` to update hands, ensuring cards cannot be drawn twice.
* **Nested Control Flow** – Managing multiple `while` loops (for rounds, player turns, and dealer turns) to maintain a clean game state.
* **String Formatting (f-strings)** – Utilizing modern Python f-strings for readable, real-time score and hand reporting in the console.

## 📊 Expected Behavior
| Situation | Logic | Result |
| :--- | :--- | :--- |
| Player has 18, Dealer has 17 | ✅ Higher score | `WYGRAŁEŚ!` |
| Player draws to 24 | ❌ Bust condition | `PRZEGRAŁEŚ! (Przekroczyłeś 21)` |
| Dealer has 14 | 🤖 AI Rule | `Krupier dobiera...` |
| Player 20, Dealer 20 | 🤝 Equal score | `REMIS!` |

## 🛠️ How to run it
1. Ensure you have **Python 3.x** installed.
2. Clone this repository or download the `.py` file.
3. Run the program:
   ```bash
   python main.py
