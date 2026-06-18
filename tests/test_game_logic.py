from logic_utils import check_guess, get_range_for_difficulty, initial_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_hard_difficulty_range():
    # If difficulty is "Easy", "Normal", or "Hard", it should return the correct number range
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)
    
def test_difficulty_fallback_range():
    # If difficulty is unrecognized, misspelled, or has wrong casing, it should fall back to the Normal range
    assert get_range_for_difficulty("easy") == (1, 100)
    assert get_range_for_difficulty("HARD") == (1, 100)
    assert get_range_for_difficulty("Normal ") == (1, 100)

def test_initial_attempts_is_zero():
    # attempts must start at 0 to match the "New Game" reset path
    state = initial_game_state(secret=42)
    assert state["attempts"] == 0
