Tic Tac Toe Game in Python

### 🎮 Advanced Tic Tac Toe Game in Python (with AI, Sound & Score Saving)

This is a beginner-friendly yet advanced **Tic Tac Toe game** written in Python. It supports two game modes—**Human vs Human** and **Human vs Computer (AI)**—and includes sound effects, error handling, and automatic score saving.

---

### 🚀 Features

* ✅ **Two Modes**:

  * 👥 Human vs Human
  * 🤖 Human vs AI (Minimax Algorithm)

* 🧠 **Smart Computer AI**:
  Uses the **Minimax algorithm** to make optimal moves and challenge the player.

* 🔊 **Sound Effects**:

  * Win sound (`win.mp3`)
  * Draw sound (`draw.mp3`)
  * Error sound for invalid input (`error.mp3`)

* 🗂️ **Score Tracking & Saving**:
  Final scores are saved automatically to a file called `scores.txt`.

* 🧩 **Beginner-Friendly Code**:
  Code is clean, modular, and easy to follow for those learning Python.

---

### 🛠️ Setup Instructions

1. **Clone the repository** or download the `.py` file.
2. Make sure you have Python 3 installed.
3. Install the required library for playing sound:

   ```bash
   pip install playsound
   ```
4. Create a folder named `Sound Effects` on your **Desktop**, and add the following files to it:

   * `win.mp3`
   * `draw.mp3`
   * `error.mp3`

   Or update the path in `play_sound()` function to match your custom sound file location.

---

### 🎯 How to Play

* Run the game:

  ```bash
  python your_file_name.py
  ```
* Choose your game mode (1 or 2).
* Enter your name(s) and choose 'X' or 'O'.
* Play as usual. If you win, draw, or make an invalid move, sound effects will play.
* When the game ends, check `scores.txt` for a summary.

---

### 🧑‍🔧 Customization Tips

* **Change Sound Folder**:
  Update the path in the `play_sound()` function:

  ```python
  sound_path = os.path.join("C:/Your/Custom/Path", file_name)
  ```

* **Disable Sound**:
  Simply comment out or remove the `play_sound()` calls in the script.

* **Customize Symbols or UI**:
  You can change the symbols used in the `printBoard()` function to emojis or other characters.

---
### 📽️ Demo Video 
