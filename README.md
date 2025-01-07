# **AI 3x3 Tic-Tac-Toe Game**

## **Description**
This project is a Python-based implementation of the classic 3x3 Tic-Tac-Toe game, featuring an intelligent AI opponent powered by the Minimax algorithm with alpha-beta pruning. The game provides a challenging experience for players, allowing them to test their strategy against an optimal AI.

The interface is built using **Pygame**, offering an interactive and visually appealing gaming experience. A slider feature allows users to adjust the AI difficulty dynamically.

---

## **Features**
- **Interactive Gameplay**: Easy-to-use graphical interface for players.
- **AI Opponent**: AI uses the Minimax algorithm with alpha-beta pruning for optimal moves.
- **Adjustable Difficulty**: Players can set the difficulty level via a slider, ranging from 1 (easy) to 9 (hard).
- **Dynamic Game Resizing**: The interface adapts to window resizing for a seamless experience.
- **Game Results**: Displays game outcomes (X wins, O wins, or Draw) in real time.

---

## **Technologies Used**
- **Python**: Core programming language for logic and functionality.
- **Pygame**: Library for graphics and user interaction.
- **Pygame Widgets**: For implementing the difficulty slider.

---

## **How to Play**
1. **Run the Game**:  
   Execute the `main3x3.py` file in a Python environment with Pygame installed.
2. **Set Difficulty**:  
   Use the slider at the bottom to adjust the AI difficulty before starting the game.
3. **Make a Move**:  
   - Click on an empty cell to place your move (X).
   - The AI (O) will respond immediately with its move.
4. **Win Condition**:  
   - Align three Xs or Os in a row, column, or diagonal to win.
   - The game ends in a draw if all cells are filled without a winner.
5. **Restart**:  
   Press `R` to reset the game and adjust the difficulty if desired.

---

## **Requirements**
- **Python 3.7+**
- **Pygame**: Install via `pip install pygame`
- **Pygame Widgets**: Install via `pip install pygame-widgets`

---

## **How It Works**
1. **Game Logic**:  
   - The `checkWin` function determines the game's outcome.
   - The AI uses the `genX` and `genO` functions, guided by Minimax and alpha-beta pruning, to decide its optimal moves.
2. **Difficulty Adjustment**:  
   - The slider controls the AI depth in decision-making, making it smarter at higher levels.
3. **Dynamic Rendering**:  
   - The game dynamically adapts to window resizing, ensuring the grid and elements remain proportional.

---

## **Controls**
- **Mouse Left-Click**: Place your move on the grid.
- **R Key**: Reset the game and adjust difficulty.
- **ESC Key**: Exit the game.


---

## **Future Enhancements**
- Add multiplayer support for two players.
- Implement sound effects for a richer gaming experience.
- Expand to larger grid sizes for more complex gameplay.

