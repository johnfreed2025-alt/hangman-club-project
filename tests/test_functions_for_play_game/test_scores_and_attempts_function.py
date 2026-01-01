import pytest
from hangman_code.functions_for_play_game.scores_and_attempts_function import remaining_attempts_function

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

#def test_update_score_function():
       #This function will update the score
       #return None