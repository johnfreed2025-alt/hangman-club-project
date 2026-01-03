import pytest

# from re import fullmatch
from hangman_code.play_game_functions import play_game

@pytest.fixture
def data():
    expected = {
        "game_name": "Ronald",
        "word": ["D", "O", "G"],
        "game_id": 42,
        "current_score": 52,
        "template": "Resume",
        "message": "The only way is up",
        "used_letters": ["A", "B", "C"],
        "game_started": True,
        "current_game_status": 1,
        "accepted_letters": ["O", "G"],
        "guess_result": ["_", "O", "G"],
        "attempts_remaining": 2,
        "guessed_word": ["BOG"],
        "words_guessed": ["BOG", "FOG"],
        "Start_Game_Selection": 2,
        "game_closed": False,
        "cumulative_score": 1010101012,
        "number_of_games_played": 100,
        "number_of_games_won": 3,
              }
    return expected


def test_play_game_returns_a_dict(data):
    letter = "A"
    result = play_game(letter, data)
    assert isinstance(result, dict)
    






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