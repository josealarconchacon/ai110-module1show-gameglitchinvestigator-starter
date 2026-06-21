# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

**Prompt I used to generate the tests:**
I fixed `parse_guess` so it rejects guesses outside the difficulty range. What edge case inputs could still break it, things like negative numbers, decimals, huge values, empty input, or messy strings like `'3.'` and `'  5  '`? Write me pytest cases for each one, and include boundary tests to make sure the low and high values themselves are accepted.

> Document how you used AI to help generate or improve tests.

| Edge Case                       | Prompt Used                                                                                                                                                                | AI-Suggested Test                        | Did It Pass? | Your Reasoning                                                                                   |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------ |
| Negative number `"-5"`          | I fixed `parse_guess` to reject guesses outside the difficulty range — what edge cases could still break it, like negative numbers or huge values? Give me pytest cases. | `test_parse_guess_negative_number`       | Yes          | Players might type a negative number to test the lower bound                                     |
| Extremely large value `"99999"` | Same prompt as above                                                                                                                                                       | `test_parse_guess_extremely_large_value` | Yes          | A number way above the range should always fail no matter the difficulty                         |
| Decimal in range `"3.7"`        | Same prompt as above                                                                                                                                                       | `test_parse_guess_decimal_in_range`      | Yes          | Decimals get truncated to int before the range check — needed to confirm valid values still pass |
| Decimal out of range `"0.9"`    | Can you add a test for when a decimal truncates to a value outside the range, like '0.9' becoming 0?                                                                     | `test_parse_guess_decimal_out_of_range`  | Yes          | 0.9 truncates to 0 which is below low=1 — easy edge case to miss                                 |
| Empty string `""`               | First prompt                                                                                                                                                               | `test_parse_guess_empty_string`          | Yes          | Submitting with nothing typed should give a clear message, not crash                             |
| Non-numeric `"abc"`             | First prompt                                                                                                                                                               | `test_parse_guess_non_numeric`           | Yes          | Typing letters is a realistic mistake and the error should be readable                           |
| None input                      | First prompt                                                                                                                                                               | `test_parse_guess_none_input`            | Yes          | No input at all should be handled without throwing an exception                                  |
| Boundary values `"1"`, `"100"`  | Add boundary tests — make sure the low and high values themselves are accepted.                                                                                          | `test_parse_guess_exact_boundary_values` | Yes          | Off-by-one errors could silently block valid guesses at the edges                                |
| Trailing dot `"3."`             | What about messy input like '3.' or whitespace around a number?                                                                                                          | `test_parse_guess_trailing_dot`          | Yes          | "3." is a valid float string in Python — worth confirming it's accepted and truncates cleanly    |
| Whitespace input `"  5  "`      | Same prompt as above                                                                                                                                                       | `test_parse_guess_whitespace_input`      | Yes          | Python's float() strips spaces, so " 5 " resolves to 5 — documents that implicit behavior        |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

|                          | Model A | Model B |
| ------------------------ | ------- | ------- |
| **Model name**           |         |         |
| **Response summary**     |         |         |
| **More Pythonic?**       |         |         |
| **Clearer explanation?** |         |         |

**Which did you prefer and why?**

<!-- Your conclusion -->
