# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game purpose:** It's a number guessing game. You pick a difficulty, and the game picks a secret number. You have a limited number of attempts to guess it, and after each guess you get a hint telling you to go higher or lower. Your score changes based on how many attempts it takes and whether your guesses are in the right direction.

**Bugs I found:**

1. The secret number kept changing every time I clicked Submit. The game was picking a new random number on each interaction instead of locking the value in session state, so I was basically chasing a moving target.
2. The hints were completely backwards. Guessing too high told you to go higher, and guessing too low told you to go lower. The comparison logic in `check_guess` had the "Too High" and "Too Low" returns swapped.
3. Hard mode was easier than Normal. The range for Hard was set to 1-50, which is a smaller range than Normal (1-100). That's the opposite of what Hard should mean.
4. Out-of-range guesses were accepted without complaint. Typing a number like 500 on Easy mode (range 1-20) would go through and get processed as a valid guess.

**Fixes I applied:**

1. Moved the secret number into `st.session_state` so it only gets generated once at the start of a game and stays put until the player starts a new one.
2. Swapped the return values in `check_guess` so "Too High" returns when the guess is above the secret, and "Too Low" returns when it's below.
3. Updated Hard mode's range to 1-200 so the difficulties actually scale in order: Easy (1-20), Normal (1-100), Hard (1-200).
4. Added range validation in `parse_guess` to reject anything outside the current difficulty's bounds before it ever reaches the game logic.

## 📸 Demo Walkthrough

The secret number for this run is **63** (Normal difficulty, range 1-100, 8 attempts allowed).

1. I type **40** and hit Submit. The game says "Too Low", so I know the answer is somewhere above 40. Score drops by 5 (now 95).
2. I type **70**. This time I get "Too High", which puts me in the 41–69 range. Score drops by 5 again (now 90).
3. I try **55**. Still "Too Low", narrowing it down to 56–69. Score is 85.
4. I guess **65**. "Too High", so it's somewhere between 56 and 64. Score sits at 80.
5. I enter **60**. "Too Low", range is now 61–64. Score is 75.
6. I type **63** and hit Submit. "The game says You already won. Start a new game to play again". Balloons go off on screen.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
