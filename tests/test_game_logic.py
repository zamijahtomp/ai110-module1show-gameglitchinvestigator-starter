import os

import pytest

from logic_utils import check_guess, get_range_for_difficulty, update_score

# Absolute path to app.py so AppTest works regardless of the current directory.
APP_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "app.py")


# ---------------------------------------------------------------------------
# check_guess tests. check_guess returns an (outcome, message) tuple, so we
# unpack it and assert on the outcome.
# ---------------------------------------------------------------------------

# FIXED: updated winning guess checks to receive a tuple
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# Regression tests for the "New Game" fix.
#
# The bug: the New Game handler used random.randint(1, 100) (a hardcoded range
# that ignored difficulty) and never reset status/score/history. After a
# win/loss, "New Game" was effectively dead because status stayed "won"/"lost"
# and the st.stop() guard halted the app.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 50)),
        ("Hard", (1, 100)),
        ("Unknown", (1, 100)),  # fallback
    ],
)
def test_range_matches_difficulty(difficulty, expected):
    # The New Game fix relies on this range contract to pick an in-range secret.
    assert get_range_for_difficulty(difficulty) == expected


def _click_new_game(at):
    for button in at.button:
        if "New Game" in button.label:
            button.click()
            return
    raise AssertionError("New Game button not found")


def test_new_game_secret_respects_difficulty_range(monkeypatch):
    # Make randint deterministic: always return the high end of whatever range
    # it's given. The default difficulty is Normal => range (1, 50), so the fix
    # yields a secret of 50. The old bug called randint(1, 100) => 100, which
    # exceeds the Normal range and fails this test.
    import random

    monkeypatch.setattr(random, "randint", lambda low, high: high)

    from streamlit.testing.v1 import AppTest

    at = AppTest.from_file(APP_PATH, default_timeout=10)
    at.run()

    _click_new_game(at)
    at.run()

    assert at.session_state["secret"] <= 50, (
        "New Game picked a secret outside the Normal range "
        "(hardcoded 1-100 bug reintroduced)"
    )


def test_new_game_resets_state_after_win():
    from streamlit.testing.v1 import AppTest

    at = AppTest.from_file(APP_PATH, default_timeout=10)
    at.run()

    # Simulate a finished, dirty game.
    at.session_state["status"] = "won"
    at.session_state["score"] = 999
    at.session_state["attempts"] = 5
    at.session_state["history"] = [10, 20, 30]
    at.run()

    _click_new_game(at)
    at.run()

    assert at.session_state["status"] == "playing", "status not reset (game stays over)"
    assert at.session_state["score"] == 0, "score not reset"
    assert at.session_state["attempts"] == 0, "attempts not reset"
    assert at.session_state["history"] == [], "history not reset"


# ---------------------------------------------------------------------------
# update_score tests. attempt_number is 1-based (incremented before scoring).
# ---------------------------------------------------------------------------

def test_first_guess_win_scores_100():
    assert update_score(0, "Win", 1) == 100


def test_win_bonus_drops_by_10_per_attempt():
    assert update_score(0, "Win", 2) == 90
    assert update_score(0, "Win", 3) == 80


def test_late_win_clamps_to_minimum_10():
    # A very late win never drops below the 10-point floor.
    assert update_score(0, "Win", 20) == 10


def test_wrong_guess_always_penalizes():
    # Neither Too High nor Too Low should ever increase the score.
    assert update_score(0, "Too High", 2) == -5
    assert update_score(0, "Too High", 3) == -5
    assert update_score(0, "Too Low", 2) == -5
