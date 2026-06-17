def initial_game_state(secret: int) -> dict:
    """Returns default state for a new game."""
    return {
        "secret": secret,
        # FIX: Refactored game initialization into a helper function. 
        # During review, agent mode identified that attempts should begin at 0 so players don't 
        # appear to have guessed before the game starts.
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            # FIX: Swapped Go HIGHER! to Go LOWER!
            # Used agent mode to help debug the integer comparison logic; 
            # It helped identify that the hints were being shown backwards.
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            # FIX: While reviewing the code together, agent mode spot the same reversed hint 
            # logic in the TypeError fallback path.
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
