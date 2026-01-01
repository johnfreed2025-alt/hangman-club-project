import pytest

# from re import fullmatch
from hangman_code.play_game_functions import play_game


def test_update_word():
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
            result = play_game(x)
        except Exception as e:
            result = type(e)
        test_result[i] = result
    msg = f"Expected {expected}, \n" f"but got {test_result}"
    assert test_result == expected, msg