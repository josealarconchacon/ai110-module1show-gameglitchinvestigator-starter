# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  When I first ran the game, it looked functional on the surface, the UI loaded, I could type a guess and submit it. But as soon as I started playing, things felt off. The hints were pointing me in the wrong direction, one was the difficulty settings weren't doing what I expected, and the attempt counter showed different numbers depending on whether I had just loaded the page or clicked New Game.

- List at least two concrete bugs you noticed at the start  
   (for example: "the hints were backwards").

  Bug 1, check_guess() has backwards hint logic
  I expected that if my guess was too high, the game would tell me to go lower. Instead, when I guessed 80 and the secret was 40, the hint said "Go HIGHER!", the exact opposite of what I needed.

  Bug 2, New Game resets attempts to 0, but fresh starts at 1.
  I expected the attempt counter to be consistent regardless of how I started the game. Instead, on a fresh page load attempts initializes to 1, so the display immediately shows one attempt already used before I guessed anything. After clicking New Game, attempts resets to 0 and the full count is restored.

  **Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input         | Expected Behavior      | Actual Behavior          | Console Output / Error |
| ------------- | ---------------------- | ------------------------ | ---------------------- |
| 80            | Go LOWER               | Go HIGHER                | None                   |
|               |                        |                          |                        |
| Select        | It should show 1–200   | Range shows 1–50         | None                   |
| Hard          | or higher              |                          |                        |
| difficulty    |                        |                          |                        |
|               |                        |                          |                        |
| Select Easy   | Instruction should say | Instruction always       | None                   |
| range is from | Guess a number from    | say Guess a number       |                        |
| 1 - 20        | 1 - 20                 | from 1 - 100             |                        |
|               |                        | regardless of difficulty |                        |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - **What the AI suggested:** While reviewing `get_range_for_difficulty` in `logic_utils.py`, agent mode pointed out that the Hard difficulty was set to return `(1, 50)`, which was actually narrower than Normal `(1, 100)`. It suggested updating Hard to `(1, 200)` to better reflect the intended difficulty progression.
  - **How I verified it:** I double-checked the difficulty logic manually and compared all ranges: Easy was `(1, 20)` and Normal was `(1, 100)`, so Hard should reasonably extend beyond Normal rather than shrink. I then validated the change by running the existing test `test_hard_difficulty_range`, which passed after the update, confirming that Hard correctly returns `(1, 200)`.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
