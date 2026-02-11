# 🎲 Cho-Han GUI Game

A professional, object-oriented implementation of the traditional Japanese dice game **Cho-Han**, built using Python's **Tkinter** library.



## 🛠️ Technical Features

This project focuses on clean code structure and modern GUI principles:

* **Object-Oriented Programming (OOP):** The game is structured into multiple classes (`Menu`, `GryWidok`, `PauzaEkran`), ensuring a clean separation of concerns.
* **Dynamic State Management:** Uses a frame-switching logic to navigate between the main menu, the active game, and the result screen without opening multiple windows.
* **Event Handling:** Implements `self.root.after()` for timed transitions, allowing users to see results before moving to the next screen.
* **Custom Styling:** A sleek "Dark Mode" aesthetic with customized buttons, fonts, and layout using `expand=True` and `fill="both"` for responsiveness.

## 🕹️ Game Logic

The program simulates a traditional dice throw:
1.  **Randomization:** Generates two independent dice rolls (1-6) using the `random` module.
2.  **User Choice:** The player predicts if the sum is **Even** (Cho) or **Odd** (Han).
3.  **Validation:** Automatically calculates the sum and compares it with the user's input to determine the winner.



## 🚀 How to Run

1.  **Requirement:** You need Python installed.
2.  **Download:** Save the `main.py` file to your computer.
3.  **Run:** Execute the script via terminal:
    ```bash
    python main.py
    ```
4.  **Play:** Use the GUI buttons to start the game and place your bets!
