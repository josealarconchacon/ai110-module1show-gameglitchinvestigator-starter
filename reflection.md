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
  - **What the AI did:** While fixing the `check_guess` logic, the AI misled the emoji mapping by pairing a downward chart with Go HIGHER! and an upward chart with Go LOWER!.
  - **How I verified it:** I caught the misleading icons during a quick visual review of the UI. While the logic worked, I felt the emojis could easily confuse players. I simply swapped the emojis to correctly match the words.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I decided the bug was fixed when I guessed 25 with a secret of 15, and the hint changed from Go HIGHER to Go LOWER, which is the correct direction.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  - I ran a pytest unit test called test_hard_difficulty_range() that checked the outputs for Easy, Normal, and Hard inputs.
  - The test successfully passed, which showed me that the logic error in the Hard was completely fixed. Originally, it was returning (1, 50), making it narrower and easier than Normal mode. Seeing the test pass with the new output of (1, 200) proved that the conditional logic is now branching correctly and that Hard mode finally scales the difficulty properly to be tougher than Normal.
- Did AI help you design or understand any tests? How?
  - Yes, the AI helped me figure out how to test the st.info() banner bug. Since the issue was locked inside the UI, it suggested a manual test instead and walked me through a visual walkthrough. By switching between all three difficulties to watch the banner in real-time.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Every time you click a button or do anything in a Streamlit app, the whole Python script reruns from the top, like it's starting over. That's what was causing the attempts counter bug. On a fresh load, `attempts` was set to 1 in the code, so before I even guessed anything, it already counted one attempt. Session state is how you save values across those reruns, because anything stored in `st.session_state` actually sticks around instead of getting reset. Once I understood that, I could see why `New Game` had to reset through session state and not just a regular variable.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - Running a manual test right after every fix before moving on is something I want to keep doing, because it stopped me from stacking bugs on top of each other. Catching the hint logic bug early by just playing the game for a minute saved me way more time than if I had found it later.

- What is one thing you would do differently next time you work with AI on a coding task?
  - I'd question the AI's output a little earlier instead of assuming it's right and then catching it during a review. The emoji mistake slipped through because I was focused on the logic and not the full picture of what the player would actually see.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - I used to think AI-generated code either worked or it didn't, but this project showed me it can be logically correct and still wrong in a way that matters. Now I think of AI more like a draft that I still have to read and own before it goes anywhere.
