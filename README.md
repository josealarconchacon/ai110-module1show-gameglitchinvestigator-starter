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

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

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
