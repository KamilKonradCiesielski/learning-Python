# 🎲 Cho-Han CLI Edition

A lightweight, terminal-based version of the traditional Japanese dice game **Cho-Han**. This script focuses on clean procedural logic, loop management, and terminal I/O.



## 🛠️ Logic & Features

This version demonstrates core Python programming concepts:

* **Dynamic Range:** Instead of a single round, the program uses a `for` loop combined with `input()` to allow the user to define the number of rounds (`liczba_gier`) they want to play.
* **Procedural Game Loop:** Manages a sequence of inputs, calculations, and outputs within a controlled iteration.
* **Logical Conditionals:** Implements complex `if/elif` statements using Boolean logic (`and`, `or`, `%` modulo) to evaluate the game result based on the parity of the dice sum.
* **Randomization:** Utilizes the `random.randint` method to simulate fair and unpredictable dice rolls.

## 🕹️ How the Logic Works

1.  **Input Phase:** The program prompts for the number of games and the player's choice ('p' for Even, 'n' for Odd).
2.  **Simulation:** Two dice are rolled, and their sum is calculated.
3.  **Validation:**
    * If `sum % 2 == 0` and player chose `p` -> **Win**.
    * If `sum % 2 != 0` and player chose `n` -> **Win**.
    * Otherwise -> **Loss**.



## 🚀 How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the directory containing the file.
3.  Execute the script:
    ```bash
    python main.py
    ```
4.  Enter the number of rounds and start betting!
