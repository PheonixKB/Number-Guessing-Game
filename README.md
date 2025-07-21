# 🎯 Number Guessing Game (Python)

A simple terminal-based Number Guessing Game developed in Python where the player tries to guess a number between 1 and 100. The game offers multiple difficulty levels and keeps track of your best attempts and fastest time for each level.

---

## 🧠 Features

- ✅ 3 Difficulty Levels: Easy, Medium, and Hard  
- 🕒 Time Tracking: Measures how long you take to guess the number  
- 🏆 Scoreboard: Tracks your best attempts and fastest time per difficulty  
- 💡 Smart Hints: Provides helpful hints after a few wrong attempts  
- 🔁 Replayable: Option to play multiple rounds in a single session  
- 🧪 Input Validation: Handles invalid inputs gracefully  

---

## 📋 Rules

- The computer randomly selects a number between 1 and 100.
- You must guess the number within a limited number of attempts:
  - **Easy**: 10 attempts
  - **Medium**: 5 attempts
  - **Hard**: 3 attempts
- A hint is provided after a specific number of attempts:
  - **Easy**: After 7 wrong guesses
  - **Medium**: After 3 wrong guesses
  - **Hard**: After 2 wrong guesses
- Scores and times are saved during the session for personal bests.

---

## 💻 How to Run

Make sure you have Python installed on your system. Then:

```bash
git clone https://github.com/your-username/number-guessing-game.git
cd number-guessing-game
python number_guessing_game.py
