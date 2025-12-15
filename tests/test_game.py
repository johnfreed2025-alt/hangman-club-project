import pytest

# from re import fullmatch
from hangman_code.game import Game


def test_display_word():
    """Test to check that the word and the blanks are
    correctly outputted for display to the player"""
    test_words = [
        "apple",
        "ra__i_",
        "Lockleaze_is_great",
        "I like wine",
        "Oopsie123",
        "1__A__3",
    ]
    test_result = [0, 0, 0, 0, 0, 0]
    expected = ["APPLE", "RA__I_", ValueError, ValueError, ValueError, ValueError]
    for i, x in enumerate(test_words):
        try:
            result = Game.display_word(x)
        except Exception as e:
            result = type(e)
        test_result[i] = result
    msg = f"Expected {expected}, \n" f"but got {test_result}"
    assert test_result == expected, msg


def test_remaining_attempts():
    test_attempts = [11, 10, 1, 0, -1]
    test_result = [20, 20, 20, 20, 20]
    expected = [10, 9, 0, ValueError, ValueError]
    for i, x in enumerate(test_attempts):
        try:
            result = Game.remaining_attempts(x)
        except Exception as e:
            result = type(e)
        test_result[i] = result
    msg = f"Expected {expected}\n" f"but got {test_result}"
    assert test_result == expected, msg


