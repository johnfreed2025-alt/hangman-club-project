import pytest
from hangman_code.functions_for_play_game.make_guess import Make_guess

def test_make_guess_fills_all_matching_letters():
    """Test to check that a word with two or more of the same letter fills in
      the guessed word multiple times"""
    test_letter = "A"
    test_result = Make_guess(
        test_letter,
        ["A", "B", "A", "C", "U", "S"],
        ["_", "_", "_", "_", "_", "_"],
    )
    assert test_result["success"] is True
    assert test_result["word_progress"] == ["A", "_", "A", "_", "_", "_"]

def test_make_guess_wrong_letter_guess():
    """Test to check that the function behaves as expected when a wrong letter
    is inserted"""
    test_letter = "E"
    test_result = Make_guess(
        test_letter,
        ["A", "B", "A", "C", "U", "S"],
        ["_", "_", "_", "_", "_", "_"],
    )
    assert test_result["success"] is False
    assert test_result["word_progress"] == ["_", "_", "_", "_", "_", "_"]