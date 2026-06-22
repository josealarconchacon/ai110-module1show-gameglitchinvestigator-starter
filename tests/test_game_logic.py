from logic_utils import check_guess, get_range_for_difficulty, initial_game_state, parse_guess

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

# --- parse_guess edge cases ---
def test_parse_guess_negative_number():
    # Negative numbers are below the valid range and must be rejected
    ok, value, err = parse_guess("-5", 1, 100)
    assert ok is False
    assert value is None
    assert "1" in err and "100" in err

def test_parse_guess_extremely_large_value():
    # Numbers far above the upper bound must be rejected regardless of difficulty
    ok, value, err = parse_guess("99999", 1, 200)
    assert ok is False
    assert value is None
    assert "200" in err

def test_parse_guess_decimal_in_range():
    # int(float("3.7")) truncates to 3, not rounds to 4
    ok, value, err = parse_guess("3.7", 1, 100)
    assert ok is True
    assert value == 3
    assert err is None

def test_parse_guess_decimal_out_of_range():
    # "0.9" truncates to 0, which is below low=1
    ok, value, _ = parse_guess("0.9", 1, 100)
    assert ok is False
    assert value is None

def test_parse_guess_trailing_dot():
    # "3." is a valid float string — should be accepted and coerced to 3
    ok, value, err = parse_guess("3.", 1, 100)
    assert ok is True
    assert value == 3
    assert err is None

def test_parse_guess_whitespace_input():
    # strips surrounding whitespace, so "  5  " is accepted as 5
    ok, value, err = parse_guess("  5  ", 1, 100)
    assert ok is True
    assert value == 5
    assert err is None

def test_parse_guess_empty_string():
    # Empty input must be rejected with a prompt to enter a guess
    ok, value, _ = parse_guess("", 1, 100)
    assert ok is False
    assert value is None

def test_parse_guess_non_numeric():
    # Non-numeric strings must be rejected with a clear error
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert value is None
    assert "not a number" in err.lower()

def test_parse_guess_none_input():
    # None input (no guess submitted) must be handled gracefully
    ok, value, _ = parse_guess(None, 1, 100)
    assert ok is False
    assert value is None

def test_parse_guess_exact_boundary_values():
    # Boundary values (low and high) must be accepted as valid
    ok_low, val_low, _ = parse_guess("1", 1, 100)
    ok_high, val_high, _ = parse_guess("100", 1, 100)
    assert ok_low is True and val_low == 1
    assert ok_high is True and val_high == 100
